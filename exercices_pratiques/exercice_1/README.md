# Exercice 1 : Manipulation de pixels avec NumPy

## Objectif

Cet exercice montre comment utiliser NumPy pour représenter une image simple comme un tableau de nombres. Il est conçu pour un débutant qui découvre Python, NumPy et la manipulation de pixels.

## Ce que fait ce script

- Il crée un tableau NumPy de taille 3x3 rempli de zéros.
- Il modifie le pixel central (position [1, 1]) et le met à 255.
- Il affiche l'image avant et après la modification.

## Structure du code

- `create_simple_image()` : crée une image 3x3 noire.
- `set_center_pixel(image, value=255)` : remplace le pixel central par la valeur blanche 255.
- `main()` : exécute les fonctions et affiche les résultats.

## Pourquoi c'est utile

- Une image en niveaux de gris peut être stockée comme un tableau NumPy.
- Chaque case du tableau représente un pixel.
- `0` signifie noir, `255` signifie blanc.

## Comment exécuter

1. Ouvrez une console dans ce dossier : `exercice_1`
2. Activez votre environnement Python si nécessaire.
3. Lancez le script :

```bash
python solution.py
```

## Conseils pour débutants

- `np.zeros((3, 3))` crée une image noire.
- `image[1, 1]` accède au pixel du milieu.
- Copier l'image avec `image.copy()` évite de modifier l'original directement.
