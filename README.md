# 🧠 Projet IA - Reconnaissance d'Objets sur Images

Projet de synthese IA centre sur le passage **donnee brute (image)** -> **features mathematiques** -> **decision algorithmique**.
Technologies: `Python`, `NumPy`, `Pandas`, `OpenCV`, `Matplotlib`, `scikit-learn`.

## 📋 Structure du Projet

```
.
├── data/
│   └── processed/
│       └── objects.csv                    # Dataset d'entrainement
├── src/
│   ├── main.py                            # Pipeline complet (entrainement + prediction image)
│   ├── core/
│   │   └── image_feature_extractor.py     # Extraction de features depuis image
│   └── ml/
│       ├── object_classifier.py           # Classifieur KNN
│       └── generate_image_dataset.py      # Generation d'images + dataset CSV
├── tests/
├── requirements.txt
└── README.md
```

## 🚀 Installation

1. `python -m venv env`
2. `.\env\Scripts\Activate.ps1`
3. `pip install -r requirements.txt`

## 🎯 Utilisation

Lancer l'interface PyQt5:

```bash
python src/main.py
```

Dans l'UI:
- bouton **Entrainer / Re-entrainer** pour construire le modele
- bouton **Charger une image** pour selectionner une image
- bouton **Predire la forme** pour obtenir la classe

Predire la forme sur une image donnee:

```bash
python src/main.py --image "chemin/vers/mon_image.png"
```

### Commandes utiles

- Generer uniquement le dataset:

```bash
python src/ml/generate_image_dataset.py
```

- Lancer un test rapide:

```bash
python tests/test_quick.py
```

## 📊 Pipeline IA

1. Generation d'images synthetiques d'objets (cercle, rectangle, triangle, ellipse, pentagone, hexagone) avec OpenCV
2. Extraction de features geometriques depuis les pixels:
   - `w`, `h`
   - `aspect_ratio`
   - `circularity`
   - `extent`, `solidity`
   - `perimeter`, `area`
3. Structuration dans `objects.csv` avec Pandas
4. Entrainement d'un modele `scikit-learn` (pipeline `StandardScaler + KNeighborsClassifier`)
5. Evaluation (accuracy, rapport de classification, matrice de confusion)
6. Visualisation avec Matplotlib (`confusion_matrix.png`)

## 🎓 Lien avec les objectifs pedagogiques

- **Algebre lineaire**: representation vectorielle des objets et distances dans l'espace des features
- **Statistiques/probabilites**: separation train/test, normalisation, decision par voisinage (KNN)
- **Data manipulation (NumPy/Pandas)**: nettoyage, structuration et analyse du dataset
- **Reconnaissance d'objets**: identification automatique d'objets dans des images
- **Python**: implementation complete de la chaine IA de bout en bout
