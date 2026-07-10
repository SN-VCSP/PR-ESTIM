# Estimation EGPF — ApplicationSN

Application Streamlit d'estimation de surfaces et de quantités de matériaux pour les travaux de chaussées (EGPF / DIRMED / VINCI Construction).

## Prérequis

- Python 3.10 ou supérieur
- pip

## Installation

```bash
pip install streamlit folium streamlit-folium pyproj pandas numpy openpyxl Pillow
```

## Lancement

```bash
streamlit run ApplicationSN.py
```

L'application s'ouvre dans le navigateur à l'adresse `http://localhost:8501`.

## Format du fichier CSV attendu

Séparateur `;`, décimale `,` (format français).

| Colonne | Obligatoire | Description |
|---------|-------------|-------------|
| `route` | ✅ | Identifiant de la route (ex. `A0007`) |
| `cote` | ✅ | Côté : `D` ou `G` |
| `pr` | ✅ | Point de repère (numérique) |
| `x` | ✅ | Coordonnée X Lambert-93 |
| `y` | ✅ | Coordonnée Y Lambert-93 |
| `cumul` | ➕ | Chaînage cumulé en mètres (mappé automatiquement en `chainage_m`) |
| `Gestionnaire` | ➕ | Gestionnaire de la voirie |
| `depPr` | ➕ | Numéro de département |
| `Fait` | ➕ | Oui/Non — auscultation réalisée |
| `Ausculte` | ➕ | Oui/Non — auscultation effectuée |
| `structure` | ➕ | Description de la structure de chaussée |
| `A_refaire` | ➕ | Oui/Non — tronçon à refaire |
| `V_L`, `V_M`, `V_R` | ➕ | Structures conseillées (données labo) |

## Fonctionnalités principales

- **Carte IGN interactive** — Fond IGN Géoportail, Esri Satellite ou OSM ; points PR colorés par statut Fait/Ausculté
- **Sélection de tronçon** — Filtrage par gestionnaire, département, route ; curseur PR début/fin
- **Profils de chaussée** — 7 profils prédéfinis (2, 3, 4 voies, accès…) + création de profils personnalisés
- **Dessin de segments** — Polylignes sur la carte pour mesurer une distance réelle
- **Calcul de surfaces** — Par élément (BAU, BDG, VL, VR, VM, VS, BRET, Accès…) avec largeurs paramétrables
- **Sous-segments** — Plusieurs tronçons avec profils différents sur un même axe
- **Rabotage** — Multi-passes, multi-hauteurs, totaux par élément et par hauteur
- **Reprofilage** — Multi-matériaux (GB, BBTM, BBSG…), volumes et tonnages
- **Surfaces dessinées** — Polygones sur la carte, rabotage + reprofilage par surface
- **Estimation de coût** — Tonnage × prix unitaire (€/t) depuis la bibliothèque de matériaux
- **Export Excel** — Rapport 5 onglets avec charte VINCI Construction (bleu #004489)
- **Sauvegarde de projet** — Export/import JSON pour reprendre le travail

## Structure du projet

```
ApplicationSN.py          Application principale Streamlit
DIRMED_EUROVIA_13-JP.csv  Données PR avec informations labo
PR_FRANCE_SN.csv          Données PR sans informations labo
test_logique_metier.py    Tests unitaires de la logique de calcul
mon_logo1.png             Logo (optionnel)
```

## Tests

```bash
python test_logique_metier.py
```
