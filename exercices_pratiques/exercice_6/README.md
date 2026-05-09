# Exercice 6 : Détection de contours par filtrage de Canny

## Objectif pédagogique

Implémenter et analyser l'algorithme de détection de contours de Canny, en appliquant les concepts de calcul différentiel discret et de traitement du signal aux images numériques.

## Concepts mathématiques fondamentaux

### Gradient et dérivées discrètes

- **Gradient spatial** : Vecteur $(\partial_x I, \partial_y I)$ mesurant les variations d'intensité
- **Magnitude du gradient** : $G = \sqrt{(\partial_x I)^2 + (\partial_y I)^2}$
- **Direction du gradient** : $\theta = \arctan(\partial_y I / \partial_x I)$

### Algorithme de Canny (5 étapes)

1. **Lissage gaussien** : Réduction du bruit par convolution avec $G(x,y) = \frac{1}{2\pi\sigma^2}e^{-(x^2+y^2)/(2\sigma^2)}$
2. **Calcul des gradients** : Application des opérateurs de Sobel ou Prewitt
3. **Suppression des non-maxima** : Conservation des pics locaux du gradient
4. **Seuillage par hystérésis** : Double seuil avec seuils haut ($\theta_H$) et bas ($\theta_L$)
5. **Liaison des contours** : Connexion des pixels de contour valides

## Description technique

Cet exercice démontre l'implémentation complète du pipeline de Canny :

1. **Préparation des données** : Conversion en niveaux de gris pour traitement monochrome
2. **Application de l'algorithme** : Exécution des 5 étapes de Canny
3. **Validation visuelle** : Comparaison image originale vs contours extraits

## Implémentation et analyse

```python
import cv2

# Chargement de l'image source
chemin_image = '../../../images/cercle/cercle_01.png'
image_originale = cv2.imread(chemin_image)

if image_originale is not None:
    # Étape 1 : Conversion en niveaux de gris (préparation pour analyse monochrome)
    image_gris = cv2.cvtColor(image_originale, cv2.COLOR_BGR2GRAY)

    # Étape 2-5 : Application complète de l'algorithme de Canny
    # Paramètres : seuil_bas=100, seuil_haut=200
    image_contours = cv2.Canny(image_gris, 100, 200)

    # Visualisation comparative
    cv2.imshow('Image source', image_originale)
    cv2.imshow('Contours Canny', image_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Echec du chargement: {chemin_image}")
```

## Analyse mathématique

### Paramètres de seuillage

- **Seuil bas ($\theta_L = 100$)** : Définit les contours "faibles" candidats
- **Seuil haut ($\theta_H = 200$)** : Définit les contours "forts" certains
- **Ratio typique** : $\theta_H / \theta_L \approx 2-3$ pour équilibre sensibilité/précision

### Propriétés de l'algorithme

- **Optimalité** : Minimise les erreurs de détection selon les critères de Canny (1986)
- **Robustesse** : Insensible au bruit grâce au lissage gaussien
- **Connectivité** : Produit des contours connectés de largeur unitaire

### Représentation binaire

- **Image de contours** : $C \in \{0,1\}^{m \times n}$ où $C_{ij} = 1$ si contour détecté
- **Squelette fin** : Contours réduits à leur ligne médiane
- **Topologie préservée** : Connexité des régions séparées maintenue

## Applications en vision par ordinateur

L'algorithme de Canny est fondamental dans de nombreux domaines :

- **Segmentation d'images** : Extraction de primitives pour l'analyse de forme
- **Reconnaissance de formes** : Détection de caractéristiques géométriques
- **Suivi d'objets** : Extraction de contours pour le tracking temporel
- **Préprocessing** : Étape initiale pour de nombreux algorithmes de haut niveau

## Exécution et validation

```bash
python solution.py
```

**Résultat attendu :**
Affichage de l'image originale et de l'image binaire des contours détectés.

## Concepts transversaux abordés

- **Traitement du signal** : Filtrage et analyse fréquentielle des images
- **Calcul différentiel** : Approximation discrète des dérivées partielles
- **Théorie de la décision** : Seuillage multi-niveaux avec hystérésis
  cv2.destroyAllWindows()
  else:
  print(f"Erreur: Impossible de charger l'image à partir de {image_path}")

````

## Notions importantes

- **Seuils de Canny** : threshold1 (100) pour les bords forts, threshold2 (200) pour relier les bords
- **Étapes de Canny** : Lissage gaussien → Calcul des gradients → Suppression des non-maxima → Seuillage par hystérésis
- **Résultat binaire** : L'image de contours est une image binaire (noir/blanc)

## Applications pratiques

La détection de contours est utilisée pour :

- L'extraction de caractéristiques géométriques
- La segmentation d'objets
- La reconnaissance de formes
- Les systèmes de vision robotique
- L'analyse de documents et de texte

## Exécution

```bash
python solution.py
````

## Résultat attendu

Affiche l'image originale et une image binaire montrant uniquement les contours détectés.
