import numpy as np
# 1. Créez une "image" aléatoire 10x10
grande_image = np.random.randint(0, 256, size=(10, 10))
print("Grande image (10×10): ")
print(grande_image)
# 2. Extrayez la sous-section centrale 5x5
# Votre code ici
print("\nSous-image centrale (5x5):")
# Votre code ici

# CODE AJOUTE POUR CETTE EXERCICE :
sous_image = grande_image[2:7, 2:7]
print(sous_image)
