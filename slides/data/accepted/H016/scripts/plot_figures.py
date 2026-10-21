#!/usr/bin/env python3
"""Create H016 result-summary figures from results.json."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


PACKAGE = Path(__file__).resolve().parents[1]
FIGURES = PACKAGE / "figures"
RESULTS = json.loads((PACKAGE / "results.json").read_text(encoding="utf-8"))
INPUTS = json.loads((PACKAGE / "inputs.json").read_text(encoding="utf-8"))

BLUE = "#3b6ea8"
ORANGE = "#d97732"
GREEN = "#2a8f6a"
PURPLE = "#7655a6"
DARK = "#263238"
LIGHT = "#e9eef5"


def setup_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 16,
            "axes.titlesize": 23,
            "axes.labelsize": 19,
            "xtick.labelsize": 15,
            "ytick.labelsize": 15,
            "legend.fontsize": 14,
            "axes.linewidth": 1.3,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )


def save(fig: plt.Figure, stem: str) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES / f"{stem}.pdf", facecolor="white")
    fig.savefig(FIGURES / f"{stem}.png", dpi=180, facecolor="white")
    plt.close(fig)


def result_line(ax: plt.Axes, text: str, color: str = DARK, y: float = 0.72) -> None:
    ax.text(0.5, y, text, transform=ax.transAxes, ha="center", va="center",
            fontsize=22, fontweight="bold", color=color)


def plot_fdps() -> None:
    r = RESULTS["f_DPS"]
    groups = INPUTS["data_driven_fraction"]["method_groups"]
    fig, (left, right) = plt.subplots(
        1, 2, figsize=(13.333, 7.5), gridspec_kw={"width_ratios": [1.03, 0.97]},
        constrained_layout=True,
    )
    fig.suptitle(r"Current data-driven $f_{DPS}$ result", fontsize=26, fontweight="bold")

    central = r["central"]
    left.axvline(central, color=DARK, linestyle="--", linewidth=1.5, alpha=0.7)
    left.errorbar(
        central, 0.62, xerr=r["stat"], fmt="o", markersize=11, color=BLUE,
        linewidth=3.0, capsize=8, label="Statistical (fixed-500 bootstrap)",
    )
    left.errorbar(
        central, 0.38,
        xerr=np.array([[r["method_syst_down"]], [r["method_syst_up"]]]),
        fmt="s", markersize=9, color=ORANGE, linewidth=3.0, capsize=8,
        label="Method systematic",
    )
    left.set_ylim(0.12, 0.88)
    left.set_xlim(0.095, 0.245)
    left.set_yticks([0.38, 0.62])
    left.set_yticklabels(["Method syst.", "Stat."])
    left.set_xlabel(r"$f_{DPS}$")
    left.grid(axis="x", alpha=0.25)
    left.legend(loc="lower center", bbox_to_anchor=(0.5, -0.24), frameon=False)
    left.text(
        0.5, 0.96,
        r"$f_{DPS}=0.170\pm0.059\,\mathrm{(stat.)}^{+0.010}_{-0.011}\,\mathrm{(method\ syst.)}$",
        transform=left.transAxes, ha="center", va="top", fontsize=18,
    )

    labels = ["Single-J category", "CR definition / purity", "Pure-DPS closure"]
    keys = ["single_j_category", "cr_definition_and_purity", "pure_dps_full_workflow_closure"]
    y = np.arange(3)[::-1]
    up = np.array([groups[key]["up"] for key in keys])
    down = np.array([groups[key]["down"] for key in keys])
    right.barh(y, up, color=GREEN, height=0.34, label="Up")
    right.barh(y, -down, color=PURPLE, height=0.34, label="Down")
    for yi, u, d in zip(y, up, down):
        right.text(u + 0.0002, yi, f"+{u:.4f}", va="center", fontsize=13)
        right.text(-d - 0.0002, yi, f"-{d:.4f}", ha="right", va="center", fontsize=13)
    right.axvline(0.0, color=DARK, linewidth=1.2)
    right.set_yticks(y)
    right.set_yticklabels(labels)
    right.set_xlim(-0.0120, 0.0120)
    right.set_xlabel(r"Absolute effect on $f_{DPS}$")
    right.set_title(
        "Three method-systematic groups\nSeparate quadrature: +0.0102/-0.0111",
        fontsize=15, pad=8,
    )
    right.grid(axis="x", alpha=0.22)
    right.legend(loc="lower center", bbox_to_anchor=(0.5, -0.22), ncol=2, frameon=False)
    save(fig, "fdps_current_result")


def plot_sigma_dps() -> None:
    r = RESULTS["sigma_DPS_mJJ_gt_7p5_pb"]
    no_mass = RESULTS["sigma_DPS_no_mJJ_cut_pb"]
    c = r["components"]
    fig, (left, right) = plt.subplots(
        1, 2, figsize=(13.333, 7.5), gridspec_kw={"width_ratios": [1.05, 0.95]},
        constrained_layout=True,
    )
    fig.suptitle(r"Data-driven DPS cross section", fontsize=26, fontweight="bold")

    left.axis("off")
    left.text(0.5, 0.90, r"$\sigma_{DPS}=f_{DPS}\,\sigma_{pair}$", ha="center", fontsize=25)
    left.text(0.5, 0.78, r"$=0.170423\times37.2\ \mathrm{pb}$", ha="center", fontsize=20)
    result_line(
        left,
        r"$6.34\pm2.21\,\mathrm{(stat.)}^{+0.57}_{-0.60}\,\mathrm{(syst.)}\ \mathrm{pb}$",
        BLUE,
        0.61,
    )
    left.text(0.5, 0.50, r"Fiducial pair region: $m(J/\psi J/\psi)>7.5$ GeV",
              ha="center", fontsize=17)
    left.annotate("", xy=(0.50, 0.31), xytext=(0.50, 0.44), xycoords="axes fraction",
                  arrowprops={"arrowstyle": "-|>", "lw": 2.0, "color": DARK})
    left.text(0.5, 0.25, r"For $\sigma_{eff}$: divide by $\epsilon_m=0.987339$",
              ha="center", fontsize=17)
    left.text(0.5, 0.14, rf"$\sigma_{{DPS}}^{{\mathrm{{no\ mass\ cut}}}}={no_mass['central']:.3f}$ pb",
              ha="center", fontsize=20, color=GREEN, fontweight="bold")
    left.text(0.5, 0.03, "Preliminary result",
              ha="center", fontsize=14, color="#5b6470")

    f_group_effects = c["f_DPS_method_groups"]
    pair_effects = c["AN_pair_sources"]
    f_method_up = np.sqrt(sum(effect["up"] ** 2 for effect in f_group_effects.values()))
    f_method_down = np.sqrt(sum(effect["down"] ** 2 for effect in f_group_effects.values()))
    labels = [
        r"", "Pair total stat.", r" syst.",
        "Pair BR", "CMS luminosity", "Acceptance / efficiency", "Lifetime variable", "Fitter stability",
    ]
    effects = [
        c["stat_from_f_DPS"], c["stat_from_pair_total"], max(f_method_up, f_method_down),
        pair_effects["branching_fraction"], pair_effects["cms_luminosity"],
        pair_effects["acceptance_efficiency"], pair_effects["lifetime_variable"],
        pair_effects["fitter_stability"],
    ]
    colors = [BLUE, BLUE] + [ORANGE] * 6
    y = np.arange(len(labels))[::-1]
    right.barh(y, effects, color=colors, height=0.52)
    for yi, value in zip(y, effects):
        right.text(value + 0.04, yi, f"{value:.3f} pb", va="center", fontsize=14)
    right.set_yticks(y)
    right.set_yticklabels(labels)
    right.set_ylim(-0.5, len(labels) + 0.2)
    right.tick_params(axis="y", labelsize=12)
    right.set_xlim(0, 2.85)
    right.set_xlabel("Absolute propagated component")
    right.set_title(
        "Source-level components\nTotal stat.: 2.209 pb\nTotal syst.: +0.575/-0.597 pb",
        fontsize=14, pad=6,
    )
    right.grid(axis="x", alpha=0.24)
    save(fig, "sigma_dps_preliminary_breakdown")


def plot_sigma_eff() -> None:
    r = RESULTS["sigma_eff_mb"]
    c = r["components"]
    mass = RESULTS["mass_extrapolation"]
    fig, (left, right) = plt.subplots(
        1, 2, figsize=(13.333, 7.5), gridspec_kw={"width_ratios": [1.08, 0.92]},
        constrained_layout=True,
    )
    fig.suptitle(r"Effective DPS cross section", fontsize=26, fontweight="bold")

    left.axis("off")
    left.text(0.5, 0.91, r"$\sigma_{eff}=\frac{1}{2}\frac{\sigma^2(J/\psi)}{\sigma_{DPS}^{\mathrm{no\ mass\ cut}}}$",
              ha="center", fontsize=25)
    left.text(0.5, 0.76, r"$X=B\,\sigma(J/\psi)=10.63$ nb", ha="center", fontsize=18)
    left.text(0.5, 0.66, rf"$\epsilon_m={mass['epsilon_m']:.6f}$  from DPS GEN-only event mixing",
              ha="center", fontsize=17)
    left.text(0.5, 0.56, r"$B$ cancels between $X^2$ and the pair-visible denominator",
              ha="center", fontsize=16, color=GREEN)
    result_line(
        left,
        r"$\sigma_{eff}=2.48\pm0.86\,\mathrm{(stat.)}^{+0.25}_{-0.22}\,\mathrm{(syst.)}\ \mathrm{mb}$",
        BLUE,
        0.38,
    )
    left.text(0.5, 0.22, "Prompt J/psi: 10 < pT < 40 GeV, |y| < 2.0",
              ha="center", fontsize=16)
    left.text(0.5, 0.10, "Preliminary result",
              ha="center", fontsize=14, color="#5b6470")

    f_endpoints = c["f_DPS_method_endpoint_sources"]
    pair_endpoints = c["CMS_pair_endpoint_sources"]
    labels = [
        r"", "Pair total stat.", "ATLAS single stat.",
        "Single-J category", "CR definition / purity", "Pure-DPS closure",
        "CMS luminosity", "Acceptance / efficiency", "Lifetime variable", "Fitter stability",
        "ATLAS bin syst.", "ATLAS luminosity",
    ]
    effects = [
        c["stat_from_f_DPS"], c["stat_from_pair_total"], c["stat_from_ATLAS_single"],
        max(f_endpoints["single_j_category"].values()),
        max(f_endpoints["cr_definition_and_purity"].values()),
        max(f_endpoints["pure_dps_full_workflow_closure"].values()),
        max(pair_endpoints["cms_luminosity"].values()),
        max(pair_endpoints["acceptance_efficiency"].values()),
        max(pair_endpoints["lifetime_variable"].values()),
        max(pair_endpoints["fitter_stability"].values()),
        max(c["ATLAS_single_bin_endpoint"].values()),
        max(c["ATLAS_luminosity_endpoint"].values()),
    ]
    colors = [BLUE, BLUE, BLUE] + [ORANGE] * 9
    y = np.arange(len(labels))[::-1]
    right.barh(y, effects, color=colors, height=0.50)
    for yi, value in zip(y, effects):
        right.text(value + 0.012, yi, f"{value:.3f}", va="center", fontsize=10.5)
    right.set_yticks(y)
    right.set_yticklabels(labels)
    right.set_xlim(0, 1.08)
    right.set_xlabel("Absolute effect [mb]")
    right.set_ylim(-0.5, len(labels) + 0.8)
    right.tick_params(axis="y", labelsize=11)
    right.set_title(
        "Exact source-by-source endpoints\nBR cancels; totals: 0.863 stat., +0.253/-0.224 syst.",
        fontsize=13, pad=8,
    )
    right.grid(axis="x", alpha=0.24)
    save(fig, "sigma_eff_preliminary_breakdown")


def plot_summary() -> None:
    f = RESULTS["f_DPS"]
    d = RESULTS["sigma_DPS_mJJ_gt_7p5_pb"]
    e = RESULTS["sigma_eff_mb"]
    fig, ax = plt.subplots(figsize=(13.333, 7.5), constrained_layout=True)
    ax.axis("off")
    ax.set_title("Current data-driven results", fontsize=28, fontweight="bold", pad=18)

    y = [0.74, 0.49, 0.24]
    colors = [GREEN, BLUE, PURPLE]
    names = [r"DPS fraction  $f_{DPS}$", r"DPS cross section  $\sigma_{DPS}$", r"Effective cross section  $\sigma_{eff}$"]
    values = [
        r"$0.170\pm0.059\,\mathrm{(stat.)}^{+0.010}_{-0.011}\,\mathrm{(method\ syst.)}$",
        r"$6.34\pm2.21\,\mathrm{(stat.)}^{+0.57}_{-0.60}\,\mathrm{(syst.)}\ \mathrm{pb}$",
        r"$2.48\pm0.86\,\mathrm{(stat.)}^{+0.25}_{-0.22}\,\mathrm{(syst.)}\ \mathrm{mb}$",
    ]
    notes = [
        "Accepted fixed-500 statistical and three-group method uncertainty",
        r"Fiducial $m(J/\psi J/\psi)>7.5$ GeV; preliminary propagation",
        r"No pair-mass cut after $\epsilon_m=0.987339$ extrapolation; preliminary propagation",
    ]
    for yi, color, name, value, note in zip(y, colors, names, values, notes):
        ax.plot([0.055, 0.055], [yi - 0.085, yi + 0.085], color=color, linewidth=8,
                transform=ax.transAxes, solid_capstyle="round")
        ax.text(0.09, yi + 0.055, name, transform=ax.transAxes, fontsize=19,
                fontweight="bold", color=color, va="center")
        ax.text(0.50, yi + 0.01, value, transform=ax.transAxes, fontsize=22,
                fontweight="bold", ha="center", va="center", color=DARK)
        ax.text(0.09, yi - 0.065, note, transform=ax.transAxes, fontsize=14.5,
                color="#5b6470", va="center")
    ax.text(
        0.5, 0.055,
        "Cross-section results are preliminary",
        transform=ax.transAxes, ha="center", va="center", fontsize=14,
        bbox={"boxstyle": "round,pad=0.38", "facecolor": LIGHT, "edgecolor": "none"},
    )
    save(fig, "data_driven_result_summary")


def main() -> None:
    setup_style()
    plot_fdps()
    plot_sigma_dps()
    plot_sigma_eff()
    plot_summary()
    print("Created four H016 figures in PDF and PNG")


if __name__ == "__main__":
    main()
