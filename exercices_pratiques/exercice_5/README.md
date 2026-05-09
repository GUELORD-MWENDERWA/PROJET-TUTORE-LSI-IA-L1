# Exercice 5 : Conversion colorimétrique et réduction dimensionnelle

## Objectif pédagogique

Maîtriser les transformations colorimétriques entre espaces de couleurs et comprendre la réduction dimensionnelle dans le cadre de l'optimisation des représentations d'images pour l'apprentissage automatique.

## Concepts mathématiques fondamentaux

### Espaces colorimétriques

- **RGB/BGR** : Représentation trichrome $I: \mathbb{Z}^2 \rightarrow \mathbb{R}^3$ avec composantes (R,G,B)
- **Niveaux de gris** : Projection monochrome $I': \mathbb{Z}^2 \rightarrow \mathbb{R}$ avec luminance unique
- **Transformation affine** : Conversion linéaire entre espaces de couleurs

### Formule de luminance

La conversion standard RGB vers niveaux de gris utilise la luminance perceptive :
$I'_{ij} = 0.299 \cdot R_{ij} + 0.587 \cdot G_{ij} + 0.114 \cdot B_{ij}$

Cette formule pondère les canaux selon la sensibilité de l'œil humain :

- **Rouge (R)** : 29.9% - Moins sensible
- **Vert (G)** : 58.7% - Le plus sensible
- **Bleu (B)** : 11.4% - Le moins sensible

## Description technique

Cet exercice implémente la chaîne de traitement colorimétrique complète :

1. **Acquisition couleur** : Chargement d'une image trichrome depuis fichier
2. **Transformation linéaire** : Application de la matrice de conversion colorimétrique
3. **Visualisation comparative** : Affichage simultané des deux représentations

## Implémentation et analyse

```python
import cv2

# Chargement d'une image couleur (espace BGR d'OpenCV)
chemin_image = '../../../images/carre/carre_01.png'
image_bgr = cv2.imread(chemin_image)

if image_bgr is not None:
    # Conversion colorimétrique BGR → niveaux de gris
    # Application de la transformation : I' = 0.299*R + 0.587*G + 0.114*B
    image_gris = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

    # Affichage comparatif des représentations
    cv2.imshow('Representation trichrome (BGR)', image_bgr)
    cv2.imshow('Representation monochrome (gris)', image_gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Echec du chargement: {chemin_image}")
```

## Analyse mathématique

### Réduction dimensionnelle

- **Dimension initiale** : $I \in \mathbb{R}^{m \times n \times 3}$ (3 canaux couleur)
- **Dimension finale** : $I' \in \mathbb{R}^{m \times n \times 1}$ (1 canal luminance)
- **Facteur de compression** : Réduction de 67% de l'espace de stockage

### Propriétés de la transformation

- **Linéarité** : Préservation des relations d'ordre local
- **Continuité** : Fonction dérivable permettant l'optimisation
- **Robustesse** : Insensibilité relative aux variations d'éclairage

### Représentation matricielle

$\begin{pmatrix} I'_{11} & I'_{12} & \cdots \\ I'_{21} & I'_{22} & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix} = \begin{pmatrix} 0.299 & 0.587 & 0.114 \end{pmatrix} \begin{pmatrix} R_{11} & R_{12} & \cdots \\ G_{11} & G_{12} & \cdots \\ B_{11} & B_{12} & \cdots \end{pmatrix}$

## Applications en apprentissage automatique

Cette transformation est cruciale pour de nombreux algorithmes :

- **Préprocessing** : Réduction de la complexité avant classification
- **Normalisation** : Uniformisation des représentations d'entrée
- **Optimisation** : Accélération des calculs sur GPUs
- **Robustesse** : Diminution de la sensibilité aux variations colorimétriques

## Exécution et validation

```bash
python solution.py
```

**Résultat attendu :**
Deux fenêtres affichant respectivement l'image couleur originale et sa version en niveaux de gris.

## Concepts transversaux

- **Algèbre linéaire** : Transformations matricielles et projections
- **Psychophysique** : Modélisation de la perception visuelle humaine
- **Optimisation computationnelle** : Réduction dimensionnelle pour l'efficacité

````

## Notions importantes

- **Format BGR** : OpenCV charge les images en Bleu-Vert-Rouge (différent du RGB standard)
- **Conversion cv2.COLOR_BGR2GRAY** : Utilise la formule Y = 0.299*R + 0.587*G + 0.114\*B
- **Réduction de dimension** : L'image couleur (3 canaux) devient monochrome (1 canal)

## Applications pratiques

La conversion en niveaux de gris est utilisée pour :

- Réduire la complexité computationnelle
- Préparer les images pour certains algorithmes de traitement
- Normaliser les images avant l'analyse
- Améliorer les performances de certains détecteurs de caractéristiques

## Exécution

```bash
python solution.py
````

## Résultat attendu

Affiche deux fenêtres : l'image couleur originale et sa version en niveaux de gris.
