"""Regression tests for source masking and real Git staging/hook behavior."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("checker", ROOT / "scripts/check_tex_internal_ids.py")
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class SourceTests(unittest.TestCase):
    def setUp(self):
        self.pattern = CHECKER.load_pattern('{"prefixes": ["REQ", "TASK"]}')

    def hits(self, source, selected=None):
        return CHECKER.scan("slides/example.tex", source, selected, self.pattern)

    def test_full_document_and_fragment(self):
        for text in ("REQ12", "\\begin{frame}{REQ12}\n\\end{frame}",
                     "\\begin{document}REQ12\\end{document}"):
            with self.subTest(text=text):
                self.assertEqual(len(self.hits(text)), 1)

    def test_document_comments_do_not_change_scope(self):
        text = "% \\end{document}\n\\begin{document}\n% \\end{document}\nREQ12\n\\end{document}"
        self.assertEqual(self.hits(text)[0][1], 4)
        self.assertEqual(len(self.hits("% \\begin{document}\nREQ12")), 1)

    def test_preamble_and_trailing_text_excluded(self):
        self.assertEqual(self.hits("REQ12\n\\begin{document}\nValid\n\\end{document}\nTASK3"), [])

    def test_comments_and_escaped_percent(self):
        self.assertEqual(self.hits("Valid % REQ12\n"), [])
        self.assertEqual(len(self.hits(r"\% REQ12")), 1)
        self.assertEqual(self.hits(r"\\% REQ12"), [])

    def test_balanced_multiline_paths_and_labels(self):
        text = r"""\includegraphics[
width={0.5\textwidth}]
{figures/REQ12/{TASK3}.pdf}
\input{parts/REQ12}
\label{REQ12}
\begin{frame}[label=REQ12]{Visible title}
\end{frame}
"""
        self.assertEqual(self.hits(text), [])

    def test_visible_link_text_and_caption_retained(self):
        text = r"""\href{https://example.test/REQ12}{TASK3}
\hyperref[REQ12]{TASK4}
\caption{REQ13}
\begin{frame}[label=TASK5]{REQ14}
"""
        self.assertEqual([row[2] for row in self.hits(text)], [["TASK3"], ["TASK4"], ["REQ13"], ["REQ14"]])

    def test_citation_keys_hidden_notes_visible(self):
        self.assertEqual(self.hits(r"\cite{REQ12}\ref{TASK3}"), [])
        self.assertEqual(self.hits(r"\citep[REQ12]{TASK3}")[0][2], ["REQ12"])

    def test_boundaries_and_configured_prefixes(self):
        self.assertEqual(self.hits("XREQ12 REQ12x REQ12_x x_REQ12 req12 H014"), [])
        self.assertEqual(self.hits("(REQ12), TASK3.")[0][2], ["REQ12", "TASK3"])

    def test_selected_lines_and_line_numbers(self):
        text = "\\includegraphics{\nREQ12.pdf}\nTASK3\nREQ13"
        self.assertEqual(self.hits(text, {3})[0][1:3], (3, ["TASK3"]))
        self.assertEqual(self.hits(text, {1, 2}), [])

    def test_empty_and_invalid_config(self):
        self.assertIsNone(CHECKER.load_pattern('{"prefixes": []}'))
        for bad in ('{}', '[]', '{"prefixes": "REQ"}', '{"prefixes": [""]}',
                    '{"prefixes": ["REQ.*"]}', '{"prefixes": [12]}',
                    '{"prefixes": [], "typo": true}'):
            with self.subTest(config=bad), self.assertRaises(ValueError):
                CHECKER.load_pattern(bad)


class GitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="tex-id-test-")
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.env = os.environ.copy()
        self.env["PYTHONDONTWRITEBYTECODE"] = "1"
        self.git("init", "-q")
        self.git("config", "user.name", "Checker regression test")
        self.git("config", "user.email", "checker@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "core.hooksPath", ".githooks")
        self.write(".tex-internal-ids.json", '{"prefixes": ["REQ", "TASK"]}\n')
        self.write("slides/main.tex", "\\begin{document}\nValid text\n\\end{document}\n")
        self.git("add", ".")
        self.git("commit", "-qm", "fixture baseline")
        for rel in ("scripts/check_tex_internal_ids.py", ".githooks/pre-commit"):
            target = self.repo / rel
            target.parent.mkdir(exist_ok=True)
            shutil.copy2(ROOT / rel, target)

    def write(self, path, text):
        p = self.repo / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def git(self, *args, check=True):
        return subprocess.run(["git", *args], cwd=self.repo, env=self.env,
                              text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=check)

    def check_ids(self, mode="--staged"):
        return subprocess.run([sys.executable, "-B", "scripts/check_tex_internal_ids.py", mode],
                              cwd=self.repo, env=self.env, text=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def test_staged_content_cannot_be_hidden_by_worktree_edit(self):
        self.write("slides/main.tex", "\\begin{document}\nREQ12\n\\end{document}\n")
        self.git("add", "slides/main.tex")
        self.write("slides/main.tex", "\\begin{document}\nValid\n\\end{document}\n")
        result = self.check_ids()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("slides/main.tex:2", result.stderr)
        self.assertEqual(self.check_ids("--all").returncode, 0)

    def test_unstaged_content_not_checked_by_hook(self):
        self.write("slides/main.tex", "REQ12")
        self.assertEqual(self.check_ids().returncode, 0)
        self.assertEqual(self.check_ids("--all").returncode, 1)

    def test_staged_configuration_used(self):
        self.write("slides/part.tex", "REQ12")
        self.git("add", "slides/part.tex")
        self.write(".tex-internal-ids.json", '{"prefixes": []}')
        self.assertEqual(self.check_ids().returncode, 1)
        self.assertEqual(self.check_ids("--all").returncode, 0)

    def test_new_prefix_staged_with_source(self):
        self.write(".tex-internal-ids.json", '{"prefixes": ["NEW"]}')
        self.write("slides/part.tex", "NEW42")
        self.git("add", ".tex-internal-ids.json", "slides/part.tex")
        self.write(".tex-internal-ids.json", '{"prefixes": ["REQ"]}')
        self.assertEqual(self.check_ids().returncode, 1)

    def test_missing_or_invalid_staged_config_fails(self):
        self.git("rm", ".tex-internal-ids.json")
        self.assertEqual(self.check_ids().returncode, 2)
        self.write(".tex-internal-ids.json", '{"prefixes": [12]}')
        self.git("add", ".tex-internal-ids.json")
        self.assertEqual(self.check_ids().returncode, 2)

    def test_unchanged_old_id_not_blocked(self):
        # Make an old ID part of the fixture baseline using a different prefix.
        self.write(".tex-internal-ids.json", '{"prefixes": ["TASK"]}')
        self.write("slides/part.tex", "REQ12\nOld text\n")
        self.git("add", ".tex-internal-ids.json", "slides/part.tex")
        self.git("commit", "-qm", "historical text under earlier policy")
        self.write(".tex-internal-ids.json", '{"prefixes": ["REQ", "TASK"]}')
        self.write("slides/part.tex", "REQ12\nNew text\n")
        self.git("add", ".tex-internal-ids.json", "slides/part.tex")
        self.assertEqual(self.check_ids().returncode, 0)
        self.assertEqual(self.check_ids("--all").returncode, 1)

    def test_fragment_paths_with_spaces_unicode_and_newline(self):
        for filename in ("slides/a b.tex", "slides/中文.tex", "slides/a\nb.tex"):
            with self.subTest(filename=filename):
                self.write(filename, "REQ12")
                self.git("add", filename)
        self.assertEqual(self.check_ids().returncode, 1)

    def test_plus_prefixed_line_and_deleted_file(self):
        self.write("slides/part.tex", "++REQ12\n")
        self.git("add", "slides/part.tex")
        self.assertEqual(self.check_ids().returncode, 1)
        self.git("rm", "--cached", "slides/part.tex")
        self.git("rm", "slides/main.tex")
        self.assertEqual(self.check_ids().returncode, 0)

    def test_real_hook_blocks_commit_then_allows_rewrite(self):
        self.write("slides/part.tex", "REQ12 result\n")
        self.git("add", "slides/part.tex")
        before = self.git("rev-parse", "HEAD").stdout
        blocked = self.git("commit", "-qm", "must be rejected", check=False)
        self.assertNotEqual(blocked.returncode, 0)
        self.assertIn("REQ12", blocked.stderr)
        self.assertEqual(self.git("rev-parse", "HEAD").stdout, before)
        self.write("slides/part.tex", "Data-driven result % REQ12\n")
        self.git("add", "slides/part.tex")
        self.git("commit", "-qm", "reader-facing wording")
        self.assertNotEqual(self.git("rev-parse", "HEAD").stdout, before)


if __name__ == "__main__":
    unittest.main()
