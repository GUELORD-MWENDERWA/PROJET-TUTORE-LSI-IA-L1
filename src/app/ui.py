import os
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from pipeline import build_preprocessed_mask, predict_single_image, train_pipeline


class ShapeRecognitionApp(QWidget):
    def __init__(self, project_root):
        super().__init__()
        self.project_root = project_root
        self.model_path = os.path.join(project_root, "models", "object_knn.joblib")
        self.current_image_path = None
        self._build_ui()

    def _build_ui(self):
        self.setWindowTitle("IA - Reconnaissance de formes sur image")
        self.setMinimumSize(920, 640)
        self.setStyleSheet(
            """
            QWidget {
                background-color: #0f172a;
                color: #e2e8f0;
                font-family: Segoe UI;
            }
            QPushButton {
                background-color: #2563eb;
                border: 1px solid #1d4ed8;
                border-radius: 10px;
                padding: 10px 16px;
                font-size: 14px;
                font-weight: 600;
                color: white;
            }
            QPushButton:hover {
                background-color: #3b82f6;
            }
            QPushButton:pressed {
                background-color: #1e40af;
            }
            """
        )

        self.image_label = QLabel("Charge une image pour commencer")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet(
            "border: 2px dashed #38bdf8; background: #020617; color: #cbd5e1; border-radius: 12px;"
        )
        self.image_label.setMinimumSize(640, 480)
        self.mask_label = QLabel("Masque binaire (debug)")
        self.mask_label.setAlignment(Qt.AlignCenter)
        self.mask_label.setStyleSheet(
            "border: 2px dashed #f59e0b; background: #020617; color: #fde68a; border-radius: 12px;"
        )
        self.mask_label.setMinimumSize(640, 220)

        self.status_label = QLabel("Modele non entraine.")
        self.status_label.setStyleSheet("font-size: 14px; color: #93c5fd;")

        self.prediction_label = QLabel("Prediction: -")
        self.prediction_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #22c55e;")

        train_button = QPushButton("Entrainer / Re-entrainer")
        train_button.clicked.connect(self.train_model)

        open_button = QPushButton("Charger une image")
        open_button.clicked.connect(self.open_image)

        predict_button = QPushButton("Predire la forme")
        predict_button.clicked.connect(self.predict_image)
        preprocess_button = QPushButton("Pretraiter image")
        preprocess_button.clicked.connect(self.preprocess_image)

        buttons = QHBoxLayout()
        buttons.addWidget(train_button)
        buttons.addWidget(open_button)
        buttons.addWidget(predict_button)
        buttons.addWidget(preprocess_button)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label, 1)
        layout.addWidget(self.mask_label)
        layout.addLayout(buttons)
        layout.addWidget(self.status_label)
        layout.addWidget(self.prediction_label)
        self.setLayout(layout)

    def train_model(self):
        try:
            model_path, acc = train_pipeline(self.project_root, samples_per_class=300, image_size=96, k=5)
            self.model_path = model_path
            self.status_label.setText(f"Modele pret. Accuracy test: {acc:.3f}")
        except Exception as exc:
            QMessageBox.critical(self, "Erreur entrainement", str(exc))

    def open_image(self):
        image_path, _ = QFileDialog.getOpenFileName(
            self,
            "Choisir une image",
            self.project_root,
            "Images (*.png *.jpg *.jpeg *.bmp)",
        )
        if not image_path:
            return
        self.current_image_path = image_path
        self._display_image(image_path)
        self.prediction_label.setText("Prediction: -")

    def _display_image(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            QMessageBox.warning(self, "Image invalide", "Impossible de lire cette image.")
            return
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        h, w, _ = image.shape
        qimg = QImage(image.data, w, h, 3 * w, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg).scaled(
            self.image_label.width(),
            self.image_label.height(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )
        self.image_label.setPixmap(pixmap)

    def predict_image(self):
        if not os.path.exists(self.model_path):
            QMessageBox.information(self, "Modele manquant", "Entraine d'abord le modele.")
            return
        if not self.current_image_path:
            QMessageBox.information(self, "Image manquante", "Charge d'abord une image.")
            return
        try:
            prediction = predict_single_image(self.model_path, self.current_image_path)
            self.prediction_label.setText(f"Prediction: {prediction}")
        except Exception as exc:
            QMessageBox.critical(self, "Erreur prediction", str(exc))

    def preprocess_image(self):
        if not self.current_image_path:
            QMessageBox.information(self, "Image manquante", "Charge d'abord une image.")
            return
        try:
            mask = build_preprocessed_mask(self.current_image_path)
            h, w = mask.shape
            qimg = QImage(mask.data, w, h, w, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qimg).scaled(
                self.mask_label.width(),
                self.mask_label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            self.mask_label.setPixmap(pixmap)
            self.status_label.setText("Masque binaire mis a jour.")
        except Exception as exc:
            QMessageBox.critical(self, "Erreur pretraitement", str(exc))
