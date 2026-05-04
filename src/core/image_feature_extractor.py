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


def _touches_border(contour, width: int, height: int):
    x, y, w, h = cv2.boundingRect(contour)
    return x <= 1 or y <= 1 or (x + w) >= (width - 1) or (y + h) >= (height - 1)


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
    best_score = -1e9

    for mask in candidates:
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = float(cv2.contourArea(contour))
            if area <= 5.0:
                continue
            perimeter = float(cv2.arcLength(contour, True))
            if perimeter <= 1e-6:
                continue

            area_ratio = area / img_area
            score = area_ratio * 4.0
            if min_area <= area <= max_area:
                score += 2.0
            if _touches_border(contour, w, h):
                score -= 4.0
            circularity = float((4.0 * math.pi * area) / (perimeter * perimeter))
            if circularity < 0.08:
                score -= 2.0

            if score > best_score:
                best = contour
                best_mask = mask
                best_score = score

    return best, best_mask


def _center_mask(mask: np.ndarray):
    """Recentre l'objet principal dans une image de meme taille."""
    if mask is None:
        return None
    ys, xs = np.where(mask > 0)
    if len(xs) == 0 or len(ys) == 0:
        return mask

    min_x, max_x = int(xs.min()), int(xs.max())
    min_y, max_y = int(ys.min()), int(ys.max())
    crop = mask[min_y : max_y + 1, min_x : max_x + 1]

    h, w = mask.shape[:2]
    ch, cw = crop.shape[:2]
    y0 = max((h - ch) // 2, 0)
    x0 = max((w - cw) // 2, 0)

    centered = np.zeros_like(mask)
    centered[y0 : y0 + ch, x0 : x0 + cw] = crop
    return centered


def extract_object_features(image: np.ndarray):
    """Extrait des features geometriques depuis une image binaire d'objet."""
    if image is None:
        return None

    if image.ndim == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()

    contour, selected_mask = _select_object_contour(gray)
    if contour is None:
        return None

    centered_mask = _center_mask(selected_mask)
    if centered_mask is None:
        return None
    contours, _ = cv2.findContours(centered_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None
    contour = max(contours, key=cv2.contourArea)

    area = float(cv2.contourArea(contour))
    if area < 5:
        return None

    perimeter = float(cv2.arcLength(contour, True))
    if perimeter <= 1e-6:
        return None

    x, y, w, h = cv2.boundingRect(contour)
    box_area = float(max(w * h, 1))
    aspect_ratio = float(min(w, h) / max(w, h))
    extent = float(area / (w * h))
    circularity = float((4.0 * math.pi * area) / (perimeter * perimeter))
    circularity = max(0.0, min(circularity, 1.0))

    hull = cv2.convexHull(contour)
    hull_area = float(cv2.contourArea(hull))
    solidity = float(area / hull_area) if hull_area > 1e-6 else 0.0

    approx_fine = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    approx_coarse = cv2.approxPolyDP(contour, 0.05 * perimeter, True)
    approx_mid = cv2.approxPolyDP(contour, 0.03 * perimeter, True)
    vertices_fine = float(len(approx_fine))
    vertices_mid = float(len(approx_mid))
    vertices_coarse = float(len(approx_coarse))

    (_, _), radius = cv2.minEnclosingCircle(contour)
    circle_area = float(math.pi * radius * radius) if radius > 1e-6 else 1.0
    circle_fill = float(area / circle_area)
    area_ratio = float(area / gray.size)
    box_fill = float(area / box_area)

    eccentricity = 0.0
    if len(contour) >= 5:
        (_, _), (ma, mi), _ = cv2.fitEllipse(contour)
        major = float(max(ma, mi))
        minor = float(min(ma, mi))
        if major > 1e-6:
            eccentricity = float(math.sqrt(max(major * major - minor * minor, 0.0)) / major)

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
            vertices_mid,
            vertices_coarse,
            box_fill,
            circle_fill,
            area_ratio,
            eccentricity,
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
    return _center_mask(mask)