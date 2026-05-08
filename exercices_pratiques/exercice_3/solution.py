import numpy as np
# 1. Créez une image 5x5 avec des valeurs de pixels aléatoires
image_couleur_simulee = np.random.randint(0, 256, size=(5, 5))
print("Image simulée originale:")
print(image_couleur_simulee)
# 2. Créez une image binaire (1 si > 127, 0 sinon)
# Votre code ici
print("\nImage binaire (seuillage):")
# Votre code ici

# CODE AJOUTE POUR CETTE EXERCICE :
image_binaire = (image_couleur_simulee > 127).astype(np.uint8)
print(image_binaire)
