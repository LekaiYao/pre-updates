# Logo 资产

本目录保存各分析 branch 可复用的机构 logo。封面只选择实际参与者 affiliation 对应的
logo，不因文件存在而全部展示；参与者、reporter、日期和 logo 组合统一在
`slides/project_setup.tex` 中填写。

| 文件 | 机构 |
|---|---|
| `CERN.png` | CERN |
| `CMS.png` | CMS Collaboration |
| `IHEP.png` | Institute of High Energy Physics |
| `IST.png` | Instituto Superior Técnico, Universidade de Lisboa |
| `LIP.png` | Laboratório de Instrumentação e Física Experimental de Partículas |
| `NNU.png` | Nanjing Normal University |
| `THU.png` | Tsinghua University |
| `TexasAM.png` | Texas A&M University |

命名使用机构认可的简称或可安全用于 TeX 路径的规范化名称：`IST.png` 不写作
`LU.png`；Texas A&M 官方不接受 `TAMU` 作为对外称呼，因此文件名使用
`TexasAM.png`，避免路径中的 `&`。

五个 logo 的 16:9 封面可从等高 `1.653cm`、间距 `0.30cm` 起步。logo 数量或长宽比
变化后，应单独编译封面并检查总宽度、纵向对齐、清晰度和视觉重心。机构标识的外部
使用须遵守各机构品牌规范。
