import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ml.generate_image_dataset import generate_test_images


if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    output_dir = os.path.join(project_root, "images")
    generate_test_images(output_dir=output_dir, per_class=8, image_size=256)
    print(f"\nImages de test generees dans: {output_dir}")
