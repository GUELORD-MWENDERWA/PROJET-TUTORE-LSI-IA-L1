import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


class ObjectKNNClassifier:
    """Classifieur scikit-learn robuste (StandardScaler + RandomForest)."""

    def __init__(self, k=5):
        n_estimators = max(200, int(k) * 40)
        self.pipeline = Pipeline(
            [
                ("scaler", StandardScaler()),
                (
                    "rf",
                    RandomForestClassifier(
                        n_estimators=n_estimators,
                        random_state=42,
                        class_weight="balanced_subsample",
                        n_jobs=-1,
                    ),
                ),
            ]
        )

    def train(self, X, y):
        self.pipeline.fit(X, y)

    def predict(self, x):
        return self.pipeline.predict([x])[0]

    def predict_batch(self, X):
        return self.pipeline.predict(X)

    def predict_proba(self, x):
        return self.pipeline.predict_proba([x])[0]

    def save(self, path):
        joblib.dump(self.pipeline, path)

    def load(self, path):
        self.pipeline = joblib.load(path)
        return self


def load_dataset(path):
    df = pd.read_csv(path)
    if "label" not in df.columns:
        raise ValueError("Colonne 'label' manquante dans le dataset")
    if df.empty:
        raise ValueError("Dataset vide")
    X = df.drop("label", axis=1).values
    y = df["label"].values
    return X, y


def train_and_evaluate(X, y, test_size=0.25, random_state=42, k=5):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    model = ObjectKNNClassifier(k=k)
    model.train(X_train, y_train)
    y_pred = model.predict_batch(X_test)
    return {
        "model": model,
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "classification_report": classification_report(y_test, y_pred),
        "confusion_matrix": confusion_matrix(y_test, y_pred),
        "labels": sorted(set(y)),
    }