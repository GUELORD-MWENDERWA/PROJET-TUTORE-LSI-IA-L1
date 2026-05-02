import argparse
import os
import sys
from PyQt5.QtWidgets import QApplication

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pipeline import predict_single_image, train_pipeline

def main():
    """Lance l'interface PyQt5 ou le mode CLI."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, default=None, help="Chemin d'une image a classifier")
    parser.add_argument("--samples", type=int, default=350, help="Nombre d'echantillons par classe")
    parser.add_argument("--size", type=int, default=96, help="Taille des images synthetiques")
    parser.add_argument("--k", type=int, default=5, help="Nombre de voisins KNN")
    parser.add_argument("--cli", action="store_true", help="Force le mode ligne de commande")
    args = parser.parse_args()

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not args.cli and args.image is None:
        from app.ui import ShapeRecognitionApp

        app = QApplication(sys.argv)
        window = ShapeRecognitionApp(project_root)
        window.show()
        sys.exit(app.exec_())
        return

    model_path, _ = train_pipeline(project_root, args.samples, args.size, args.k)
    if args.image:
        prediction = predict_single_image(model_path, args.image)
        print(f"Prediction pour {args.image}: {prediction}")


if __name__ == "__main__":
    main()