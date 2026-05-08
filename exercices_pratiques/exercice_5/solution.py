import cv2
image_path = '../../../images/carre/carre_01.png' # Remplacez par le nom de votre image
# 1. Lire L'image couleur
image_couleur = cv2.imread(image_path)
if image_couleur is not None:
    # 2. Convertir l'image en niveaux de gris
    # Votre code ici
    # 3. Afficher L'image couleur originale
    cv2.imshow('Image Originale', image_couleur)
    # 4. Afficher l'image en niveaux de gris
    # Votre code ici
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Erreur: Impossible de charger l'image à partir de {image_path}")

# CODE AJOUTE POUR CETTE EXERCICE :
# image_gris = cv2.cvtColor(image_couleur, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Image en niveaux de gris', image_gris)

