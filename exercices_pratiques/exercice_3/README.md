# Exercice 3 : Détection de couleur simple (seuillage)

## Objectif

Cet exercice montre comment transformer une image en niveaux de gris en une image binaire qui sépare le "clair" du "sombre".

## Ce que fait ce script

- Il crée une image 5x5 avec des valeurs de pixels aléatoires entre 0 et 255.
- Il compare chaque pixel à un seuil de 127.
- Il génère une image binaire où les valeurs supérieures au seuil deviennent 1 et les autres deviennent 0.

## Structure du code

- `create_random_image()` : crée un tableau NumPy 5x5.
- `threshold_image(image, threshold=127)` : transforme l'image en noir/blanc.
- `main()` : affiche l'image originale et l'image seuillée.

## Comment exécuter

```bash
python solution.py
```

## Explication pour débutants

- La comparaison `image > threshold` crée un tableau de valeurs booléennes (`True` ou `False`).
- `astype(np.uint8)` convertit ces valeurs en `0` et `1`.
- L'image binaire est utile pour détecter des zones claires ou sombres.
