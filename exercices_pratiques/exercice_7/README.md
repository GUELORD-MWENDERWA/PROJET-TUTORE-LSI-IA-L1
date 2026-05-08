# Exercice 7 : Afficher des images avec Matplotlib

## Objectif

Cet exercice explique pourquoi Matplotlib est souvent utilisé pour afficher des images dans les notebooks Python.

## Ce que fait ce script

- Il charge une image avec OpenCV.
- Il convertit l'image du format BGR d'OpenCV vers le format RGB de Matplotlib.
- Il affiche l'image dans une fenêtre Matplotlib.

## Structure du code

- `load_image(image_path)` : charge un fichier image.
- `convert_bgr_to_rgb(image)` : change l'ordre des canaux de couleur.
- `display_image_with_matplotlib(image)` : montre l'image avec Matplotlib.
- `main()` : orchestre l'exécution.

## Comment exécuter

```bash
python solution.py --image mon_image.jpg
```

## Pourquoi c'est important

- OpenCV lit les images en BGR.
- Matplotlib attend des images en RGB.
- Si vous ne convertissez pas, les couleurs seront inversées (bleu/rouge).

## Conseils pour débutants

- `plt.axis('off')` enlève les axes, ce qui rend l'image plus propre.
- Cette méthode est utile dans les notebooks Jupyter ou lorsque l'affichage OpenCV est instable.
