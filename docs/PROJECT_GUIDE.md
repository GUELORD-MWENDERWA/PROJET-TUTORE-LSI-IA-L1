# Guide pedagogique du projet

## 1) Ce que fait le projet

Le projet construit un systeme complet de reconnaissance de formes:
- il genere un dataset d'images synthetiques,
- il extrait des caracteristiques mathematiques de chaque forme,
- il entraine un modele de classification,
- il permet de predire la forme d'une image chargee.

L'objectif est d'expliquer la chaine IA de bout en bout: **image brute -> features -> modele -> prediction**.

---

## 2) Architecture du code

### `src/main.py`
- Point d'entree de l'application.
- Lance soit l'interface PyQt5, soit un mode ligne de commande.

### `src/app/ui.py`
- Interface graphique.
- Boutons principaux:
  - entrainer le modele,
  - charger une image,
  - predire la forme.

### `src/pipeline.py`
- Orchestration globale.
- Fonctions:
  - `train_pipeline(...)`: genere dataset, entraine et sauvegarde le modele.
  - `predict_single_image(...)`: charge une image et retourne la prediction.

### `src/ml/generate_image_dataset.py`
- Generation d'images synthetiques pour chaque classe.
- Creation du DataFrame de features.
- Fonctions de dessin des formes (`draw_random_*`).
- `generate_image_dataset(...)` pour creer les donnees d'entrainement.
- `generate_test_images(...)` pour creer des images prêtes a tester dans l'UI.

### `src/ml/object_classifier.py`
- Partie Machine Learning avec scikit-learn.
- `ObjectKNNClassifier`: pipeline `StandardScaler + KNeighborsClassifier`.
- Fonctions utilitaires:
  - `load_dataset(...)`
  - `train_and_evaluate(...)`

### `src/core/image_feature_extractor.py`
- Partie vision/geométrie.
- Nettoie l'image en binaire.
- Trouve le contour principal.
- Recentre la forme pour reduire les erreurs de positionnement.
- Extrait un vecteur de features numeriques.

---

## 3) Role de chaque bibliotheque

### `OpenCV (cv2)`
- Creation des images de formes.
- Traitement d'image (gris, seuil Otsu, morphologie).
- Extraction des contours et mesures geometriques.

### `NumPy`
- Manipulation de tableaux pixels.
- Calculs numeriques rapides.

### `Pandas`
- Construction du dataset tabulaire (`objects.csv`).

### `scikit-learn`
- Entrainement du modele KNN.
- Standardisation des features.
- Evaluation (accuracy, rapport, matrice de confusion).

### `Matplotlib`
- Affichage/sauvegarde de la matrice de confusion.

### `PyQt5`
- Interface graphique desktop.

### `joblib`
- Sauvegarde/chargement du modele entraine.

---

## 4) Detail des features extraites

Le modele ne lit pas directement "la forme" comme un humain.  
Il lit un vecteur de mesures:

- `w`, `h`: largeur/hauteur de la boite englobante
- `aspect_ratio`: rapport entre dimensions
- `circularity`: proche de 1 pour les formes rondes
- `extent`: taux de remplissage de la boite englobante
- `solidity`: compacite par rapport a l'enveloppe convexe
- `perimeter`, `area`: perimetre et aire
- `vertices_fine`, `vertices_coarse`: estimation du nombre de sommets
- `hu1..hu4`: moments de Hu (forme globale, invariants)

Ces features rendent le modele robuste meme quand la forme est deplacee, agrandie ou legèrement tournee.

---

## 5) Formes reconnues

Classes actuellement utilisees:
- `Carre`
- `Rectangle`
- `Cercle`
- `Triangle`
- `Ellipse`
- `Pentagone`
- `Hexagone`

---

## 6) Flux d'execution complet

1. L'utilisateur entraine via l'UI ou CLI.
2. Le programme genere des images artificielles par classe.
3. Chaque image est convertie en features.
4. Les features sont enregistrees dans `data/processed/objects.csv`.
5. Le modele est entraine puis sauvegarde dans `models/object_knn.joblib`.
6. Lors d'une prediction, la meme extraction de features est appliquee a l'image test.
7. Le modele retourne l'etiquette de forme.

---

## 7) Comment tester rapidement

1. Generer les images:
   - `python src/ml/generate_test_images.py`
2. Entrainer:
   - bouton "Entrainer / Re-entrainer" dans l'UI
3. Charger une image depuis `images/`
4. Cliquer sur "Predire la forme"

---

## 8) Pourquoi le centrage est important

Sans centrage, une forme collee au bord peut etre mal analysee:
- contour tronque,
- mesures de boite englobante faussees,
- prediction moins stable.

La fonction de centrage recopie la forme extraite au centre d'une image vide de meme taille.  
Cela stabilise les features geometriques et ameliore la constance des predictions.
