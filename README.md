# Projet IA - Reconnaissance de formes

Ce projet entraine un modele de Machine Learning pour reconnaitre des formes geometriques depuis une image.

Formes prises en charge:
- `Carre`
- `Rectangle`
- `Cercle`
- `Triangle`
- `Ellipse`
- `Pentagone`
- `Hexagone`

## Installation

```bash
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

## Lancer le projet

- Interface graphique:
```bash
python src/main.py
```

- Mode CLI (entrainement + prediction d'une image):
```bash
python src/main.py --cli --image "chemin/vers/image.png"
```

## Generer des donnees et images de test

- Regenerer le dataset d'entrainement:
```bash
python src/ml/generate_image_dataset.py
```

- Generer des images de test dans `images/`:
```bash
python src/ml/generate_test_images.py
```
Les images sont rangees par classe dans des sous-dossiers (`images/carre`, `images/cercle`, etc.).

## Pipeline resumee

1. Generation d'images synthetiques de formes avec OpenCV
2. Extraction de descripteurs geometriques (`w`, `h`, ratio, circularite, aire, etc.)
3. Entrainement d'un modele `StandardScaler + KNeighborsClassifier`
4. Evaluation (accuracy, classification report, matrice de confusion)
5. Prediction sur une image chargee par l'utilisateur

## Documentation detaillee

La documentation pedagogique complete est dans:
- `docs/PROJECT_GUIDE.md`
