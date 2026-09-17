import json
from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from data import TRAINING_DATA

MODEL_DIR = Path(__file__).parent / "model"
VECTORIZER_PATH = MODEL_DIR / "vectorizer.joblib"
CLASSIFIER_PATH = MODEL_DIR / "classifier.joblib"
CLASSES_PATH = MODEL_DIR / "classes.json"

DEFAULT_MARGIN_THRESHOLD = 0.15 


def train_and_save():
    texts, labels = zip(*TRAINING_DATA)

    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X = vectorizer.fit_transform(texts)

    clf = LogisticRegression(C=5.0, max_iter=1000)
    clf.fit(X, labels)

    MODEL_DIR.mkdir(exist_ok=True)

    joblib.dump(vectorizer, VECTORIZER_PATH)
    joblib.dump(clf, CLASSIFIER_PATH)
    CLASSES_PATH.write_text(json.dumps(sorted(set(labels))))

    print(f"trained on {len(texts)} examples, {len(set(labels))} classes.")
    print(f"Saved to {MODEL_DIR}/")
    return vectorizer, clf


def load():
    if not (VECTORIZER_PATH.exists() and CLASSIFIER_PATH.exists()):
        raise FileNotFoundError(
            "no saved model found. `python classifier.py` "
        )
    vectorizer = joblib.load(VECTORIZER_PATH)
    clf = joblib.load(CLASSIFIER_PATH)
    return vectorizer, clf


class IntentClassifier:
    def __init__(self, margin_threshold: float = DEFAULT_MARGIN_THRESHOLD):
        self.vectorizer, self.clf = load()
        self.threshold = margin_threshold

    def predict(self, text: str):

        X = self.vectorizer.transform([text])

        probs = self.clf.predict_proba(X)[0]
        ranked_idx = probs.argsort()[::-1]

        top_idx, second_idx = ranked_idx[0], ranked_idx[1]
        top_conf = probs[top_idx]
        margin = top_conf - probs[second_idx]

        if margin < self.threshold:
            return None, top_conf
        return self.clf.classes_[top_idx], top_conf


if __name__ == "__main__":
    train_and_save()
