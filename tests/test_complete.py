#!/usr/bin/env python
"""Test complet pipeline image -> features -> prediction."""
import sys
import os
import cv2
import numpy as np

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)

from src.core.image_feature_extractor import extract_object_features
from src.ml.generate_image_dataset import generate_image_dataset, save_dataset
from src.ml.object_classifier import load_dataset, train_and_evaluate

print("=" * 70)
print("TEST COMPLET DU MODELE - RECONNAISSANCE D'OBJETS SUR IMAGES")
print("=" * 70)

# Charger le dataset
dataset_path = os.path.join(root, "data", "processed", "objects.csv")
dataset = generate_image_dataset(samples_per_class=150, image_size=96)
save_dataset(dataset, dataset_path)

X, y = load_dataset(dataset_path)
print(f"\nDataset charge: {len(X)} exemples")
for label in sorted(set(y)):
    print(f"{label}: {sum(y == label)}", end=" | ")
print()

train_results = train_and_evaluate(X, y, k=5)
model = train_results["model"]
print(f"Modele entraine avec k=5, accuracy={train_results['accuracy']:.3f}")

# Tests avec images artificielles
print("\n" + "=" * 70)
print("TESTS AVEC FORMES ARTIFICIELLES")
print("=" * 70)

def blank():
    return np.zeros((96, 96), dtype=np.uint8)


test_cases = {}
img = blank()
cv2.circle(img, (48, 48), 24, 255, -1)
test_cases["Cercle propre"] = {"image": img, "expected": "Cercle"}

img = blank()
cv2.rectangle(img, (18, 28), (78, 64), 255, -1)
test_cases["Rectangle propre"] = {"image": img, "expected": "Rectangle"}

img = blank()
cv2.rectangle(img, (24, 24), (72, 72), 255, -1)
test_cases["Carre propre"] = {"image": img, "expected": "Carre"}

img = blank()
pts = np.array([[48, 14], [18, 78], [78, 78]], dtype=np.int32)
cv2.fillPoly(img, [pts], 255)
test_cases["Triangle propre"] = {"image": img, "expected": "Triangle"}

img = blank()
cv2.ellipse(img, (48, 48), (24, 14), 30, 0, 360, 255, -1)
test_cases["Ellipse propre"] = {"image": img, "expected": "Ellipse"}

test_results = {"OK": 0, "KO": 0}
for name, test_case in test_cases.items():
    features = extract_object_features(test_case["image"])

    if features is not None:
        prediction = model.predict(features)
        status = "OK" if prediction == test_case["expected"] else "KO"
        if status == "OK":
            test_results["OK"] += 1
        else:
            test_results["KO"] += 1
        print(f"{status} {name:30} -> {prediction:12} (attendu: {test_case['expected']})")
        print(
            f"   Features: w={features[0]:5.1f} h={features[1]:5.1f} "
            f"aspect={features[2]:.2f} circ={features[3]:.2f} area={features[7]:.1f}"
        )
    else:
        print(f"KO {name:30} -> Objet invalide")
        test_results["KO"] += 1

print("\n" + "=" * 70)
print(f"RESUME: {test_results['OK']} reussis, {test_results['KO']} echoues")
print("=" * 70)
print("\nMatrice de confusion:")
print(train_results["confusion_matrix"])
