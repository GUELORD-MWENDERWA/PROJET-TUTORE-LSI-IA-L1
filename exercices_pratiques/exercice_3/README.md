# Exercice 3 : Détection de couleur simple (seuillage)

## Objectif

Comprendre et implémenter le seuillage binaire pour la segmentation d'images.

## Concepts fondamentaux

- **Seuillage (Thresholding)** : Technique de segmentation qui convertit une image en niveaux de gris en image binaire
- **Image binaire** : Image ne contenant que deux valeurs (0 et 1, ou noir et blanc)
- **Segmentation** : Processus de séparation d'une image en régions distinctes

## Description détaillée

Cet exercice illustre :

1. La génération d'une matrice 5x5 avec des valeurs aléatoires (0-255)
2. L'application d'un seuil fixe (127) pour binariser l'image
3. La conversion des valeurs booléennes en entiers

## Code et explication

```python
import numpy as np

# Création d'une image 5x5 avec valeurs aléatoires
image_couleur_simulee = np.random.randint(0, 256, size=(5, 5))

# Seuillage : pixels > 127 deviennent 1, autres deviennent 0
image_binaire = (image_couleur_simulee > 127).astype(np.uint8)

print("Image simulée originale:")
print(image_couleur_simulee)
print("\nImage binaire (seuillage):")
print(image_binaire)
```

## Notions importantes

- **Comparaison vectorielle** : `image > seuil` retourne un tableau de booléens
- **Conversion de type** : `.astype(np.uint8)` transforme True/False en 1/0
- **Choix du seuil** : 127 est la moyenne entre 0 et 255, mais peut être ajusté selon les besoins

## Applications pratiques

Le seuillage est utilisé pour :

- La détection de contours
- La séparation avant/arrière-plan
- La préparation d'images pour l'analyse morphologique
- Les systèmes de vision industrielle

## Exécution

```bash
python solution.py
```

## Résultat attendu

Affiche une matrice 5x5 aléatoire puis sa version binarisée avec le seuil 127.
