# Exercice 8 : Préparation de données pour l'apprentissage automatique

## Objectif

Comprendre la structuration des données pour l'entraînement de modèles de machine learning.

## Concepts fondamentaux

- **Jeu de données supervisé** : Ensemble de paires (caractéristiques, étiquette)
- **Caractéristiques (features)** : Variables d'entrée décrivant les exemples
- **Étiquettes (labels)** : Valeurs cibles à prédire
- **Format matriciel** : Organisation des données en tableaux NumPy

## Description détaillée

Cet exercice illustre :

1. La création d'un jeu de données simple avec caractéristiques géométriques
2. L'organisation des données en matrices X (caractéristiques) et y (étiquettes)
3. La classification binaire (carré vs rectangle)

## Code et explication

```python
import numpy as np

# Création du jeu de données
# X : caractéristiques (largeur, hauteur)
# y : étiquettes (0 = carré, 1 = rectangle)

X = np.array([
    [10, 10],  # Carré
    [20, 20],  # Carré
    [15, 10],  # Rectangle
    [25, 15],  # Rectangle
    [12, 12],  # Carré
    [18, 14]   # Rectangle
])

y = np.array([0, 0, 1, 1, 0, 1])  # Étiquettes correspondantes

print("Caracteristiques (X):")
print(X)
print("\nEtiquettes (y):")
print(y)
print(f"\nDimensions: X {X.shape}, y {y.shape}")
```

## Notions importantes

- **Matrice X** : Chaque ligne représente un exemple, chaque colonne une caractéristique
- **Vecteur y** : Une étiquette par exemple (même nombre de lignes que X)
- **Classification binaire** : Étiquettes 0/1 pour deux classes
- **Format NumPy** : Arrays multidimensionnels optimisés pour les calculs

## Applications pratiques

Cette structure est utilisée pour :

- L'entraînement de tous les algorithmes supervisés
- La validation croisée des modèles
- L'évaluation des performances
- Le prétraitement des données réelles

## Exécution

```bash
python solution.py
```

## Résultat attendu

Affiche les matrices X et y avec leurs dimensions, montrant la structure des données d'entraînement.
