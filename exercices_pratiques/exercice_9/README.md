# Exercice 9 : Classification par K-plus proches voisins (K-NN)

## Objectif pédagogique

Implémenter l'algorithme de classification K-Nearest Neighbors et comprendre les principes de l'apprentissage par similarité dans les espaces métriques.

## Concepts mathématiques fondamentaux

### Algorithme K-NN

- **Classification par proximité** : Décision basée sur les $k$ exemples les plus similaires
- **Distance euclidienne** : $d(x, x') = \sqrt{\sum_{j=1}^d (x_j - x'_j)^2}$ dans $\mathbb{R}^d$
- **Vote majoritaire** : Classe prédite = argmax des classes parmi les k plus proches voisins

### Validation croisée

- **Séparation stratifiée** : Maintien des proportions de classes dans train/test
- **Évaluation des performances** : Mesure de l'exactitude sur données non vues
- **Prévention du surapprentissage** : Validation sur un ensemble indépendant

## Description technique

Cet exercice démontre le pipeline complet d'apprentissage supervisé :

1. **Préparation des données** : Constitution d'un dataset représentatif
2. **Partitionnement** : Séparation train/validation pour évaluation objective
3. **Entraînement** : Apprentissage des relations de similarité
4. **Inférence** : Classification de nouvelles instances

## Implémentation et analyse

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Dataset supervisé : caractéristiques géométriques → classes
X = np.array([
    [10, 10], [20, 20], [15, 10], [25, 15], [12, 12], [18, 14],
    [8, 8], [22, 18], [14, 12], [16, 16], [9, 7], [21, 19]
])
y = np.array([0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1])

# Partitionnement stratifié : 70% entraînement, 30% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Instanciation et entraînement du classifieur K-NN (k=3)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Inférence sur un nouvel exemple
nouvel_exemple = np.array([[6, 6]])
prediction = knn.predict(nouvel_exemple)

print(f"Prediction pour {nouvel_exemple[0]}: {'Carre' if prediction[0] == 0 else 'Rectangle'}")
print(f"Exactitude sur test: {knn.score(X_test, y_test):.3f}")
```

## Analyse mathématique

### Fonction de décision K-NN

Pour un point $x \in \mathbb{R}^d$ :

1. Calculer $d(x, x^{(i)})$ pour tous les exemples d'entraînement
2. Sélectionner les $k$ plus proches voisins $\mathcal{N}_k(x)$
3. Prédire $\hat{y} = \arg\max_{c} \sum_{i \in \mathcal{N}_k(x)} \mathbb{I}_{y^{(i)} = c}$

### Propriétés algorithmiques

- **Non-paramétrique** : Pas d'hypothèse sur la distribution des données
- **Lazy learning** : Pas d'entraînement explicite, stockage des données
- **Sensibilité locale** : Décisions basées sur similarité géométrique

### Complexité computationnelle

- **Entraînement** : $O(1)$ (stockage uniquement)
- **Prédiction** : $O(N \cdot d)$ où $N$ est la taille du dataset
- **Optimisation possible** : Structures de données spatiales (KD-tree, Ball-tree)

## Applications en apprentissage automatique

K-NN est particulièrement adapté pour :

- **Classification géométrique** : Problèmes où la similarité spatiale est pertinente
- **Systèmes de recommandation** : Similarité entre utilisateurs/objets
- **Détection d'anomalies** : Points isolés dans l'espace des caractéristiques
- **Apprentissage semi-supervisé** : Propagation d'étiquettes par similarité

## Exécution et validation

```bash
python solution.py
```

**Résultat attendu :**
Affichage de la prédiction pour un nouvel exemple et du score d'exactitude sur l'ensemble de test.

## Concepts transversaux abordés

- **Théorie des métriques** : Espaces mesurés et distances
- **Statistiques non-paramétriques** : Méthodes sans hypothèse distributionnelle
- **Validation empirique** : Évaluation objective des performances
  knn = KNeighborsClassifier(n_neighbors=3)
  knn.fit(X_train, y_train)

# Prédiction sur une nouvelle forme

nouvelle_forme = np.array([[6, 6]])
prediction = knn.predict(nouvelle_forme)

print(f"Prediction pour [6, 6]: {'Carre' if prediction[0] == 0 else 'Rectangle'}")
print(f"Score sur l'ensemble de test: {knn.score(X_test, y_test):.2f}")

````

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
````

## Résultat attendu

Affiche la prédiction pour une nouvelle forme et le score de précision sur l'ensemble de test.
