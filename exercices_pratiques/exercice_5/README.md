# Exercice 5 : Conversion couleur -> niveaux de gris

## Objectif

Cet exercice montre comment transformer une image couleur en une image en niveaux de gris avec OpenCV.

## Ce que fait ce script

- Il charge une image couleur.
- Il convertit l'image de BGR vers grayscale.
- Il affiche l'image originale et l'image convertie.

## Structure du code

- `load_image(image_path)` : lit l'image.
- `convert_to_grayscale(image)` : convertit une image couleur en niveaux de gris.
- `main()` : affiche les deux images dans des fenêtres séparées.

## Comment exécuter

```bash
python solution.py --image mon_image.jpg
```

## Conseils pour débutants

- En reconnaissance d'image, on réduit souvent une image couleur en gris pour simplifier le traitement.
- OpenCV lit une image en format BGR. La conversion vers grayscale est automatique avec `cv2.cvtColor`.
- Si OpenCV ne trouve pas l'image, le script affiche une erreur claire.
