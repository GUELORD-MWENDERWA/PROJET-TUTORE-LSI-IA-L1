# Exercice 7 : Affichage d'images avec Matplotlib

## Objectif

Maîtriser l'affichage d'images dans des environnements graphiques interactifs avec Matplotlib.

## Concepts fondamentaux

- **Matplotlib** : Bibliothèque de visualisation scientifique pour Python
- **Conversion BGR vers RGB** : Correction de l'ordre des canaux de couleur
- **Affichage interactif** : Visualisation dans des fenêtres avec contrôles

## Description détaillée

Cet exercice démontre :

1. Le chargement d'une image avec OpenCV
2. La conversion nécessaire entre formats de couleur
3. L'affichage avec Matplotlib pour une visualisation améliorée

## Code et explication

```python
import cv2
import matplotlib.pyplot as plt

# Chargement de l'image
image_path = '../../../images/triangle/triangle_01.png'
image_bgr = cv2.imread(image_path)

if image_bgr is not None:
    # Conversion BGR vers RGB pour Matplotlib
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    # Affichage avec Matplotlib
    plt.figure(figsize=(8, 6))
    plt.imshow(image_rgb)
    plt.title('Image affichee avec Matplotlib')
    plt.axis('off')  # Masquer les axes
    plt.show()
else:
    print(f"Erreur: Impossible de charger l'image à partir de {image_path}")
```

## Notions importantes

- **Format BGR d'OpenCV** : Bleu-Vert-Rouge (convention historique)
- **Format RGB standard** : Rouge-Vert-Bleu (convention Matplotlib)
- **plt.axis('off')** : Supprime les graduations des axes pour un affichage propre
- **plt.show()** : Affiche la figure dans une fenêtre interactive

## Applications pratiques

Matplotlib est préféré pour :

- Les environnements de développement interactifs (Jupyter notebooks)
- La visualisation scientifique avec annotations
- L'intégration dans des rapports et publications
- Le débogage avec des sous-graphiques multiples

## Exécution

```bash
python solution.py
```

## Résultat attendu

Ouvre une fenêtre Matplotlib affichant l'image avec les couleurs correctes et sans axes.
