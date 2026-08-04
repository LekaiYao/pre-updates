> Lifecycle: historical QA/implementation evidence, archived on 2026-08-02.

# H006 slides revision assessment

## 结论

21项建议中，大部分是slides文字、标题、顺序和解释增强；需要代码侧新增/冻结内容的
部分已拆为 H008--H010。所有新产物accepted前不更新slides。

## 不需要新request的项目

- P1--P10的标题、goal、术语和primary定义；
- P13--P19的pseudoexperiment、rho、bias、pull、30 seeds说明；
- 删除phase-space独立页并把fiducial match合并到公式页；
- P20/P22现有variation/envelope的教学性解释。

这些内容已有accepted H006代码/metadata支持，可在最终改稿时直接完成。

## 已有artifact，不重复建立request

以下三个nominal component-fit figures已经存在：

- `delta_phi_component_shapes_normalized.pdf`
- `evt_mass_component_shapes_normalized.pdf`
- `evt_y_component_shapes_normalized.pdf`

路径：

```text
../JPsiJPsi/tests/atlas_data_driven_sps/results/
e3_shape_systematics/nominal/component_fits/
```

按“已有artifact交付不新建request”规则，后续只做路径、数值、标签、物理口径和视觉
验收，并在用户确认后纳入accepted manifest。

## 新requests

- H008：control-region absolute physics evidence；
- H009：weights、toys、closure、method-systematic和E4误差breakdown；
- H010：冻结可与H006并列的current CMS AN nominal结果。

## 文字修正

用户给出的英文标题在制作时将规范为：

- `Data-driven SPS/DPS separation`（不是 `seperation`）；
- subtitle：`Based on the ATLAS 8 TeV measurement` 或用户指定的
  `from the ATLAS 8 TeV measurement`；
- `Measured sigma_SPS vs. theory prediction` 使用LaTeX物理符号排版。
