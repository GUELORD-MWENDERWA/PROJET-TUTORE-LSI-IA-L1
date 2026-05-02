#!/usr/bin/env python
"""Test rapide: generation image + entrainement sklearn."""
import sys
import os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)

from src.ml.generate_image_dataset import generate_image_dataset, save_dataset
from src.ml.object_classifier import load_dataset, train_and_evaluate

dataset_path = os.path.join(root, "data", "processed", "objects.csv")
df = generate_image_dataset(samples_per_class=80, image_size=96)
save_dataset(df, dataset_path)
X, y = load_dataset(dataset_path)

results = train_and_evaluate(X, y, k=5)

print(f"Dataset: {len(df)} echantillons")
print(f"Classes: {sorted(set(y))}")
print(f"Accuracy test: {results['accuracy']:.3f}")
