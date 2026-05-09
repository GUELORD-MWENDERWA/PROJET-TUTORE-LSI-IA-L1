# Exercice 4 : Entrée/Sortie d'images et interface graphique OpenCV

## Objectif pédagogique

Maîtriser les protocoles d'entrée/sortie d'images numériques et comprendre l'architecture d'affichage graphique dans le contexte de la vision par ordinateur appliquée.

## Concepts mathématiques et informatiques fondamentaux

### Représentation numérique des images

- **Codage matriciel** : Image comme fonction discrète $I: \mathbb{Z}^2 \rightarrow \mathbb{R}^3$ (couleurs RGB)
- **Formats de fichiers** : Encodage compressé (JPEG, PNG) vs représentation matricielle brute
- **Espaces colorimétriques** : Conversion entre RGB, BGR, HSV selon les applications

### Architecture d'affichage

- **Fenêtrage graphique** : Gestion des buffers d'affichage et des événements utilisateur
- **Boucle d'événements** : Mécanisme de polling pour l'interaction homme-machine
- **Gestion mémoire** : Allocation/désallocation des ressources graphiques

## Description technique

Cet exercice implémente le pipeline complet d'E/S visuelle :

1. **Chargement de fichier** : Lecture et décodage d'un fichier image compressé
2. **Validation des données** : Vérification de l'intégrité de la matrice chargée
3. **Affichage graphique** : Rendu visuel avec interface utilisateur interactive
4. **Gestion des ressources** : Libération propre de la mémoire graphique

## Implémentation et architecture

```python
import cv2

# Spécification du chemin d'accès au fichier image
chemin_image = '../../../images/carre/carre_01.png'

# Opération d'E/S : chargement synchrone du fichier
image = cv2.imread(chemin_image)

# Validation de l'opération de chargement
if image is not None:
    # Création d'une fenêtre d'affichage nommée
    cv2.imshow('Visualisation OpenCV', image)

    # Boucle d'attente d'événement : blocage jusqu'à interaction utilisateur
    cv2.waitKey(0)

    # Libération des ressources graphiques
    cv2.destroyAllWindows()
else:
    print(f"Erreur E/S: Impossible de charger {chemin_image}")
```

## Analyse technique

### Gestion d'erreurs et robustesse

- **Test de nullité** : Vérification de l'échec du chargement (fichier inexistant, corrompu)
- **Messages diagnostiques** : Retour d'information pour débogage
- **Graceful degradation** : Comportement contrôlé en cas d'erreur

### Architecture événementielle

- **Modèle synchrone** : Attente active d'un événement clavier
- **Code de retour** : Valeur entière représentant la touche pressée
- **Timeout configurable** : Possibilité d'attente limitée dans le temps

### Optimisations mémoire

- **Lazy loading** : Chargement à la demande uniquement
- **Resource management** : Libération explicite des fenêtres graphiques
- **Memory mapping** : Accès direct aux données sans copie intermédiaire

## Applications en IA et vision par ordinateur

Ces primitives d'E/S constituent la base de tout système de vision :

- **Acquisition de données** : Interface avec capteurs et caméras
- **Validation de datasets** : Vérification de l'intégrité des données d'entraînement
- **Débogage visuel** : Inspection intermédiaire des résultats de traitement
- **Interfaces homme-machine** : Intégration dans des applications interactives

## Exécution et validation

```bash
python solution.py
```

**Comportement attendu :**
Ouverture d'une fenêtre graphique affichant l'image carrée, fermeture sur pression d'une touche quelconque.

## Concepts transversaux

- **Programmation système** : Gestion des ressources et des E/S
- **Interface homme-machine** : Conception d'interactions utilisateur
- **Architecture logicielle** : Séparation des préoccupations (chargement/affichage)
  else:
  print(f"Erreur: Impossible de charger l'image à partir de {image_path}")

````

## Notions importantes

- **cv2.imread()** : Retourne `None` si le fichier n'existe pas ou est corrompu
- **cv2.imshow()** : Crée une fenêtre avec le titre spécifié
- **cv2.waitKey(0)** : Attend indéfiniment une pression de touche
- **cv2.destroyAllWindows()** : Ferme toutes les fenêtres OpenCV ouvertes

## Applications pratiques

Ces fonctions de base sont essentielles pour :

- Le débogage de pipelines de traitement d'images
- La visualisation intermédiaire des résultats
- L'inspection manuelle des images chargées

## Exécution

```bash
python solution.py
````

## Résultat attendu

Ouvre une fenêtre affichant l'image carrée du projet. Appuyez sur une touche pour fermer.
