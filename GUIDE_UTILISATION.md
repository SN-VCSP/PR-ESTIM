# Guide d'utilisation — Estimation EGPF

## Démarrage rapide

Lancez l'application :
```bash
streamlit run ApplicationSN.py
```

---

## Étape 1 · Importer un fichier PR

1. Cliquez sur **"Browse files"** en haut de la page.
2. Sélectionnez votre fichier CSV ou Excel (colonnes obligatoires : `route`, `cote`, `pr`, `x`, `y`).
3. Un message vert confirme le chargement (ex. `✅ PR chargés : 312 lignes, 5 route(s)…`).

> **Astuce** : Si votre CSV contient une colonne `cumul`, elle est automatiquement reconnue comme chaînage.

---

## Étape 2 · Choisir le tronçon (panneau gauche)

Dans le panneau **Filtres** à gauche :

1. Filtrez par **Gestionnaire** et/ou **Département** (optionnel).
2. Filtrez par **Route(s)** si nécessaire.
3. Dans **Sélection du segment** :
   - Choisissez la **Route** et le **Côté** (`D` ou `G`).
   - Déplacez les deux curseurs pour choisir le **PR début → PR fin**.

---

## Étape 3 · Régler les options

Utilisez les 4 boutons en haut de la page pour ouvrir les panneaux de réglage :

### 3a · Distance & courbure
- **Méthode** : `Segment édité` (recommandé pour dessiner), `Chainage`, `Droite PR→PR`, `Fixe`.
- **Facteur de courbure** : multiplie la distance pour tenir compte des virages (1.00 = sans correction).

### 3b · Filtrage & légende
- Filtrez les points PR par combinaison Fait/Ausculté.
- Activez le **clustering** pour les gros fichiers (> 5 000 points).

### 3d · Profils & éléments *(le plus important)*
1. Choisissez le **profil** de la chaussée (`2_voies`, `3_voies`, `Accès`…).
2. Sélectionnez le **préréglage d'inclusion** (`Tout` inclut BAU, BDG, voies…).
3. Ajustez les **largeurs par élément** si nécessaire (valeurs par défaut prédéfinies).
4. Pour créer un profil personnalisé, utilisez le bloc **Créer / Modifier un profil**.

---

## Étape 4 · Dessiner et ajouter des sous-segments

1. Cliquez sur l'outil **Polyligne** (icône crayon en haut à gauche de la carte).
2. Cliquez sur la carte pour tracer le segment, puis **double-cliquez** pour terminer.
3. Dans la colonne de droite, choisissez le **profil** dans la liste.
4. Cliquez **➕ Ajouter comme sous-segment**.
5. Répétez pour chaque tronçon avec un profil différent.

> **Réinitialiser** : bouton "Réinitialiser le tracé édité" pour effacer le dessin temporaire.

---

## Étape 5 · Lancer les calculs

Cliquez sur **🚀 Lancer les calculs**.

Les résultats apparaissent en dessous :
- **Distance totale** (en mètres)
- **Surface totale** (en m²)
- Tableau détaillé par élément et par sous-segment

---

## Étape 6 · Rabotage

Onglet **Rabotage** :

1. Choisissez la base : **Toute la voirie** ou **Par élément**.
2. Pour chaque élément, saisissez la **hauteur de rabotage (cm)** de la passe.
3. Cliquez **+ Ajouter une passe** pour les profils multicouches.
4. Les volumes (m³) sont calculés automatiquement.
5. Téléchargez les résultats en CSV.

---

## Étape 7 · Reprofilage

Onglet **Reprofilage** :

1. Vérifiez/modifiez la **bibliothèque de matériaux** (densités t/m³, prix €/t).
2. Choisissez la base et sélectionnez les matériaux pour chaque élément.
3. Saisissez les **épaisseurs (cm)** pour chaque couche.
4. Les tonnages (t) sont calculés automatiquement.

---

## Étape 8 · Surfaces dessinées (optionnel)

Pour une zone délimitée (giratoire, aire de service…) :

1. Tracez un **polygone** sur la carte (outil rectangle ou polygone).
2. Dans la colonne de droite, nommez la surface et cliquez **➕ Ajouter comme surface**.
3. Dans l'onglet **Surface**, saisissez la hauteur de rabotage et les matériaux.

---

## Étape 9 · Exporter

- **📊 Rapport Excel (5 onglets)** : cliquez le bouton en bas de page — contient Surface général, Rabotage, Reprofilage, Surface, Coût.
- **CSV par section** : disponible dans chaque onglet.
- **💾 Sauvegarder le projet** : export JSON pour reprendre plus tard.

---

## Utiliser les popups PR sur la carte

Cliquez sur un point PR (rond coloré) pour afficher :
- **Page 1** : Structure de chaussée, statuts Fait/Ausculté/À refaire, lien Google Maps.
- **Page 2** (bouton ➡) : Structures conseillées V_L, V_M, V_R (données labo si disponibles).

**Code couleur des points PR :**

| Couleur | Signification |
|---------|--------------|
| Remplissage bleu, bordure grise | Fait = Non, Ausculté = Oui (données labo disponibles) |
| Remplissage blanc, bordure grise | Fait = Non, Ausculté = Non |
| Remplissage doré, bordure verte | Fait = Oui |
| Anneau rouge | À refaire = Oui |
