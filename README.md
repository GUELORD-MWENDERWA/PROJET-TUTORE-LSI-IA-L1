# Geometric Shape Recognition with Classical Computer Vision

An end-to-end image classification project that recognizes seven geometric shapes from raw images. It covers the full machine learning workflow: synthetic data generation, image preprocessing, geometric feature engineering, supervised training, evaluation and inference through a desktop application.

Developed as the tutored project of the first year of the LSI-IA (Software Engineering and Artificial Intelligence) program at ISIG Goma. The goal is to understand the mathematics behind an AI decision by going from pixels to a prediction without relying on a black-box deep learning model.

**Classes:** square, rectangle, circle, ellipse, triangle, pentagon, hexagon.

## Pipeline

```
 Synthetic image      Preprocessing          Feature extraction        Classifier              Output
 generation      ──>  grayscale, threshold,  ──>  19 geometric and  ──>  StandardScaler    ──>  label +
 (OpenCV)             morphology, contour        Hu moment features      + Random Forest        confusion matrix
```

### Features

Each image is reduced to a vector of shape descriptors computed from its main contour:

| Group | Features |
| --- | --- |
| Size and proportions | width, height, aspect ratio, area, perimeter |
| Shape regularity | circularity, extent, solidity, eccentricity, area ratio |
| Polygon approximation | vertex count at fine, medium and coarse tolerance |
| Fill ratios | bounding-box fill, enclosing-circle fill |
| Invariant moments | first four Hu moments (log-scaled) |

Preprocessing is robust to inverted images (light shape on dark background and the reverse), ignores contours touching the border, and recentres the object before measuring it.

### Model

A scikit-learn `Pipeline` combining `StandardScaler` and a `RandomForestClassifier` with balanced class weights. The dataset is split 75/25 with a fixed random seed. Evaluation reports overall accuracy, a per-class classification report and a confusion matrix saved to `data/processed/confusion_matrix.png`.

## Getting started

Requirements: Python 3.10 or later.

```bash
git clone https://github.com/GUELORD-MWENDERWA/PROJET-TUTORE-LSI-IA-L1.git
cd PROJET-TUTORE-LSI-IA-L1
./run.sh                 # Windows: run.bat
```

The script creates a virtual environment, installs the dependencies and launches the application. To run steps manually:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt

python src/main.py                                  # desktop application (PyQt5)
python src/main.py --cli --samples 350 --size 96    # train and evaluate from the terminal
python src/main.py --image path/to/shape.png        # train, then classify one image
```

| Option | Default | Description |
| --- | --- | --- |
| `--samples` | 350 | Synthetic images generated per class |
| `--size` | 96 | Image size in pixels |
| `--k` | 5 | Model size parameter (number of trees = max(200, 40 x k)) |
| `--cli` | off | Run without the graphical interface |

The trained model is saved to `models/object_knn.joblib`.

## Tests

```bash
python tests/test_quick.py      # fast smoke test on a small dataset
python tests/test_model.py      # model training and prediction
python tests/test_complete.py   # full pipeline
```

## Repository structure

```
src/
  main.py                   Entry point (GUI or CLI)
  pipeline.py               Training and inference orchestration
  app/ui.py                 PyQt5 desktop interface
  core/image_feature_extractor.py
  ml/generate_image_dataset.py
  ml/generate_test_images.py
  ml/object_classifier.py
images/                     Reference images, one folder per class
data/processed/             Generated dataset and evaluation outputs
exercices_pratiques/        Ten guided exercises (see below)
tests/                      Smoke, model and end-to-end tests
docs/PROJECT_GUIDE.md       Detailed project guide
```

## Guided exercises

The `exercices_pratiques/` directory contains ten exercises that build up the skills used in the project. Each has a statement and a reference solution.

| # | Topic |
| --- | --- |
| 1 | Pixel manipulation with NumPy |
| 2 | Simulated image resizing |
| 3 | Simple colour detection by thresholding |
| 4 | Reading and displaying images with OpenCV |
| 5 | Colour to grayscale conversion |
| 6 | Edge detection with Canny |
| 7 | Displaying images with Matplotlib |
| 8 | Preparing data for machine learning |
| 9 | Training a k-nearest neighbours classifier |
| 10 | Object classification from pixel analysis |

## Tech stack

Python, NumPy, pandas, OpenCV, scikit-learn, Matplotlib, joblib, PyQt5.

## Limitations and next steps

- The model is trained mostly on synthetic images; accuracy on photographs with clutter, perspective or occlusion will be lower.
- Next steps: augment the dataset with real photographs, compare with a small convolutional neural network, and add real-time recognition from a webcam.

## License

No license has been specified yet. Contact the author before reusing this code.
