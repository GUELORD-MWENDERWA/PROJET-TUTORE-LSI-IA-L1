# 📁 Structure du Projet

## Répertoires

```
projet_tutore/
├── src/                    # Code source principal
│   ├── main.py            # Point d'entrée original
│   ├── app/               # Interface graphique
│   │   ├── __init__.py
│   │   └── ui.py          # Application PyQt5
│   ├── core/              # Logique métier
│   │   ├── __init__.py
│   │   └── shape_analyzer.py  # Extraction des features
│   ├── ml/                # Machine Learning
│   │   ├── __init__.py
│   │   └── model.py       # Modèle KNN
│   └── utils/             # Utilitaires
│       ├── __init__.py
│       └── geometry.py    # Fonctions géométriques
│
├── data/                  # Données
│   └── processed/
│       └── shapes.csv     # Dataset d'entraînement
│
├── tests/                 # Tests
│   ├── __init__.py
│   ├── test_quick.py      # Test rapide du modèle
│   ├── test_model.py      # Tests complets
│   └── test_complete.py   # Tests avec formes artificielles
│
├── scripts/               # Scripts utilitaires
│   ├── __init__.py
│   ├── diagnostic.py      # Diagnostic du modèle
│   └── debug_features.py  # Debug d'extraction de features
│
├── docs/                  # Documentation
│   ├── __init__.py
│   └── CHANGEMENTS.md     # Historique des changements
│
├── START.py               # 🚀 Lanceur principal
├── src/main.py            # Point d'entrée original
├── README.md              # Documentation principale
├── requirements.txt       # Dépendances Python
├── run.bat                # Script lanceur (Windows)
└── run.sh                 # Script lanceur (Linux/Mac)
```

## Fichiers Racine

- **START.py** : Lanceur de l'application (recommandé)
- **src/main.py** : Alternative pour lancer l'app
- **README.md** : Documentation générale
- **requirements.txt** : Dépendances Python
- **run.bat / run.sh** : Scripts d'installation et lancement

## Utilisation

### Lancer l'application

```bash
python START.py
```

### Tester le modèle

```bash
python tests/test_quick.py
```

### Diagnostic détaillé

```bash
python scripts/diagnostic.py
```
