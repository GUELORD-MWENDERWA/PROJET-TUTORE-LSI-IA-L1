# Exercice 2 : Extraction de sous-matrices et redimensionnement matriciel

## Objectif pédagogique

Comprendre les opérations de slicing sur les matrices multidimensionnelles et leur application au redimensionnement d'images dans le cadre de l'algèbre linéaire appliquée au traitement d'images.

## Concepts mathématiques fondamentaux

### Slicing matriciel

- **Sous-matrice** : Extraction d'une région rectangulaire $A[i_1:i_2, j_1:j_2]$ d'une matrice $A \in \mathbb{R}^{m \times n}$
- **Coordonnées discrètes** : Indices entiers pour définir les bornes d'extraction
- **Conservation de la structure** : La sous-matrice préserve les propriétés matricielles

### Redimensionnement par cropping

- **Crop centré** : Extraction de la région centrale pour réduire les dimensions
- **Calcul des indices** : Détermination automatique des coordonnées du centre
- **Aspect ratio** : Maintien des proportions lors du redimensionnement

## Description technique

Cet exercice illustre l'application pratique des opérations matricielles suivantes :

1. **Génération de données** : Création d'une matrice aléatoire simulant une image
2. **Calcul géométrique** : Détermination des indices pour l'extraction centrée
3. **Extraction matricielle** : Application du slicing pour obtenir la sous-matrice

## Implémentation et analyse

```python
import numpy as np

# Génération d'une matrice 10×10 avec distribution uniforme discrète
# Valeurs dans [8, 255] pour simuler des intensités d'image réalistes
grande_image = np.random.randint(8, 256, size=(10, 10))

# Calcul des indices pour extraction centrée d'une sous-matrice 5×5
# Centre d'une matrice N×N : indices de (N-crop_size)//2 à (N-crop_size)//2 + crop_size
debut = (10 - 5) // 2  # (10-5)//2 = 2
fin = debut + 5        # 2 + 5 = 7

sous_image = grande_image[debut:fin, debut:fin]

print("Matrice originale (10×10):")
print(grande_image)
print(f"\nSous-matrice extraite (indices [{debut}:{fin}, {debut}:{fin}]):")
print(sous_image)
```

## Analyse mathématique

### Géométrie de l'extraction

Pour une matrice $A \in \mathbb{R}^{N \times N}$ et une taille de crop $C$ :

- **Indice de départ** : $start = \frac{N - C}{2}$
- **Indice de fin** : $end = start + C$
- **Sous-matrice** : $B = A[start:end, start:end] \in \mathbb{R}^{C \times C}$

### Propriétés préservées

- **Structure matricielle** : La sous-matrice reste une matrice valide
- **Continuité spatiale** : Connexité des pixels dans l'image originale
- **Distribution statistique** : Conservation partielle des caractéristiques locales

## Applications en IA et vision par ordinateur

Cette opération fondamentale est utilisée dans de nombreux contextes :

- **Préparation de données** : Normalisation des dimensions d'entrée pour les réseaux de neurones
- **Data augmentation** : Génération de variantes d'images par cropping
- **Extraction de caractéristiques** : Focus sur des régions d'intérêt spécifiques
- **Optimisation computationnelle** : Réduction de la complexité spatiale

## Exécution et validation

```bash
python solution.py
```

**Sortie attendue :**
Affichage d'une matrice 10×10 aléatoire suivie de sa sous-matrice 5×5 centrale extraite.

## Concepts transversaux

- **Algèbre linéaire** : Opérations sur les sous-espaces vectoriels
- **Probabilités** : Génération de distributions aléatoires pour simulation
- **Optimisation** : Réduction dimensionnelle pour améliorer l'efficacité algorithmique
- La normalisation des tailles d'images pour l'entraînement de modèles

## Exécution

```bash
python solution.py
```

## Résultat attendu

Affiche une matrice 10x10 aléatoire puis sa sous-matrice centrale 5x5.
