import numpy as np
# 1. Créez une "image" aléatoire 10x10
grande_image = np.random.randint(0, 256, size=(10, 10))
print("Grande image (10×10): ")
print(grande_image)
# 2. Extrayez la sous-section centrale 5x5
sous_image = grande_image[2:7, 2:7]
print("\nSous-image centrale (5x5):")
print(sous_image)
