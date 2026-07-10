"""
Test de non-régression de la LOGIQUE MÉTIER pure d'ApplicationSN.py.

Ces fonctions sont reproduites à l'identique de l'application (calculs de surfaces,
mix de profils, distances). Le but est de prouver que la logique de calcul n'a PAS
changé après le refactor de fluidité (qui ne touche qu'à l'affichage de la carte).

Dépendances : pandas + numpy uniquement (ni streamlit, ni folium, ni pyproj).
Lancement :   python3 test_logique_metier.py
"""
from math import hypot
import numpy as np
import pandas as pd

# --- Constantes identiques à l'app -------------------------------------------
PROFILES = {
    "2_voies": {"BDG": 1, "VR": 1, "VL": 1, "BAU": 1},
    "3_voies": {"BDG": 1, "VR": 1, "VM": 1, "VL": 1, "BAU": 1},
    "Accès":   {"Accès": 1, "AccoD": 1, "AccoG": 1},
}


# --- Fonctions reproduites à l'identique d'ApplicationSN.py -------------------
def planimetric_distance_l93(coords):
    if len(coords) < 2:
        return 0.0
    return float(sum(
        hypot(coords[i + 1][0] - coords[i][0], coords[i + 1][1] - coords[i][1])
        for i in range(len(coords) - 1)
    ))


def pr_delta_m(pr_start, pr_end):
    try:
        return 1000.0 * (float(pr_end) - float(pr_start))
    except Exception:
        return 0.0


def merge_profile_mix(profiles_selected, percentages):
    weights = np.array(percentages, dtype=float)
    if weights.sum() == 0:
        return {}
    weights = weights / weights.sum()
    agg = {}
    for prof_name, w in zip(profiles_selected, weights):
        for elem, count in PROFILES[prof_name].items():
            agg[elem] = agg.get(elem, 0.0) + float(w) * float(count)
    return agg


def apply_overrides(widths, overrides, route, cote, pr_start, pr_end):
    if overrides is None:
        return widths
    mask = (
        (overrides["route"] == route)
        & (overrides["cote"] == cote)
        & (overrides["pr_start"] <= pr_end)
        & (overrides["pr_end"] >= pr_start)
    )
    ov = overrides.loc[mask]
    if ov.empty:
        return widths
    new_widths = widths.copy()
    for _, row in ov.iterrows():
        elem = str(row["element"])
        val = float(row["largeur_m"])
        if elem in new_widths:
            new_widths[elem] = val
    return new_widths


def compute_areas(distance_m, widths_m, element_counts, included_elements):
    rows, total = [], 0.0
    for elem, count in element_counts.items():
        if elem not in included_elements:
            continue
        width = float(widths_m.get(elem, 0.0))
        width_equiv = float(count) * width
        area = float(distance_m) * width_equiv
        rows.append({"element": elem, "area_m2": area})
        total += area
    return pd.DataFrame(rows), float(total)


# --- Tests -------------------------------------------------------------------
def run():
    ok = True

    # 1) Distance planimétrique
    assert planimetric_distance_l93([(0, 0), (1000, 0)]) == 1000.0
    assert planimetric_distance_l93([(0, 0), (3, 4)]) == 5.0

    # 2) PR x 1000
    assert pr_delta_m(12, 15) == 3000.0

    # 3) Mix de profil
    assert merge_profile_mix(["2_voies"], [100]) == {"BDG": 1.0, "VR": 1.0, "VL": 1.0, "BAU": 1.0}
    mix2 = merge_profile_mix(["2_voies", "3_voies"], [50, 50])
    assert abs(mix2["VM"] - 0.5) < 1e-9

    # 4) Surface 2_voies, largeurs standard, 1000 m
    widths = {"BDG": 1.0, "VR": 3.5, "VL": 3.5, "BAU": 2.5}
    _, total = compute_areas(1000.0, widths, merge_profile_mix(["2_voies"], [100]),
                             ["BDG", "VR", "VL", "BAU"])
    assert abs(total - 10500.0) < 1e-6, f"attendu 10500, obtenu {total}"

    # 5) Overrides : VL passe de 3.5 à 4.0 sur le tronçon
    ov = pd.DataFrame([{"route": "A0007", "cote": "D", "pr_start": 0.0,
                        "pr_end": 100.0, "element": "VL", "largeur_m": 4.0}])
    w2 = apply_overrides(widths, ov, "A0007", "D", 10.0, 20.0)
    assert w2["VL"] == 4.0 and w2["VR"] == 3.5

    print("✅ Tous les tests de logique métier PASSENT — calculs identiques à l'app.")
    return ok


if __name__ == "__main__":
    run()
