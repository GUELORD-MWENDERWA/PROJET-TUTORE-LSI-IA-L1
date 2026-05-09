# Projet IA L1 - Reconnaissance de formes géométriques

## Objectifs pédagogiques

**BUT** : Maîtriser les bases de l'intelligence artificielle à travers l'étude des mathématiques décisionnelles, l'initiation à Python et l'entraînement de modèles de reconnaissance d'objets utilisant les frameworks NumPy/Pandas.

### Mission

Comprendre la logique mathématique de l'IA et réaliser un premier projet d'identification visuelle automatisée, illustrant le passage de la donnée brute (images) à une décision algorithmique.

### Compétences développées

- **Mathématiques décisionnelles** : Algèbre linéaire, statistiques et probabilités appliquées à la modélisation
- **Manipulation de données** : Nettoyage, structuration et analyse de jeux de données avec NumPy/Pandas
- **Reconnaissance d'objets** : Entraînement de modèles capables d'identifier des formes géométriques
- **Programmation Python** : Maîtrise du langage pilier de l'IA

## Description du projet

Ce projet implémente un système de reconnaissance automatique de formes géométriques à partir d'images numériques. Les formes reconnues incluent :

- Carré, Rectangle, Cercle, Triangle
- Ellipse, Pentagone, Hexagone

## Architecture technique

### Pipeline de traitement

1. **Acquisition de données** : Génération d'images synthétiques de formes géométriques
2. **Extraction de caractéristiques** : Analyse morphologique et statistique des pixels
3. **Entraînement du modèle** : Apprentissage supervisé avec algorithmes de classification
4. **Évaluation et prédiction** : Validation des performances et classification de nouvelles images

### Technologies utilisées

- **NumPy** : Calculs matriciels et manipulation de tableaux multidimensionnels
- **OpenCV** : Traitement d'images et extraction de caractéristiques visuelles
- **Matplotlib** : Visualisation de données et résultats
- **Scikit-learn** : Algorithmes d'apprentissage automatique
- **Pandas** : Structures de données tabulaires (optionnel pour extension)

## Structure du projet

```
projet_tutore/
├── src/                    # Code principal de l'application
│   ├── main.py            # Point d'entrée du programme
│   ├── pipeline.py        # Pipeline de traitement d'images
│   ├── app/ui.py          # Interface utilisateur
│   ├── core/              # Noyau fonctionnel
│   └── ml/                # Composants d'apprentissage automatique
├── exercices_pratiques/   # Exercices pédagogiques 1-10
├── images/                # Base de données d'images
├── models/                # Modèles entraînés sauvegardés
├── tests/                 # Tests unitaires et d'intégration
└── docs/                  # Documentation technique
```

## Installation et configuration

### Environnement virtuel

```bash
python -m venv env
# Windows
.\env\Scripts\activate
# Linux/Mac
source env/bin/activate
```

### Dépendances

```bash
pip install -r requirements.txt
```

## Utilisation

### Interface graphique principale

```bash
python src/main.py
```

### Génération de données d'entraînement

```bash
python src/ml/generate_image_dataset.py
```

### Tests du modèle

```bash
python src/ml/generate_test_images.py
```

## Exercices pratiques

Les exercices 1 à 10 constituent une progression pédagogique couvrant :

1. **Manipulation matricielle** : Représentation d'images avec NumPy
2. **Traitement d'images** : Conversion, seuillage, détection de contours
3. **Apprentissage automatique** : Préparation de données et entraînement de classifieurs
4. **Évaluation** : Mesure des performances et validation croisée

Chaque exercice inclut une implémentation complète avec documentation technique détaillée.

## Évaluation et métriques

Le système évalue les performances selon plusieurs critères :

- **Précision globale** : Taux de classification correcte
- **Matrice de confusion** : Analyse détaillée des erreurs
- **Métriques par classe** : Performance spécifique à chaque forme géométrique

## Perspectives d'extension

- Intégration de réseaux de neurones convolutionnels (CNN)
- Extension à la reconnaissance de formes complexes
- Optimisation des performances computationnelles
- Interface web pour déploiement applicatif

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
