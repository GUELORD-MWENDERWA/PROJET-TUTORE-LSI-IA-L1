# Exercice 10 : Extraction de caractéristiques et classification morphologique

## Objectif pédagogique

Comprendre l'extraction de caractéristiques morphologiques et l'implémentation de règles de décision simples pour la classification d'objets dans les images binaires.

## Concepts mathématiques fondamentaux

### Morphologie mathématique

- **Image binaire** : $I: \mathbb{Z}^2 \rightarrow \{0,1\}$ où 1 représente l'objet, 0 le fond
- **Caractéristiques morphologiques** : Propriétés géométriques extraites de l'objet
- **Aire (surface)** : $A = \sum_{i,j} I_{ij}$ nombre total de pixels de l'objet

### Classification par seuil

- **Fonction de décision** : $f(x) = \mathbb{I}_{x > \theta}$ où $\theta$ est le seuil
- **Espace de décision** : Partition binaire de l'espace des caractéristiques
- **Erreur de classification** : Probabilité de mauvaise décision

## Description technique

Cet exercice implémente une chaîne de traitement simplifiée :

1. **Génération synthétique** : Création d'une forme géométrique binaire
2. **Extraction de caractéristiques** : Calcul de descripteurs morphologiques
3. **Classification automatique** : Application d'une règle de décision

## Implémentation et analyse

```python
import numpy as np

# Génération d'une forme binaire : carré 3×3 centré dans matrice 5×5
image_binaire = np.zeros((5, 5), dtype=np.uint8)
image_binaire[1:4, 1:4] = 1  # Indices 1,2,3 pour chaque dimension

# Extraction de la caractéristique morphologique : aire de l'objet
aire_objet = np.sum(image_binaire)

# Classification par seuil : distinction grand/petit objet
seuil_morphologique = 8  # Seuil empirique pour la classification
classification = aire_objet > seuil_morphologique

print("Representation binaire de l'objet:")
print(image_binaire)
print(f"\nAire morphologique: {aire_objet} pixels")
print(f"Seuil de decision: {seuil_morphologique}")
print(f"Classification: {'Grand carre' if classification else 'Petit carre'}")
```

## Analyse mathématique

### Géométrie de la forme

- **Matrice support** : $I \in \{0,1\}^{5 \times 5}$
- **Objet discret** : Ensemble des pixels $(i,j)$ où $I_{ij} = 1$
- **Aire calculée** : Cardinalité de l'ensemble objet = 9 pixels

### Fonction caractéristique

La classification repose sur la fonction indicatrice :
$d(A) = \begin{cases} 1 & \text{si } A > 8 \\ 0 & \text{sinon} \end{cases}$

Où $A$ représente l'aire morphologique de l'objet.

### Propriétés de la décision

- **Seuil adaptatif** : Peut être ajusté selon les besoins de l'application
- **Robustesse** : Insensible aux translations de l'objet dans l'image
- **Limites** : Ne capture que l'information de surface, pas la forme détaillée

## Applications en vision par ordinateur

Cette approche simplifiée est utilisée dans :

- **Contrôle qualité industriel** : Vérification de dimensions d'objets
- **Analyse de particules** : Comptage et classification en microscopie
- **Préprocessing** : Filtrage d'objets selon leur taille
- **Systèmes embarqués** : Classification rapide avec ressources limitées

## Exécution et validation

```bash
python solution.py
```

**Résultat attendu :**
Affichage de la matrice binaire, calcul de l'aire et classification résultante.

## Concepts transversaux abordés

- **Théorie des ensembles** : Caractérisation d'objets discrets
- **Statistiques spatiales** : Analyse morphologique des formes
- **Théorie de la décision** : Classification binaire par seuillage
  print(f"Classification: {'Grand carre' if est_grand_carre else 'Petit carre'}")

````

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
````

## Résultat attendu

Affiche l'image binaire, la somme des pixels et la classification résultante.
