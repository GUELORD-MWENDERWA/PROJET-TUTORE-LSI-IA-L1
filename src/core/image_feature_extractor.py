import math
import cv2
import numpy as np


def preprocess_object_mask(image: np.ndarray):
    """Construit un masque binaire robuste (fond clair ou sombre)."""
    if image is None:
        return None
    if image.ndim == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()

    _, base = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    masks = [base, cv2.bitwise_not(base)]
    kernel = np.ones((3, 3), np.uint8)
    masks = [cv2.morphologyEx(m, cv2.MORPH_OPEN, kernel) for m in masks]
    masks = [cv2.morphologyEx(m, cv2.MORPH_CLOSE, kernel) for m in masks]
    return gray, masks


def _select_object_contour(gray: np.ndarray):
    """Trouve le meilleur contour objet en gerant fond clair/sombre."""
    prep = preprocess_object_mask(gray)
    if prep is None:
        return None, None
    _, candidates = prep

    h, w = gray.shape[:2]
    img_area = float(h * w)
    min_area = img_area * 0.01
    max_area = img_area * 0.90

    best = None
    best_mask = None
    best_area = 0.0
    fallback = None
    fallback_mask = None
    fallback_area = 0.0

    for mask in candidates:
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = float(cv2.contourArea(contour))
            if area <= fallback_area:
                continue
            fallback = contour
            fallback_mask = mask
            fallback_area = area
            if min_area <= area <= max_area and area > best_area:
                best = contour
                best_mask = mask
                best_area = area

    if best is not None:
        return best, best_mask
    return fallback, fallback_mask


def extract_object_features(image: np.ndarray):
    """Extrait des features geometriques depuis une image binaire d'objet."""
    if image is None:
        return None

    if image.ndim == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()

    contour, _ = _select_object_contour(gray)
    if contour is None:
        return None

    area = float(cv2.contourArea(contour))
    if area < 5:
        return None

    perimeter = float(cv2.arcLength(contour, True))
    if perimeter <= 1e-6:
        return None

    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = float(min(w, h) / max(w, h))
    extent = float(area / (w * h))
    circularity = float((4.0 * math.pi * area) / (perimeter * perimeter))
    circularity = max(0.0, min(circularity, 1.0))

    hull = cv2.convexHull(contour)
    hull_area = float(cv2.contourArea(hull))
    solidity = float(area / hull_area) if hull_area > 1e-6 else 0.0

    approx_fine = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    approx_coarse = cv2.approxPolyDP(contour, 0.05 * perimeter, True)
    vertices_fine = float(len(approx_fine))
    vertices_coarse = float(len(approx_coarse))
    moments = cv2.moments(contour)
    hu = cv2.HuMoments(moments).flatten()
    hu_log = [-np.sign(v) * np.log10(max(abs(v), 1e-12)) for v in hu]

    return np.array(
        [
            float(w),
            float(h),
            aspect_ratio,
            circularity,
            extent,
            solidity,
            perimeter,
            area,
            vertices_fine,
            vertices_coarse,
            float(hu_log[0]),
            float(hu_log[1]),
            float(hu_log[2]),
            float(hu_log[3]),
        ],
        dtype=np.float32,
    )


def preprocess_mask_for_debug(image: np.ndarray):
    """Retourne le meilleur masque binaire pour affichage debug UI."""
    if image is None:
        return None
    if image.ndim == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()
    _, mask = _select_object_contour(gray)
    return mask    