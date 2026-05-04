import os
import random
import sys
import cv2
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.image_feature_extractor import extract_object_features


def _blank_image(image_size: int) -> np.ndarray:
    return np.zeros((image_size, image_size), dtype=np.uint8)


def draw_random_circle(image_size: int):
    image = _blank_image(image_size)
    radius = random.randint(14, 34)
    cx = random.randint(radius + 3, image_size - radius - 3)
    cy = random.randint(radius + 3, image_size - radius - 3)
    cv2.circle(image, (cx, cy), radius, 255, -1)
    return image, "Cercle"


def draw_random_rectangle(image_size: int):
    image = _blank_image(image_size)
    if random.random() < 0.5:
        w = random.randint(42, 62)
        h = random.randint(14, 24)
    else:
        w = random.randint(14, 24)
        h = random.randint(42, 62)
    x = random.randint(4, image_size - w - 4)
    y = random.randint(4, image_size - h - 4)
    cv2.rectangle(image, (x, y), (x + w, y + h), 255, -1)
    return image, "Rectangle"


def draw_random_square(image_size: int):
    image = _blank_image(image_size)
    side = random.randint(24, 44)
    x = random.randint(6, image_size - side - 6)
    y = random.randint(6, image_size - side - 6)
    cv2.rectangle(image, (x, y), (x + side, y + side), 255, -1)
    return image, "Carre"


def draw_random_triangle(image_size: int):
    image = _blank_image(image_size)
    base_y = random.randint(image_size // 2, image_size - 10)
    apex_y = random.randint(8, image_size // 3)
    left_x = random.randint(6, image_size // 3)
    right_x = random.randint(2 * image_size // 3, image_size - 6)
    apex_x = random.randint(image_size // 3, 2 * image_size // 3)
    pts = np.array([[apex_x, apex_y], [left_x, base_y], [right_x, base_y]], dtype=np.int32)
    cv2.fillPoly(image, [pts], 255)
    return image, "Triangle"


def draw_random_ellipse(image_size: int):
    image = _blank_image(image_size)
    center = (random.randint(28, image_size - 28), random.randint(28, image_size - 28))
    axes = (random.randint(18, 34), random.randint(10, 20))
    angle = random.randint(0, 180)
    cv2.ellipse(image, center, axes, angle, 0, 360, 255, -1)
    return image, "Ellipse"


def _regular_polygon_points(cx, cy, radius, sides, rotation_deg=0):
    pts = []
    for i in range(sides):
        theta = np.deg2rad(rotation_deg + (360.0 * i / sides))
        x = int(cx + radius * np.cos(theta))
        y = int(cy + radius * np.sin(theta))
        pts.append([x, y])
    return np.array(pts, dtype=np.int32)


def draw_random_pentagon(image_size: int):
    image = _blank_image(image_size)
    r = random.randint(16, 28)
    cx = random.randint(r + 8, image_size - r - 8)
    cy = random.randint(r + 8, image_size - r - 8)
    pts = _regular_polygon_points(cx, cy, r, 5, random.randint(0, 72))
    cv2.fillPoly(image, [pts], 255)
    return image, "Pentagone"


def draw_random_hexagon(image_size: int):
    image = _blank_image(image_size)
    r = random.randint(15, 26)
    cx = random.randint(r + 8, image_size - r - 8)
    cy = random.randint(r + 8, image_size - r - 8)
    pts = _regular_polygon_points(cx, cy, r, 6, random.randint(0, 30))
    cv2.fillPoly(image, [pts], 255)
    return image, "Hexagone"


DRAWERS = [
    draw_random_circle,
    draw_random_square,
    draw_random_rectangle,
    draw_random_triangle,
    draw_random_ellipse,
    draw_random_pentagon,
    draw_random_hexagon,
]
FEATURE_COLUMNS = [
    "w",
    "h",
    "aspect_ratio",
    "circularity",
    "extent",
    "solidity",
    "perimeter",
    "area",
    "vertices_fine",
    "vertices_mid",
    "vertices_coarse",
    "box_fill",
    "circle_fill",
    "area_ratio",
    "eccentricity",
    "hu1",
    "hu2",
    "hu3",
    "hu4",
]


def generate_image_dataset(samples_per_class: int = 300, image_size: int = 96):
    rows = []
    for drawer in DRAWERS:
        for _ in range(samples_per_class):
            image, label = drawer(image_size)
            features = extract_object_features(image)
            if features is None:
                continue
            row = dict(zip(FEATURE_COLUMNS, features.tolist()))
            row["label"] = label
            rows.append(row)

    return pd.DataFrame(rows)


def generate_test_images(output_dir: str, per_class: int = 5, image_size: int = 256):
    """Genere des images de test par classe dans des sous-dossiers."""
    os.makedirs(output_dir, exist_ok=True)

    # Nettoie les anciennes images "a plat" pour garder une structure claire.
    for entry in os.listdir(output_dir):
        full_path = os.path.join(output_dir, entry)
        if os.path.isfile(full_path) and entry.lower().endswith(".png"):
            os.remove(full_path)

    for drawer in DRAWERS:
        _, class_label = drawer(image_size)
        class_name = class_label.lower()
        class_dir = os.path.join(output_dir, class_name)
        os.makedirs(class_dir, exist_ok=True)
        for idx in range(1, per_class + 1):
            image, label = drawer(image_size)
            file_name = f"{class_name}_{idx:02d}.png"
            output_path = os.path.join(class_dir, file_name)
            cv2.imwrite(output_path, image)
            print(f"Image test creee: {output_path} ({label})")


def save_dataset(df: pd.DataFrame, output_csv: str):
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index=False)


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    csv_path = os.path.join(root, "data", "processed", "objects.csv")
    dataset = generate_image_dataset(samples_per_class=350, image_size=96)
    save_dataset(dataset, csv_path)
    print(f"Dataset image genere: {len(dataset)} lignes -> {csv_path}")