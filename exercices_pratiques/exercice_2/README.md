# Exercice 2 : Redimensionnement simulé d'une image

## Objectif

Maîtriser l'extraction de régions d'intérêt dans un tableau NumPy pour simuler le redimensionnement d'images.

## Concepts fondamentaux

- **Slicing NumPy** : Technique pour extraire des sous-parties de tableaux multidimensionnels
- **Redimensionnement** : Processus de modification des dimensions d'une image
- **Crop central** : Extraction de la zone centrale d'une image

## Description détaillée

Cet exercice démontre :

1. La génération d'une matrice 10x10 avec des valeurs aléatoires
2. L'extraction d'une sous-matrice 5x5 centrée
3. L'affichage comparatif des deux matrices

## Code et explication

```python
import numpy as np

# Génération d'une image 10x10 aléatoire
grande_image = np.random.randint(8, 256, size=(10, 10))

# Extraction de la sous-image centrale 5x5
# Centre d'une matrice 10x10 : indices 2 à 7 (2:7)
sous_image = grande_image[2:7, 2:7]

print("Grande image (10×10): ")
print(grande_image)
print("\nSous-image centrale (5x5):")
print(sous_image)
```

## Notions importantes

- **Syntaxe du slicing** : `array[début:fin, début:fin]`
- **Calcul du centre** : Pour une taille N, le centre commence à `(N-crop_size)//2`
- **Redimensionnement simplifié** : Cette méthode ne fait qu'un crop, pas un vrai redimensionnement

## Applications pratiques

Cette technique est utilisée pour :

- Le prétraitement d'images avant analyse
- L'extraction de régions d'intérêt (ROI)
- La normalisation des tailles d'images pour l'entraînement de modèles

## Exécution

```bash
python solution.py
```

## Résultat attendu

Affiche une matrice 10x10 aléatoire puis sa sous-matrice centrale 5x5.
