# Exercice 4 : Lecture et affichage d'une image avec OpenCV

## Objectif

Maîtriser les opérations de base d'entrée/sortie d'images avec la bibliothèque OpenCV.

## Concepts fondamentaux

- **OpenCV** : Bibliothèque spécialisée dans le traitement d'images et la vision par ordinateur
- **Lecture d'image** : Chargement d'un fichier image en mémoire sous forme de tableau NumPy
- **Affichage d'image** : Création de fenêtres graphiques pour visualiser les images
- **Gestion d'événements** : Attente et traitement des interactions utilisateur

## Description détaillée

Cet exercice couvre :

1. Le chargement d'une image depuis le disque dur
2. La vérification de la réussite du chargement
3. L'affichage dans une fenêtre OpenCV
4. La gestion de la fermeture de fenêtre

## Code et explication

```python
import cv2

# Chemin vers l'image (utilise une image existante du projet)
image_path = '../../../images/carre/carre_01.png'

# Chargement de l'image
image = cv2.imread(image_path)

# Vérification du chargement
if image is not None:
    # Affichage dans une fenêtre
    cv2.imshow('Image OpenCV', image)
    # Attente d'une touche pour fermer
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Erreur: Impossible de charger l'image à partir de {image_path}")
```

## Notions importantes

- **cv2.imread()** : Retourne `None` si le fichier n'existe pas ou est corrompu
- **cv2.imshow()** : Crée une fenêtre avec le titre spécifié
- **cv2.waitKey(0)** : Attend indéfiniment une pression de touche
- **cv2.destroyAllWindows()** : Ferme toutes les fenêtres OpenCV ouvertes

## Applications pratiques

Ces fonctions de base sont essentielles pour :

- Le débogage de pipelines de traitement d'images
- La visualisation intermédiaire des résultats
- L'inspection manuelle des images chargées

## Exécution

```bash
python solution.py
```

## Résultat attendu

Ouvre une fenêtre affichant l'image carrée du projet. Appuyez sur une touche pour fermer.
