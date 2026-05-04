import os
import cv2
import matplotlib.pyplot as plt

from core.image_feature_extractor import extract_object_features
from ml.generate_image_dataset import FEATURE_COLUMNS, generate_image_dataset, save_dataset
from ml.object_classifier import ObjectKNNClassifier, load_dataset, train_and_evaluate


def train_pipeline(project_root, samples_per_class=350, image_size=96, k=5):
    dataset_path = os.path.join(project_root, "data", "processed", "objects.csv")
    chart_path = os.path.join(project_root, "data", "processed", "confusion_matrix.png")
    model_path = os.path.join(project_root, "models", "object_knn.joblib")

    dataset = generate_image_dataset(samples_per_class=samples_per_class, image_size=image_size)
    save_dataset(dataset, dataset_path)
    print(f"Dataset cree: {dataset_path} ({len(dataset)} lignes)")
    print(f"Features: {FEATURE_COLUMNS}")

    X, y = load_dataset(dataset_path)
    results = train_and_evaluate(X, y, k=k)

    print(f"\nAccuracy test: {results['accuracy']:.3f}")
    print("\nRapport de classification:")
    print(results["classification_report"])

    cm = results["confusion_matrix"]
    labels = results["labels"]

    plt.figure(figsize=(7, 6))
    plt.imshow(cm, cmap="Blues")
    plt.title("Matrice de confusion - Reconnaissance d'objets")
    plt.colorbar()
    plt.xticks(range(len(labels)), labels, rotation=30)
    plt.yticks(range(len(labels)), labels)
    plt.xlabel("Prediction")
    plt.ylabel("Classe reelle")
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, str(cm[i, j]), ha="center", va="center", color="black")
    plt.tight_layout()
    plt.savefig(chart_path, dpi=140)
    print(f"Matrice de confusion enregistree: {chart_path}")

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    results["model"].save(model_path)
    print(f"Modele enregistre: {model_path}")
    return model_path, results["accuracy"]


def predict_single_image(model_path, image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Image introuvable ou invalide: {image_path}")

    features = extract_object_features(image)
    if features is None:
        raise ValueError("Impossible d'extraire les features depuis cette image.")

    model = ObjectKNNClassifier()
    model.load(model_path)
    prediction = model.predict(features)
    return prediction


def predict_single_image_with_confidence(model_path, image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Image introuvable ou invalide: {image_path}")

    features = extract_object_features(image)
    if features is None:
        raise ValueError("Impossible d'extraire les features depuis cette image.")

    model = ObjectKNNClassifier()
    model.load(model_path)
    prediction = model.predict(features)
    proba = model.predict_proba(features)
    confidence = float(max(proba))
    return prediction, confidence
