import cv2
# Assurez-vous que "mon_image.jpg' existe dans le même dossier ou fournissez le chemin
image_path = '../../../images/carre/carre_01.png' # Remplacez par le nom de votre image
# 1. Lire l'image
image = cv2.imread(image_path)
# 2. Vérifier si l'image a été chargée avec succès
if image is not None:
    # 3. Afficher l'image dans une fenêtre
    cv2.imshow('Image OpenCV', image)
    # 4. Attendre qu'une touche soit pressée et fermer les fenêtres
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Erreur: Impossible de charger l'image à partir de {image_path}")

