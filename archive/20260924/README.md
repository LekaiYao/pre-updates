# 20260924 X 分析 update

汇报日期：2026-09-24；归档执行日期：2026-09-30。两单元均已获用户批准，共17页（首页及正文7页、致谢1页、backup9页）。

正式PDF：`main.pdf`；历史副本：`../../pbpb_updates/X_update_260924.pdf`。两者与归档时 `build/main.pdf` 逐字节一致；完整构建无告警，17页与归档前已验收版本渲染一致。22项源码、图片、宏及配置的SHA256见 `source_manifest.json`。

在本目录执行 `latexmk -pdf -outdir=build slides/main.tex` 可按既有TeX环境重建。根目录main.tex和project_setup.tex为标准脚本副本，重建入口使用保留原路径的slides/main.tex。

本轮tmp的42个文件已打包并逐项核验至 `../../docs/archive/20260924_tmp/tmp_20260924.tar.gz`，原tmp已清空。需要恢复历史预览时，在项目根执行 `tar -xzf docs/archive/20260924_tmp/tmp_20260924.tar.gz`；恢复前确认当前tmp无冲突文件。

素材验收及冻结证据继续保留于 `../../docs/verification/20260924/`；本轮归档核验见其中 `archive_20260930/archive_checks.json`。本次未提交或推送Git；不改变展示内容和既有科学结论边界。

本地记录说明：文中 `docs/`、`tmp/` 和 `build/` 路径属于本地工作区，按仓库规则不随 Git 发布；从 GitHub 获取的副本不包含这些验收记录、临时预览或恢复包。归档源码、依赖清单和正式 PDF 随仓库保存。以上未提交或推送的描述（如有）仅指当时的归档操作。
