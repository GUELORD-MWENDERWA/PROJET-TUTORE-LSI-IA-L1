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
        w = random.randint(36, 60)
        h = random.randint(14, 26)
    else:
        w = random.randint(16, 28)
        h = random.randint(34, 58)
    x = random.randint(4, image_size - w - 4)
    y = random.randint(4, image_size - h - 4)
    cv2.rectangle(image, (x, y), (x + w, y + h), 255, -1)
    return image, "Rectangle"


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
    center = (random.randint(26, image_size - 26), random.randint(26, image_size - 26))
    axes = (random.randint(14, 28), random.randint(10, 22))
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
    r = random.randint(14, 26)
    cx = random.randint(r + 6, image_size - r - 6)
    cy = random.randint(r + 6, image_size - r - 6)
    pts = _regular_polygon_points(cx, cy, r, 5, random.randint(0, 72))
    cv2.fillPoly(image, [pts], 255)
    return image, "Pentagone"


def draw_random_hexagon(image_size: int):
    image = _blank_image(image_size)
    r = random.randint(12, 20)
    cx = random.randint(r + 6, image_size - r - 6)
    cy = random.randint(r + 6, image_size - r - 6)
    pts = _regular_polygon_points(cx, cy, r, 6, random.randint(0, 30))
    cv2.fillPoly(image, [pts], 255)
    return image, "Hexagone"


DRAWERS = [
    draw_random_circle,
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
    "vertices_coarse",
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
            if random.random() < 0.5:
                image = cv2.bitwise_not(image)
            features = extract_object_features(image)
            if features is None:
                continue
            row = dict(zip(FEATURE_COLUMNS, features.tolist()))
            row["label"] = label
            rows.append(row)

    return pd.DataFrame(rows)


def save_dataset(df: pd.DataFrame, output_csv: str):
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index=False)


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    csv_path = os.path.join(root, "data", "processed", "objects.csv")
    dataset = generate_image_dataset(samples_per_class=350, image_size=96)
    save_dataset(dataset, csv_path)
    print(f"Dataset image genere: {len(dataset)} lignes -> {csv_path}")