import cv2
import matplotlib.pyplot as plt
image_path = '../../../images/triangle/triangle_01.png' # Remplacez par le nom de votre image
image = cv2.imread(image_path)
if image is not None:
    # 1. Convertir l'image de BGR à RGB pour Matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # 2. Afficher l'image avec Matplotlib
    plt.imshow(image_rgb)
    plt.axis('off') # Pour masquer les axes
    plt.show()
else:
    print(f"Erreur: Impossible de charger l'image à partir de {image_path}")

