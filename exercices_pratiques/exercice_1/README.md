# Exercice 1 : Représentation matricielle d'images avec NumPy

## Objectif pédagogique

Maîtriser la représentation mathématique des images sous forme de matrices et comprendre les opérations élémentaires de manipulation de pixels dans le contexte de l'algèbre linéaire appliquée au traitement d'images.

## Concepts mathématiques fondamentaux

### Image comme matrice

- **Matrice d'intensité** : Une image numérique est représentée par une matrice $I \in \mathbb{R}^{m \times n}$ où chaque élément $I_{ij}$ correspond à l'intensité du pixel $(i,j)$
- **Espace discret** : Les indices matriciels correspondent aux coordonnées spatiales $(x,y)$ dans l'image
- **Codage numérique** : Valeurs entières sur 8 bits $[0, 255]$ pour les images en niveaux de gris

### Opérations matricielles élémentaires

- **Accès direct** : $I[i,j]$ pour modification ponctuelle d'un pixel
- **Types de données** : Utilisation de `np.uint8` pour optimisation mémoire et calculs

## Description technique

Cet exercice démontre l'implémentation pratique des concepts suivants :

1. **Initialisation matricielle** : Création d'une matrice nulle représentant une image noire
2. **Modification élémentaire** : Changement de valeur d'un pixel spécifique
3. **Visualisation des résultats** : Affichage des matrices avant/après transformation

## Implémentation et analyse

```python
import numpy as np

# Création d'une matrice 3x3 initialisée à zéro (image noire)
image_simple = np.zeros((3, 3), dtype=np.uint8)

# Modification du pixel central - opération d'indexation matricielle
image_simple[1, 1] = 255  # Attribution de la valeur maximale (blanc)

print("Image originale (matrice nulle):")
print(image_simple)
print("\nImage après modification:")
print(image_simple)
```

## Analyse mathématique

### Représentation formelle

- **Avant modification** : $I = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$
- **Après modification** : $I = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 255 & 0 \\ 0 & 0 & 0 \end{pmatrix}$

### Propriétés de l'opération

- **Localité** : Modification isolée d'un élément sans affecter les autres
- **Précision** : Contrôle direct de l'intensité lumineuse par valeur numérique
- **Efficacité** : Accès $O(1)$ aux éléments matriciels

## Applications en IA

Cette opération élémentaire constitue la base de nombreux algorithmes de vision par ordinateur :

- **Segmentation d'images** : Marquage de régions d'intérêt
- **Filtrage spatial** : Modification sélective de pixels selon des critères
- **Préparation de données** : Normalisation et correction d'images d'entraînement

## Exécution et validation

```bash
python solution.py
```

**Sortie attendue :**

```
Image originale (matrice nulle):
[[0 0 0]
 [0 0 0]
 [0 0 0]]

Image après modification:
[[0 0 0]
 [0 255 0]
 [0 0 0]]
```

## Concepts transversaux abordés

- **Algèbre linéaire** : Manipulation de matrices comme objets mathématiques
- **Représentation discrète** : Discrétisation de l'espace continu des images
- **Optimisation computationnelle** : Choix des types de données pour l'efficacité

print("Image initiale (3x3) :")
print(np.zeros((3, 3), dtype=np.uint8))
print("\nImage après modification du pixel central à 255 :")
print(image_simple)

````

## Notions importantes

- **Indices NumPy** : Commencent à 0, donc `image[1, 1]` accède au pixel central d'une matrice 3x3
- **dtype=np.uint8** : Type de données pour les images 8 bits (0-255)
- **np.zeros()** : Crée un tableau rempli de zéros

## Applications pratiques

Cette manipulation de base est essentielle pour :

- Le traitement d'images
- La génération de masques binaires
- Les opérations de filtrage pixel par pixel

## Exécution

```bash
python solution.py
````

## Résultat attendu

```
Image initiale (3x3) :
[[0 0 0]
 [0 0 0]
 [0 0 0]]

Image après modification du pixel central à 255 :
[[  0   0   0]
 [  0 255   0]
 [  0   0   0]]
```
