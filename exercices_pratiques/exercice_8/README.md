# Exercice 8 : Structuration de données pour apprentissage supervisé

## Objectif pédagogique

Maîtriser la préparation et l'organisation de jeux de données pour l'apprentissage automatique supervisé, en appliquant les concepts d'espaces de caractéristiques et de codage des classes.

## Concepts mathématiques fondamentaux

### Apprentissage supervisé

- **Espace d'entrée** : $\mathcal{X} \subseteq \mathbb{R}^d$ (espace des caractéristiques)
- **Espace de sortie** : $\mathcal{Y} = \{0,1,\dots,k-1\}$ (classes pour classification)
- **Jeu d'entraînement** : Ensemble $\{(x^{(i)}, y^{(i)})\}_{i=1}^N$ de $N$ exemples étiquetés

### Représentation matricielle

- **Matrice des caractéristiques** : $X \in \mathbb{R}^{N \times d}$ avec $X_{ij} = j$-ème coordonnée de l'exemple $i$
- **Vecteur des étiquettes** : $y \in \mathbb{R}^N$ avec $y_i \in \mathcal{Y}$
- **Encodage one-hot** : Extension possible à $Y \in \{0,1\}^{N \times k}$ pour classification multi-classes

## Description technique

Cet exercice implémente la structuration complète d'un dataset supervisé :

1. **Définition des caractéristiques** : Sélection de descripteurs géométriques pertinents
2. **Codage des classes** : Attribution d'étiquettes numériques aux catégories
3. **Organisation matricielle** : Format standard pour les bibliothèques d'IA

## Implémentation et analyse

```python
import numpy as np

# Construction du jeu de données supervisé
# Caractéristiques : dimensions géométriques (largeur, hauteur)
# Classes : 0 = carré (largeur = hauteur), 1 = rectangle (largeur ≠ hauteur)

X = np.array([
    [10, 10],  # Exemple 1 : carré
    [20, 20],  # Exemple 2 : carré
    [15, 10],  # Exemple 3 : rectangle
    [25, 15],  # Exemple 4 : rectangle
    [12, 12],  # Exemple 5 : carré
    [18, 14]   # Exemple 6 : rectangle
])

# Vecteur des étiquettes : codage numérique des classes
y = np.array([0, 0, 1, 1, 0, 1])

print("Matrice des caracteristiques X:")
print(X)
print(f"\nDimensions de X: {X.shape}")
print(f"\nVecteur des etiquettes y:")
print(y)
print(f"\nDimensions de y: {y.shape}")
```

## Analyse mathématique

### Géométrie des données

- **Dimensionnalité** : $d = 2$ (largeur, hauteur)
- **Cardinalité** : $N = 6$ exemples d'entraînement
- **Classes équilibrées** : 3 carrés, 3 rectangles

### Propriétés statistiques

- **Séparabilité linéaire** : Les classes sont séparables par la droite $largeur = hauteur$
- **Variance intra-classe** : Variation des dimensions au sein de chaque classe
- **Robustesse** : Résistance aux variations d'échelle

### Représentation formelle

$\mathcal{D} = \{(x^{(i)}, y^{(i)})\}_{i=1}^6$ où :

- $x^{(i)} = (l_i, h_i) \in \mathbb{R}^2$
- $y^{(i)} = \mathbb{I}_{l_i \neq h_i} \in \{0,1\}$

## Applications en apprentissage automatique

Cette structuration est la base de tous les algorithmes supervisés :

- **Classification** : Prédiction de classes à partir de caractéristiques
- **Régression** : Prédiction de valeurs continues
- **Validation croisée** : Évaluation des performances sur données non vues
- **Generalisation** : Capacité du modèle à traiter de nouveaux exemples

## Exécution et validation

```bash
python solution.py
```

**Sortie attendue :**
Affichage de la matrice X (6×2) et du vecteur y (6×1) avec leurs dimensions.

## Concepts transversaux abordés

- **Algèbre linéaire** : Manipulation de matrices et vecteurs
- **Théorie des ensembles** : Définition d'espaces et de fonctions caractéristiques
- **Statistiques** : Analyse descriptive des distributions de données

print("Caracteristiques (X):")
print(X)
print("\nEtiquettes (y):")
print(y)
print(f"\nDimensions: X {X.shape}, y {y.shape}")

````

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
````

## Résultat attendu

Affiche les matrices X et y avec leurs dimensions, montrant la structure des données d'entraînement.
