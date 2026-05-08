# Exercice 4 : Lecture et affichage d'une image avec OpenCV

## Objectif

Cet exercice montre comment ouvrir une image existante et l'afficher dans une fenêtre grâce à OpenCV.

## Ce que fait ce script

- Il lit un fichier image (`.jpg`, `.png`, etc.).
- Il vérifie que l'image a été chargée.
- Il ouvre une fenêtre pour afficher l'image.
- Il ferme la fenêtre après qu'une touche est pressée.

## Structure du code

- `load_image(image_path)` : charge l'image depuis le chemin.
- `display_image(window_name, image)` : affiche l'image et attend une touche.
- `main()` : gère les arguments et exécute l'affichage.

## Comment exécuter

1. Placez une image dans ce dossier ou utilisez un chemin complet.
2. Exécutez :

```bash
python solution.py --image mon_image.jpg
```

## Notes pour débutants

- OpenCV utilise l'espace de couleurs BGR, pas RGB.
- Si le script affiche une erreur, vérifiez que le nom du fichier est correct.
- `cv2.waitKey(0)` signifie "attendre indéfiniment" jusqu'à ce qu'une touche soit pressée.
