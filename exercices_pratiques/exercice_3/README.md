# Exercice 3 : Seuillage binaire et segmentation par seuil fixe

## Objectif pédagogique

Maîtriser les techniques de seuillage binaire dans le cadre de la segmentation d'images, en appliquant les concepts de statistiques descriptives et de logique booléenne aux opérations matricielles.

## Concepts mathématiques fondamentaux

### Fonction de seuillage

- **Seuillage binaire** : Transformation $T: \mathbb{R}^{m \times n} \rightarrow \{0,1\}^{m \times n}$ définie par :
  $T(I)_{ij} = \begin{cases} 1 & \text{si } I_{ij} > \theta \\ 0 & \text{sinon} \end{cases}$
- **Seuil statistique** : Valeur $\theta$ souvent choisie comme la moyenne empirique ou médiane
- **Segmentation binaire** : Partition de l'image en deux classes (avant-plan/arrière-plan)

### Logique vectorielle

- **Comparaison élément-wise** : Application de l'opérateur de comparaison à chaque élément
- **Conversion de types** : Transformation booléen → entier pour compatibilité numérique
- **Fonction caractéristique** : Représentation mathématique de l'appartenance à une classe

## Description technique

Cet exercice démontre l'implémentation pratique de l'algorithme de seuillage :

1. **Génération de données** : Création d'une matrice simulant une image en niveaux de gris
2. **Application du seuil** : Classification binaire de chaque pixel
3. **Conversion numérique** : Transformation en matrice binaire exploitable

## Implémentation et analyse

```python
import numpy as np

# Génération d'une matrice 5×5 avec distribution uniforme [0, 255]
# Simulation d'une image en niveaux de gris
image_gris = np.random.randint(0, 256, size=(5, 5))

# Application du seuillage binaire avec θ = 127 (médiane théorique)
# Opération vectorielle : chaque élément comparé indépendamment
seuil = 127
image_binaire = (image_gris > seuil).astype(np.uint8)

print("Matrice originale (niveaux de gris):")
print(image_gris)
print(f"\nMatrice binaire (seuillage θ = {seuil}):")
print(image_binaire)
```

## Analyse mathématique

### Fonction de décision

Pour chaque pixel $p \in [0, 255]$ :

- **Classe 0 (noir)** : $p \leq 127$
- **Classe 1 (blanc)** : $p > 127$

### Propriétés statistiques

- **Seuil médian** : $\theta = 127$ correspond à la valeur centrale pour 8 bits
- **Équilibre des classes** : Théoriquement 50% de pixels dans chaque classe
- **Robustesse** : Insensibilité aux variations d'éclairage uniforme

### Représentation matricielle

- **Avant seuillage** : $I \in \mathbb{R}^{5 \times 5}, I_{ij} \in [0, 255]$
- **Après seuillage** : $B \in \{0,1\}^{5 \times 5}, B_{ij} = \mathbb{I}_{I_{ij} > 127}$

## Applications en vision par ordinateur

Le seuillage constitue une étape fondamentale dans de nombreux algorithmes :

- **Segmentation d'images** : Séparation automatique des régions d'intérêt
- **Binarisation de documents** : Préparation pour l'OCR (reconnaissance optique de caractères)
- **Détection de mouvement** : Comparaison d'images successives
- **Préprocessing** : Simplification des données avant analyse avancée

## Exécution et validation

```bash
python solution.py
```

**Sortie attendue :**
Affichage d'une matrice 5×5 aléatoire en niveaux de gris, suivie de sa version binarisée avec le seuil 127.

## Concepts transversaux abordés

- **Statistiques** : Utilisation de seuils pour la classification automatique
- **Algèbre booléenne** : Opérations logiques appliquées aux matrices
- **Théorie de la décision** : Classification binaire dans un espace discret
- Les systèmes de vision industrielle

## Exécution

```bash
python solution.py
```

## Résultat attendu

Affiche une matrice 5x5 aléatoire puis sa version binarisée avec le seuil 127.
