import numpy as np
# 1. Créer une image 5x5 avec un grand carré central de 1s
# (Représentant une forme simple)
image_forme = np.array([
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 1, 1, 1, 0],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
])

def reconnaitre_forme(image, seuil_pixels):
    # 2. Calculer la somme des pixels
    somme = np.sum(image)
    # 3. Vérifier si la somme dépasse le seuil
    if somme > seuil_pixels:
        return True
    else:
        return False
    
# 4. Définir un seuil (la somme des 1s dans l'exemple est 9)
seuil_pour_grand_carre = 8 # Si plus de 8 pixels sont 'blancs', c'est un grand carré

print("Image de forme (5x5) :")
print(image_forme)

# CODE AJOUTE POUR CETTE EXERCICE :
resultat = reconnaitre_forme(image_forme, seuil_pour_grand_carre)
if resultat:
    print("\nRésultat : Cette forme est un grand carré.")
else:
    print("\nRésultat : Cette forme n'est pas un grand carré.")

