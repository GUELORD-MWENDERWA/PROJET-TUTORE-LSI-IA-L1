# Exercice 2 : Redimensionnement simulé d'une image

## Objectif

Cet exercice montre comment utiliser NumPy pour simuler la réduction d'une image en prenant une partie centrale de l'image.

## Ce que fait ce script

- Il crée une image 10x10 avec des valeurs aléatoires (simulant des pixels).
- Il extrait une zone centrale de 5x5 pour simuler un redimensionnement.
- Il affiche l'image originale et la sous-image extraite.

## Structure du code

- `create_random_image(size=(10, 10))` : crée une image aléatoire.
- `central_crop(image, crop_size=5)` : extrait la zone centrale.
- `main()` : exécute l'exemple et affiche le résultat.

## Comment exécuter

```bash
python solution.py
```

## Notes importantes pour débutants

- Le redimensionnement réel utilise des algorithmes plus complexes, mais ce script montre le principe de "découper" une image.
- `image[start_row:start_row + crop_size, start_col:start_col + crop_size]` sélectionne la zone du milieu.
- Les indices NumPy commencent à 0, donc le centre d'une image 10x10 est autour de `[2:7, 2:7]`.
