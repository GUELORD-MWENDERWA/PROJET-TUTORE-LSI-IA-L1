# Exercice 10 : Simulation de reconnaissance d'objet très basique

## Objectif

Cet exercice simule une reconnaissance d'objet simple en vérifiant si une forme contient suffisamment de pixels blancs.

## Ce que fait ce script

- Il crée un tableau NumPy 5x5 représentant une forme simple.
- Il calcule la somme de tous les pixels.
- Il compare cette somme à un seuil pour décider si la forme est un "grand carré".

## Structure du code

- `create_simple_shape()` : crée une image binaire avec un carré central.
- `recognize_large_square(image, threshold_pixels)` : vérifie si la somme des pixels dépasse le seuil.
- `main()` : affiche l'image et le résultat de la reconnaissance.

## Comment exécuter

```bash
python solution.py
```

## Explication pour débutants

- `np.sum(image)` additionne tous les pixels de l'image.
- Dans une image binaire, plus il y a de `1`, plus la forme est grande.
- Ce script ne fait pas de vraie reconnaissance intelligente : il utilise simplement une règle basée sur la taille.

## Pourquoi c'est utile

- C'est une première étape pour comprendre comment un algorithme peut prendre une décision.
- Les vrais modèles de reconnaissance utilisent des règles plus complexes ou des réseaux de neurones.
