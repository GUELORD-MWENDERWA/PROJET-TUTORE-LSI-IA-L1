# Exercice 6 : Détection de bord simple avec OpenCV

## Objectif

Cet exercice montre comment appliquer un filtre de détection de bord (Canny) sur une image.

## Ce que fait ce script

- Il charge une image couleur.
- Il convertit l'image en niveaux de gris.
- Il applique l'algorithme Canny pour extraire les contours.
- Il affiche les deux images : l'image en gris et les bords détectés.

## Structure du code

- `load_image(image_path)` : charge l'image.
- `convert_to_grayscale(image)` : transforme l'image couleur en niveaux de gris.
- `detect_edges(image, threshold1, threshold2)` : applique Canny.
- `main()` : gère les arguments et affiche les résultats.

## Comment exécuter

```bash
python solution.py --image mon_image.jpg
```

## Explication pour débutants

- La détection de bord cherche les transitions rapides entre clair et foncé.
- `cv2.Canny(image, 100, 200)` utilise deux seuils : le premier pour détecter les bords forts, le second pour relier les bords.
- Cette méthode est souvent utilisée dans les projets d'IA pour détecter la forme générale d'un objet.
