# Projet IA - Reconnaissance de formes

Ce projet est conçu pour un débutant en programmation et en intelligence artificielle. Il montre comment créer des images simples, extraire des caractéristiques, entraîner un modèle et faire des prédictions.

## Qu'est-ce que ce projet fait ?

Ce projet apprend à reconnaître des formes géométriques à partir d'une image. Les formes prises en charge sont :

- `Carre`
- `Rectangle`
- `Cercle`
- `Triangle`
- `Ellipse`
- `Pentagone`
- `Hexagone`

## Pourquoi ce projet est utile pour un débutant

- Il utilise Python et des bibliothèques populaires comme NumPy, OpenCV, Matplotlib et Scikit-learn.
- Il montre les étapes de base d'un projet de reconnaissance d'images.
- Il contient des exercices pratiques pour apprendre pas à pas.

## Structure du projet

- `src/` : code principal de l'application.
- `src/ml/` : scripts de génération de données et de tests.
- `docs/` : documentation pédagogique.
- `images/` : exemples d'images générées.
- `exercices_pratiques/` : dossiers des exercices 1 à 10.
- `models/` : modèles entraînés.

## Installation

1. Créez et activez un environnement virtuel :

```bash
python -m venv env
.\env\Scripts\activate
```

2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

## Exécution du projet principal

- Pour lancer l'interface graphique :

```bash
python src/main.py
```

- Pour lancer en mode ligne de commande et prédire une image :

```bash
python src/main.py --cli --image "chemin/vers/image.png"
```

## Génération de données et d'images de test

- Pour régénérer le dataset d'entraînement :

```bash
python src/ml/generate_image_dataset.py
```

- Pour générer des images de test :

```bash
python src/ml/generate_test_images.py
```

Les images générées sont rangées par classe dans des sous-dossiers comme `images/carre`, `images/cercle`, etc.

## Exercices pratiques

Chaque exercice se trouve dans `exercices_pratiques/exercice_X` et contient :

- `solution.py` : le code Python qui résout l'exercice.
- `README.md` : une explication détaillée étape par étape.

Ces exercices vous aident à comprendre :

- comment manipuler des images avec NumPy,
- comment lire et afficher une image avec OpenCV,
- comment convertir une image en niveaux de gris,
- comment détecter des bords,
- comment afficher une image avec Matplotlib,
- comment préparer des données pour un modèle,
- et comment entraîner un classifieur K-NN.

## Concepts de base expliqués ici

- **Python** : langage utilisé pour écrire les scripts.
- **NumPy** : bibliothèque pour manipuler des tableaux et des images.
- **OpenCV** : bibliothèque pour lire, afficher et transformer des images.
- **Matplotlib** : outil pour afficher des images dans des notebooks ou des graphiques.
- **Scikit-learn** : bibliothèque pour entraîner des modèles simples.

## Conseils pour débutants

- Commencez par lire `exercices_pratiques/exercice_1/README.md`.
- Exécutez chaque script avec `python solution.py` dans le dossier de l'exercice.
- Lisez le README de chaque exercice : il explique le rôle de chaque fonction.
- Si vous ne comprenez pas un mot, cherchez-le : c'est normal pour un premier projet.

## Documentation détaillée

La documentation pédagogique complète se trouve dans :

- `docs/PROJECT_GUIDE.md`

> Si vous débutez, prenez le temps de lire chaque README d'exercice avant de lancer le script. Ils sont conçus pour expliquer chaque étape.
