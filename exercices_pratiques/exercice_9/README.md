# Exercice 9 : Entraînement d'un classifieur simple K-NN

## Objectif

Cet exercice montre comment entraîner un modèle K-Nearest Neighbors (K-NN) avec Scikit-learn.

## Ce que fait ce script

- Il prépare un jeu de données de largeur/hauteur pour des objets.
- Il sépare les données en ensembles d'entraînement et de test.
- Il entraîne un classifieur K-NN.
- Il effectue une prédiction sur une nouvelle forme.

## Structure du code

- `create_dataset()` : crée les données et les labels.
- `train_knn_classifier(X, y, n_neighbors=3)` : divise les données et entraîne le modèle.
- `main()` : exécute l'entraînement et affiche la prédiction.

## Comment exécuter

```bash
python solution.py
```

## Explication pour débutants

- `train_test_split()` sépare les données pour tester si le modèle apprend bien.
- `KNeighborsClassifier(n_neighbors=3)` classe un objet en regardant ses 3 voisins les plus proches.
- `model.predict([[6, 6]])` donne la classe d'une nouvelle forme.

## Remarques

- `0` signifie "carré" et `1` signifie "rectangle".
- Ce script montre le flux complet : données -> entraînement -> prédiction.
