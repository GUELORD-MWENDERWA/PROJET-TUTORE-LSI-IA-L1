# Code de départ (à compléter)
import numpy as np
# 1. Créez un tableau 3x3 de zéros
# image_simple = # Votre code ici
# 2. Modifiez le pixel central à 255
# Votre code ici

# CODE AJOUTE POUR CETTE EXERCICE :
image_simple = np.zeros((3, 3), dtype=np.uint8)
# 2. Modifiez le pixel central à 255
image_simple[1, 1] = 255

print("Image initiale (3x3) :")
print(np.zeros((3, 3), dtype=np.uint8))
print("\nImage après modification du pixel central à 255 :")
print(image_simple)
