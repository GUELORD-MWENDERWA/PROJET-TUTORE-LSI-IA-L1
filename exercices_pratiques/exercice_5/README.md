# Exercice 5 : Conversion couleur vers niveaux de gris

## Objectif

Comprendre la conversion d'images couleur RGB/BGR vers le format niveaux de gris.

## Concepts fondamentaux

- **Espace colorimétrique** : Système de représentation des couleurs (RGB, BGR, HSV, etc.)
- **Niveaux de gris** : Représentation monochrome où chaque pixel a une intensité unique
- **Conversion colorimétrique** : Transformation mathématique entre espaces de couleurs

## Description détaillée

Cet exercice démontre :

1. Le chargement d'une image couleur
2. La conversion BGR vers niveaux de gris
3. L'affichage comparatif des deux versions

## Code et explication

```python
import cv2

# Chargement d'une image couleur
image_path = '../../../images/carre/carre_01.png'
image_couleur = cv2.imread(image_path)

if image_couleur is not None:
    # Conversion en niveaux de gris
    image_gris = cv2.cvtColor(image_couleur, cv2.COLOR_BGR2GRAY)

    # Affichage des deux versions
    cv2.imshow('Image Originale', image_couleur)
    cv2.imshow('Image en niveaux de gris', image_gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Erreur: Impossible de charger l'image à partir de {image_path}")
```

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
```

## Résultat attendu

Affiche deux fenêtres : l'image couleur originale et sa version en niveaux de gris.
