# Exercice 9 : Entraînement d'un classifieur K-Nearest Neighbors

## Objectif

Implémenter et entraîner un modèle de classification par plus proches voisins.

## Concepts fondamentaux

- **Apprentissage supervisé** : Algorithme qui apprend à partir d'exemples étiquetés
- **K-Nearest Neighbors (K-NN)** : Classification basée sur la similarité avec les voisins
- **Validation croisée** : Séparation entraînement/test pour évaluer les performances
- **Distance euclidienne** : Mesure de similarité entre points dans l'espace des caractéristiques

## Description détaillée

Cet exercice couvre :

1. La préparation d'un jeu de données géométriques
2. La séparation en ensembles d'entraînement et de test
3. L'entraînement d'un modèle K-NN
4. La prédiction sur de nouvelles données

## Code et explication

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Jeu de données : [largeur, hauteur] -> classe (0=carré, 1=rectangle)
X = np.array([
    [10, 10], [20, 20], [15, 10], [25, 15], [12, 12], [18, 14],
    [8, 8], [22, 18], [14, 12], [16, 16], [9, 7], [21, 19]
])
y = np.array([0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1])

# Séparation entraînement/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entraînement du modèle K-NN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Prédiction sur une nouvelle forme
nouvelle_forme = np.array([[6, 6]])
prediction = knn.predict(nouvelle_forme)

print(f"Prediction pour [6, 6]: {'Carre' if prediction[0] == 0 else 'Rectangle'}")
print(f"Score sur l'ensemble de test: {knn.score(X_test, y_test):.2f}")
```

## Notions importantes

- **Paramètre k** : Nombre de voisins considérés (ici k=3)
- **Distance par défaut** : Euclidienne pour les caractéristiques numériques
- **train_test_split** : Division aléatoire préservant la distribution des classes
- **Score de précision** : Proportion de prédictions correctes

## Applications pratiques

K-NN est utilisé pour :

- La classification d'images simples
- Les systèmes de recommandation
- La reconnaissance de formes géométriques
- Les problèmes où la similarité locale est importante

## Exécution

```bash
python solution.py
```

## Résultat attendu

Affiche la prédiction pour une nouvelle forme et le score de précision sur l'ensemble de test.
