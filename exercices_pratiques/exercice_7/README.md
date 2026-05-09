# Exercice 7 : Visualisation scientifique et conversion colorimétrique Matplotlib

## Objectif pédagogique

Maîtriser les techniques de visualisation scientifique d'images et comprendre les conversions entre espaces colorimétriques dans le contexte de l'analyse de données visuelles.

## Concepts mathématiques et informatiques fondamentaux

### Visualisation matricielle

- **Fonction d'affichage** : Représentation graphique de matrices 2D/3D comme images
- **Échelle de couleurs** : Mapping des valeurs numériques vers l'espace perceptuel
- **Normalisation automatique** : Ajustement des plages dynamiques pour l'affichage

### Gestion des espaces colorimétriques

- **Convention OpenCV** : Format BGR (Bleu-Vert-Rouge) pour compatibilité historique
- **Convention Matplotlib** : Format RGB (Rouge-Vert-Bleu) standard scientifique
- **Transformation bijective** : Permutation circulaire des canaux : $(B,G,R) \leftrightarrow (R,G,B)$

## Description technique

Cet exercice implémente l'interface entre traitement d'images et visualisation scientifique :

1. **Chargement brut** : Acquisition d'image dans le format natif d'OpenCV
2. **Conversion colorimétrique** : Adaptation aux conventions de Matplotlib
3. **Rendu graphique** : Affichage avec contrôles interactifs et annotations

## Implémentation et architecture

```python
import cv2
import matplotlib.pyplot as plt

# Acquisition de l'image source (format BGR d'OpenCV)
chemin_image = '../../../images/triangle/triangle_01.png'
image_bgr = cv2.imread(chemin_image)

if image_bgr is not None:
    # Conversion colorimétrique BGR → RGB pour conformité Matplotlib
    # Transformation : (B,G,R) ↦ (R,G,B) par permutation circulaire
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    # Configuration de la figure Matplotlib
    plt.figure(figsize=(8, 6))  # Dimensions en pouces
    plt.imshow(image_rgb)       # Affichage matriciel avec colormap par défaut
    plt.title('Visualisation Matplotlib - Espace RGB')
    plt.axis('off')             # Suppression des graduations pour affichage propre
    plt.show()                  # Rendu interactif avec boucle d'événements
else:
    print(f"Echec du chargement: {chemin_image}")
```

## Analyse technique

### Architecture de Matplotlib

- **Figure** : Conteneur principal pour les éléments graphiques
- **Axes** : Système de coordonnées pour le positionnement
- **Artist** : Objets graphiques (lignes, textes, images) dans la figure

### Gestion de la couleur

- **RGB normalisé** : Valeurs dans $[0,1]$ pour l'affichage (conversion automatique depuis $[0,255]$)
- **Alpha channel** : Transparence optionnelle pour compositions complexes
- **Colorspace perceptuel** : Espace sRGB pour rendu fidèle à la perception humaine

### Optimisations d'affichage

- **Interpolation** : Rééchantillonnage automatique pour adaptation à la résolution d'écran
- **Antialiasing** : Lissage des contours pour qualité visuelle
- **Backend selection** : Choix automatique du moteur graphique optimal

## Applications en analyse de données

Matplotlib constitue l'outil standard pour la visualisation en IA :

- **Exploration de données** : Inspection visuelle des datasets d'images
- **Débogage d'algorithmes** : Visualisation des étapes intermédiaires
- **Publication scientifique** : Génération de figures pour articles et rapports
- **Interfaces interactives** : Intégration dans des notebooks Jupyter

## Exécution et validation

```bash
python solution.py
```

**Comportement attendu :**
Ouverture d'une fenêtre Matplotlib interactive affichant l'image avec les couleurs correctes.

## Concepts transversaux

- **Représentation graphique** : Traduction mathématique vers visualisation
- **Interface homme-machine** : Conception d'environnements interactifs
- **Standards de couleur** : Gestion des conventions dans les pipelines de traitement
  else:
  print(f"Erreur: Impossible de charger l'image à partir de {image_path}")

````

## Notions importantes

- **Format BGR d'OpenCV** : Bleu-Vert-Rouge (convention historique)
- **Format RGB standard** : Rouge-Vert-Bleu (convention Matplotlib)
- **plt.axis('off')** : Supprime les graduations des axes pour un affichage propre
- **plt.show()** : Affiche la figure dans une fenêtre interactive

## Applications pratiques

Matplotlib est préféré pour :

- Les environnements de développement interactifs (Jupyter notebooks)
- La visualisation scientifique avec annotations
- L'intégration dans des rapports et publications
- Le débogage avec des sous-graphiques multiples

## Exécution

```bash
python solution.py
````

## Résultat attendu

Ouvre une fenêtre Matplotlib affichant l'image avec les couleurs correctes et sans axes.
