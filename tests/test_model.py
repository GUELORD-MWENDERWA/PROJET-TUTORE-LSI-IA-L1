import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ml.generate_image_dataset import generate_image_dataset, save_dataset
from src.ml.object_classifier import load_dataset, train_and_evaluate


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dataset_path = os.path.join(project_root, "data", "processed", "objects.csv")

dataset = generate_image_dataset(samples_per_class=120, image_size=96)
save_dataset(dataset, dataset_path)
X, y = load_dataset(dataset_path)
print(f"Dataset charge: {len(X)} exemples")

results = train_and_evaluate(X, y, k=5)
print(f"Accuracy: {results['accuracy']:.3f}")
print(results["classification_report"])

