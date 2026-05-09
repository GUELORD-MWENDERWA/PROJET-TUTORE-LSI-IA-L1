from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
# Données des caractéristiques (Largeur, Hauteur) et labels (0: carré, 1: rectangle)
X = [[18, 10], [5, 5], [12, 10], [7, 15], [8, 8], [15, 7], [6, 12], [9, 9]]
y = [1, 0, 1, 1, 0, 1, 1, 0]
# 1. Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# 2. Instancier le classifieur K-NN (par exemple, avec 3 voisins)
model = KNeighborsClassifier(n_neighbors=3)
# 3. Entraîner le modèle
model.fit(X_train, y_train)
# 4. Faire une prédiction pour un nouvel objet (ex: largeur 6, hauteur 6)
nouvel_objet = [[6, 6]]
prediction = model.predict(nouvel_objet)
print(f"La prédiction pour l'objet {nouvel_objet} est: {prediction[0]} (0: carré, 1: rectangle)")

