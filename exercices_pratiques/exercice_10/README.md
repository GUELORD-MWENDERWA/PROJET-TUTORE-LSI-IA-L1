# Exercice 10 : Classification d'objets par analyse de pixels

## Objectif

Implémenter une classification simple basée sur l'analyse des caractéristiques d'image.

## Concepts fondamentaux

- **Caractéristiques d'image** : Propriétés extraites des pixels (somme, moyenne, etc.)
- **Classification par seuillage** : Décision basée sur un critère numérique fixe
- **Analyse morphologique** : Étude de la forme et de la structure des objets

## Description détaillée

Cet exercice démontre :

1. La création d'une image binaire représentant une forme géométrique
2. L'extraction d'une caractéristique simple (somme des pixels)
3. La classification basée sur un seuil prédéfini

## Code et explication

```python
import numpy as np

# Création d'une image binaire représentant un carré
image = np.zeros((5, 5), dtype=np.uint8)
image[1:4, 1:4] = 1  # Carré 3x3 au centre

# Calcul de la caractéristique : nombre total de pixels blancs
somme_pixels = np.sum(image)

# Classification basée sur un seuil
seuil = 8  # Seuil pour considérer la forme comme "grande"
est_grand_carre = somme_pixels > seuil

print("Image binaire:")
print(image)
print(f"\nSomme des pixels: {somme_pixels}")
print(f"Seuil: {seuil}")
print(f"Classification: {'Grand carre' if est_grand_carre else 'Petit carre'}")
```

## Notions importantes

- **Image binaire** : Chaque pixel vaut 0 (noir) ou 1 (blanc)
- **np.sum()** : Addition de tous les éléments du tableau
- **Classification par seuil** : Décision binaire basée sur une valeur limite
- **Caractéristique simple** : La somme des pixels comme mesure de taille

## Applications pratiques

Cette approche simplifiée est utilisée pour :

- Les systèmes de vision industrielle basiques
- Le prétraitement avant des algorithmes plus complexes
- La détection de formes simples
- Les applications embarquées avec ressources limitées

## Exécution

```bash
python solution.py
```

## Résultat attendu

Affiche l'image binaire, la somme des pixels et la classification résultante.
