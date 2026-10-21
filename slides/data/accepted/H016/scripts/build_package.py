#!/usr/bin/env python3
"""Build H016 manifests and package checksums after calculation and plotting."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from datetime import datetime
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
REPO = PACKAGE.parents[2]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def command(*args: str) -> str:
    return subprocess.check_output(args, cwd=REPO, text=True).strip()


def pdf_size(path: Path) -> str:
    output = command("pdfinfo", str(path))
    for line in output.splitlines():
        if line.startswith("Page size:"):
            return " ".join(line.split()[2:5])
    raise RuntimeError(f"No page size in {path}")


def png_size(path: Path) -> str:
    return command("identify", "-format", "%wx%h", str(path))


def main() -> None:
    branch = command("git", "rev-parse", "--abbrev-ref", "HEAD")
    head = command("git", "rev-parse", "HEAD")
    generated = datetime.now().astimezone().isoformat(timespec="seconds")

    producer_request = REPO / "docs/requests/active/H016_preupdates_data_driven_final_results_and_figures.md"
    requester_request = REPO.parent / "pre-updates/docs/requests/active/H016_JPsiJPsi_data_driven_final_results_and_figures.md"
    package_request = PACKAGE / "request.md"
    request_hashes = {sha256(path) for path in (producer_request, requester_request, package_request)}
    if len(request_hashes) != 1:
        raise RuntimeError("H016 requester and producer copies are not byte-identical")

    local_specs = [
        ("H016-F01", "Current data-driven f_DPS result", "fdps_current_result",
         "accepted f_DPS central/stat/method systematic and three included method groups",
         "f_DPS is accepted; group details follow H014 accepted inputs"),
        ("H016-F02", "Data-driven sigma_DPS result and uncertainty breakdown", "sigma_dps_preliminary_breakdown",
         "sigma_DPS(mJJ>7.5)=f_DPS*sigma_pair and source-level propagated components",
         "preliminary rho=0 statistical reference; five AN percentages used directly; unknown shared-systematic correlations use conditional independence"),
        ("H016-F03", "Data-driven sigma_eff result and uncertainty breakdown", "sigma_eff_preliminary_breakdown",
         "mass-extrapolated DPS denominator, BR cancellation, and exact source-by-source endpoint propagation",
         "preliminary rho=0 statistical reference; epsilon_m uncertainty not included"),
        ("H016-F04", "Current data-driven result summary", "data_driven_result_summary",
         "slide-ready f_DPS, sigma_DPS, and sigma_eff summary",
         "cross-section results are preliminary; rho=0 statistical reference approved for this update"),
    ]

    rows: list[dict[str, str]] = []
    for figure_id, title, stem, definition, caveat in local_specs:
        pdf = PACKAGE / "figures" / f"{stem}.pdf"
        png = PACKAGE / "figures" / f"{stem}.png"
        rows.append({
            "id": figure_id,
            "title": title,
            "status": "ready",
            "pdf": str(pdf.relative_to(PACKAGE)),
            "pdf_sha256": sha256(pdf),
            "pdf_page_size": pdf_size(pdf),
            "png": str(png.relative_to(PACKAGE)),
            "png_sha256": sha256(png),
            "png_size": png_size(png),
            "machine_sources": "inputs.json;results.json;uncertainty_source_map.csv",
            "definition": definition,
            "caveat": caveat,
        })

    reused_pdf = REPO / "docs/answers/H015_preupdates_data_driven_slide_figures/figures/control_region_variations.pdf"
    reused_png = REPO / "docs/answers/H015_preupdates_data_driven_slide_figures/figures/control_region_variations.png"
    rows.append({
        "id": "H016-F05",
        "title": "CR boundary and zero/MC SPS-leakage variants",
        "status": "reused_accepted_H015_F07",
        "pdf": str(reused_pdf.relative_to(REPO)),
        "pdf_sha256": sha256(reused_pdf),
        "pdf_page_size": pdf_size(reused_pdf),
        "png": str(reused_png.relative_to(REPO)),
        "png_sha256": sha256(reused_png),
        "png_size": png_size(reused_png),
        "machine_sources": "docs/answers/H015_preupdates_data_driven_slide_figures/data/control_region_variations.csv",
        "definition": "accepted CR-boundary and zero/MC-leakage variants with one group envelope",
        "caveat": "reused without copying; MC-leakage variants are members of the CR envelope, not an extra systematic",
    })

    fields = list(rows[0])
    with (PACKAGE / "figure_manifest.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    md = ["# H016 figure manifest", "", "Package status: `ready` for consumer review.", ""]
    for row in rows:
        md.extend([
            f"## {row['id']} - {row['title']}", "",
            f"- Status: `{row['status']}`",
            f"- PDF: `{row['pdf']}` (`{row['pdf_sha256']}`)",
            f"- PNG: `{row['png']}` (`{row['png_sha256']}`)",
            f"- Machine sources: `{row['machine_sources']}`",
            f"- Definition: {row['definition']}",
            f"- Caveat: {row['caveat']}", "",
        ])
    (PACKAGE / "figure_manifest.md").write_text("\n".join(md), encoding="utf-8")

    metadata = {
        "request_id": "H016",
        "status": "ready",
        "generated_at": generated,
        "producer_branch": branch,
        "producer_head": head,
        "request_sha256": next(iter(request_hashes)),
        "request_copies_byte_identical": True,
        "analysis_runtime": "CMSSW_10_6_20 / ROOT 6.14/09 / cmssw-el7",
        "analysis_rerun": False,
        "fit_bootstrap_systematic_rerun": False,
        "compatibility_validation": {
            "environment": "CMSSW_10_6_20 / ROOT 6.14/09 / cmssw-el7",
            "compiled_source": "tests/atlas_data_driven_sps/fit_pp_2d_adaptive.cpp",
            "compile_status": 1,
            "aclic_output_location": "/tmp/leyao/h016_aclic",
            "fit_run": False,
            "record": "validation.txt",
            "mass_extrapolation_reproduction": True
        },
        "new_operations": ["deterministic source-level cross-section propagation", "F02-F04 presentation redraw", "mass-extrapolation provenance freeze", "manifest and checksum generation"],
        "physics_status": {
            "f_DPS": "accepted",
            "sigma_DPS": "preliminary conditional propagation",
            "sigma_eff": "preliminary conditional propagation",
            "statistical_covariance": "unresolved; rho=0 preliminary use approved by user",
            "mass_extrapolation_uncertainty": "fixed for this preliminary round by explicit 2026-08-29 user instruction; not asserted zero",
            "pair_systematics": "five AN percentages used directly without normalization to rounded 2.5 pb",
            "sigma_eff_systematics": "exact endpoint propagation for every independent source",
        },
        "cr_sps_leakage": {
            "included_in_current_method_systematic": True,
            "group": "CR definition/purity envelope",
            "double_counted_as_separate_source": False,
            "future_improvement_recorded": True,
        },
        "tracked_dirty_files_at_intake": [],
        "files_not_to_overwrite": [
            "tests/atlas_data_driven_sps/results/fdps_systematics_global_nominal_v1/",
            "tests/atlas_data_driven_sps/results/route9p3_global_calibrated_allpairs/bootstrap_fixed500_global_nominal_v1/",
            "docs/answers/H015_preupdates_data_driven_slide_figures/",
        ],
    }
    (PACKAGE / "package_metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    checksum_path = PACKAGE / "package_checksums.sha256"
    files = sorted(
        path for path in PACKAGE.rglob("*")
        if path.is_file() and path != checksum_path and "__pycache__" not in path.parts
    )
    lines = [f"{sha256(path)}  {path.relative_to(PACKAGE)}" for path in files]
    checksum_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Built H016 package manifest with {len(rows)} figures and {len(files)} checksummed files")


if __name__ == "__main__":
    main()
