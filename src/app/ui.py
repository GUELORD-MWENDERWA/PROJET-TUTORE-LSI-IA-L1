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

from pipeline import predict_single_image_with_confidence, train_pipeline


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

        buttons = QHBoxLayout()
        buttons.addWidget(train_button)
        buttons.addWidget(open_button)
        buttons.addWidget(predict_button)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label, 1)
        layout.addLayout(buttons)
        layout.addWidget(self.status_label)
        layout.addWidget(self.prediction_label)
        self.setLayout(layout)

    def train_model(self):
        try:
            model_path, acc = train_pipeline(self.project_root, samples_per_class=500, image_size=128, k=8)
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
            prediction, confidence = predict_single_image_with_confidence(self.model_path, self.current_image_path)
            self.prediction_label.setText(f"Prediction: {prediction} ({confidence * 100:.1f}%)")
        except Exception as exc:
            QMessageBox.critical(self, "Erreur prediction", str(exc))
