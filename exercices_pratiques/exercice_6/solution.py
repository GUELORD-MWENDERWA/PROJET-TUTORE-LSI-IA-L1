import cv2
image_path = '../../../images/cercle/cercle_01.png' # Remplacez par le nom de votre image
image = cv2.imread(image_path)
if image is not None:
    image_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 1. Appliquer la détection de bord Canny
    edges = cv2.Canny(image_gris, 100, 200)
    cv2.imshow('Image Originale (Gris)', image_gris)
    # 2. Afficher les bords détectés
    cv2.imshow('Bords détectés', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Erreur: Impossible de charger l'image à partir de {image_path}")

