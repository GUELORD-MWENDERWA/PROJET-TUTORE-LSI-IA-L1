# Exercice 6 : Détection de contours avec l'algorithme de Canny

## Objectif

Implémenter la détection de contours dans les images à l'aide de l'algorithme de Canny.

## Concepts fondamentaux

- **Détection de contours** : Identification des transitions d'intensité dans une image
- **Algorithme de Canny** : Méthode multi-étapes pour une détection de contours optimale
- **Gradient d'intensité** : Mesure du changement d'intensité entre pixels voisins

## Description détaillée

Cet exercice couvre :

1. Le prétraitement de l'image (conversion en niveaux de gris)
2. L'application de l'algorithme de Canny
3. La visualisation des contours détectés

## Code et explication

```python
import cv2

# Chargement et prétraitement
image_path = '../../../images/cercle/cercle_01.png'
image = cv2.imread(image_path)

if image is not None:
    # Conversion en niveaux de gris
    image_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Détection de contours avec Canny
    contours = cv2.Canny(image_gris, 100, 200)

    # Affichage des résultats
    cv2.imshow('Image originale', image)
    cv2.imshow('Contours detectes', contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Erreur: Impossible de charger l'image à partir de {image_path}")
```

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
```

## Résultat attendu

Affiche l'image originale et une image binaire montrant uniquement les contours détectés.
