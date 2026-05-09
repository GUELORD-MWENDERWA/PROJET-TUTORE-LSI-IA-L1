# Exercice 1 : Manipulation de pixels avec NumPy

## Objectif

Comprendre comment représenter et manipuler des images sous forme de tableaux numériques en utilisant NumPy.

## Concepts fondamentaux

- **Image numérique** : Une image est un tableau 2D où chaque élément représente l'intensité d'un pixel
- **Pixel** : Plus petit élément d'une image, contenant une valeur numérique (0-255 pour les images 8 bits)
- **Tableau NumPy** : Structure de données optimisée pour les calculs mathématiques sur des tableaux

## Description détaillée

Cet exercice montre comment :

1. Créer un tableau NumPy représentant une image noire (tous les pixels à 0)
2. Modifier individuellement un pixel spécifique
3. Afficher les résultats avant et après modification

## Code et explication

```python
import numpy as np

# Création d'une image 3x3 noire
image_simple = np.zeros((3, 3), dtype=np.uint8)

# Modification du pixel central (ligne 1, colonne 1)
image_simple[1, 1] = 255  # Blanc = 255

print("Image initiale (3x3) :")
print(np.zeros((3, 3), dtype=np.uint8))
print("\nImage après modification du pixel central à 255 :")
print(image_simple)
```

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
```

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
