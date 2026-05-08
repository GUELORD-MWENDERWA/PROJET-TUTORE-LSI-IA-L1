# Exercice 8 : Préparation de données pour un modèle simple

## Objectif

Cet exercice présente comment organiser des données pour un modèle de machine learning.

## Ce que fait ce script

- Il crée une liste de caractéristiques (`X`) contenant la largeur et la hauteur de formes.
- Il crée une liste de labels (`y`) indiquant si l'objet est un carré (`0`) ou un rectangle (`1`).
- Il affiche les deux listes.

## Structure du code

- `create_feature_dataset()` : prépare les données de base.
- `main()` : affiche les caractéristiques et les labels.

## Comment exécuter

```bash
python solution.py
```

## Explication pour débutants

- `X` contient les exemples d'entrée : ici, chaque ligne est `[largeur, hauteur]`.
- `y` contient la sortie attendue : la classe de chaque exemple.
- Les modèles de machine learning apprennent à partir de ces données.

## Pourquoi c'est utile

- Avant d'entraîner un modèle, il faut toujours préparer les données sous forme de tableaux.
- Cette structure `X` et `y` est la base de presque tous les modèles scikit-learn.
