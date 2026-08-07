#!/usr/bin/env python3
"""Deterministic H013 propagation for the current data-driven f_DPS."""

import csv
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent

F = 0.169980427756
F_STAT = 0.056796474528
F_CATEGORY_UP = 0.007263523592
F_CATEGORY_DOWN = 0.0
F_CR_UP = 0.001318512530
F_CR_DOWN = 0.010590504745
P_PB = 37.2
P_STAT_PB = 0.6
P_SYST_PB = 2.5
P_BR_REL = 0.0078
X_NB = 10.63
X_STAT_NB = 0.01
X_BIN_SYST_NB = 0.09
ATLAS_LUMI_REL = 0.0113
BR = 0.05961


def sigma_dps(f=F, p=P_PB):
    return f * p


def sigma_eff(f=F, p=P_PB, x=X_NB):
    # X=B*sigma(single), while p is the full pair cross section.
    return 0.001 * 0.5 * x * x / (BR * BR * f * p)


def quadrature(values):
    return math.sqrt(sum(value * value for value in values))


def product_stat(rho):
    variance = (
        P_PB**2 * F_STAT**2
        + F**2 * P_STAT_PB**2
        + 2.0 * rho * F * P_PB * F_STAT * P_STAT_PB
    )
    return math.sqrt(max(0.0, variance))


def eff_stat(rho):
    dps = sigma_dps()
    eff = sigma_eff()
    return eff * math.hypot(product_stat(rho) / dps, 2.0 * X_STAT_NB / X_NB)


def one_sided_effect(func, **changed):
    return func(**changed) - func()


def build_results():
    dps = sigma_dps()
    eff = sigma_eff()

    # Current category/CR groups are user-approved as independent provisional
    # groups. The AN pair aggregate is kept separate and treated as independent
    # only for the provisional reference because no shared correction variation
    # is present in the current f_DPS partial systematic.
    dps_syst_up = quadrature([
        one_sided_effect(sigma_dps, f=F + F_CATEGORY_UP),
        one_sided_effect(sigma_dps, f=F + F_CR_UP),
        one_sided_effect(sigma_dps, p=P_PB + P_SYST_PB),
    ])
    dps_syst_down = quadrature([
        -one_sided_effect(sigma_dps, f=F - F_CR_DOWN),
        -one_sided_effect(sigma_dps, p=P_PB - P_SYST_PB),
    ])

    pair_nonbr_syst = math.sqrt(P_SYST_PB**2 - (P_PB * P_BR_REL) ** 2)
    single_lumi = X_NB * ATLAS_LUMI_REL
    eff_up_effects = [
        one_sided_effect(sigma_eff, f=F - F_CR_DOWN),
        one_sided_effect(sigma_eff, p=P_PB - pair_nonbr_syst),
        one_sided_effect(sigma_eff, x=X_NB + X_BIN_SYST_NB),
        one_sided_effect(sigma_eff, x=X_NB + single_lumi),
    ]
    eff_down_effects = [
        -one_sided_effect(sigma_eff, f=F + F_CATEGORY_UP),
        -one_sided_effect(sigma_eff, f=F + F_CR_UP),
        -one_sided_effect(sigma_eff, p=P_PB + pair_nonbr_syst),
        -one_sided_effect(sigma_eff, x=X_NB - X_BIN_SYST_NB),
        -one_sided_effect(sigma_eff, x=X_NB - single_lumi),
    ]
    eff_syst_up = quadrature(eff_up_effects)
    eff_syst_down = quadrature(eff_down_effects)

    rows = [
        {
            "quantity": "sigma_DPS", "scenario": "recommended_partial_syst_stat_unresolved",
            "rho_f_pair_stat": "unresolved", "central": dps, "unit": "pb",
            "stat_up": "", "stat_down": "", "partial_syst_up": dps_syst_up,
            "partial_syst_down": dps_syst_down,
            "recommended_display": "6.32 +0.51/-0.58 (partial syst) pb; stat pending covariance",
            "status": "recommended_central_and_partial_systematic_only",
        },
        {
            "quantity": "sigma_eff", "scenario": "recommended_partial_syst_stat_unresolved",
            "rho_f_pair_stat": "unresolved", "central": eff, "unit": "mb",
            "stat_up": "", "stat_down": "", "partial_syst_up": eff_syst_up,
            "partial_syst_down": eff_syst_down,
            "recommended_display": "2.51 +0.26/-0.20 (partial syst) mb; stat pending covariance",
            "status": "recommended_central_and_partial_systematic_only",
        },
    ]
    for rho, scenario in [(-1.0, "rho_minus1_sensitivity"), (0.0, "rho0_independent_reference"), (1.0, "rho_plus1_sensitivity")]:
        rows.extend([
            {
                "quantity": "sigma_DPS", "scenario": scenario, "rho_f_pair_stat": rho,
                "central": dps, "unit": "pb", "stat_up": product_stat(rho),
                "stat_down": product_stat(rho), "partial_syst_up": dps_syst_up,
                "partial_syst_down": dps_syst_down,
                "recommended_display": "reference_or_sensitivity_only",
                "status": "provisional_partial_systematic_stat_correlation_unresolved",
            },
            {
                "quantity": "sigma_eff", "scenario": scenario, "rho_f_pair_stat": rho,
                "central": eff, "unit": "mb", "stat_up": eff_stat(rho),
                "stat_down": eff_stat(rho), "partial_syst_up": eff_syst_up,
                "partial_syst_down": eff_syst_down,
                "recommended_display": "reference_or_sensitivity_only",
                "status": "provisional_partial_systematic_stat_correlation_unresolved",
            },
        ])
    details = {
        "pair_nonbr_syst_pb_for_sigma_eff": pair_nonbr_syst,
        "atlas_single_lumi_nb": single_lumi,
        "visible_sigma_dps_pb": BR * BR * dps,
        "sigma_dps_partial_syst_source_effects_pb": {
            "category_up": P_PB * F_CATEGORY_UP,
            "category_down": 0.0,
            "control_region_up": P_PB * F_CR_UP,
            "control_region_down": P_PB * F_CR_DOWN,
            "pair_total_syst": F * P_SYST_PB,
        },
        "sigma_eff_partial_syst_source_effects_mb": {
            "up_from_control_region_down": eff_up_effects[0],
            "up_from_pair_nonbr_down": eff_up_effects[1],
            "up_from_single_bin_up": eff_up_effects[2],
            "up_from_atlas_lumi_up": eff_up_effects[3],
            "down_from_category_up": eff_down_effects[0],
            "down_from_control_region_up": eff_down_effects[1],
            "down_from_pair_nonbr_up": eff_down_effects[2],
            "down_from_single_bin_down": eff_down_effects[3],
            "down_from_atlas_lumi_down": eff_down_effects[4],
        },
    }
    return rows, details


def cross_checks():
    old_f = 0.192473188486
    old_f_stat = 0.0188290296535
    old_eff = sigma_eff(f=old_f)
    old_dps = sigma_dps(f=old_f)
    old_dps_stat = math.hypot(old_f * P_STAT_PB, P_PB * old_f_stat)
    old_eff_stat = old_eff * math.hypot(
        old_dps_stat / old_dps, 2.0 * X_STAT_NB / X_NB
    )
    cms_eff = 0.001 * 0.5 * X_NB**2 / (BR**2 * 12.6)
    return {
        "old_H006_E4": {
            "sigma_DPS_pb": old_dps,
            "sigma_eff_mb": old_eff,
            "sigma_eff_stat_mb": old_eff_stat,
            "reference_sigma_DPS_pb": 7.16000261168,
            "reference_sigma_eff_mb": 2.22067554009,
            "reference_sigma_eff_stat_mb": 0.22021401332,
        },
        "CMS_MC_template_nominal": {
            "input_sigma_DPS_pb": 12.6,
            "sigma_eff_mb": cms_eff,
            "reference_sigma_eff_mb": 1.26191,
        },
    }


def main():
    rows, details = build_results()
    with (HERE / "results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    with (HERE / "propagation_details.json").open("w", encoding="utf-8") as handle:
        json.dump(details, handle, indent=2, sort_keys=True)
        handle.write("\n")
    with (HERE / "cross_checks.json").open("w", encoding="utf-8") as handle:
        json.dump(cross_checks(), handle, indent=2, sort_keys=True)
        handle.write("\n")
    for row in rows:
        stat = (
            f"+/- {row['stat_up']:.12g} (stat) "
            if isinstance(row["stat_up"], float)
            else "stat unresolved "
        )
        print(
            f"{row['quantity']} {row['scenario']}: {row['central']:.12g} "
            f"{stat}+{row['partial_syst_up']:.12g}/-{row['partial_syst_down']:.12g} "
            f"(partial syst) {row['unit']}"
        )


if __name__ == "__main__":
    main()
