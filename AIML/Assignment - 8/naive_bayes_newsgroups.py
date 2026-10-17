"""Assignment 8: Multinomial Naive Bayes for news-topic classification.

The experiment classifies real discussion posts from four 20 Newsgroups
categories.  It is intentionally a multi-class topic problem rather than
spam detection.
"""

from pathlib import Path
import csv

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


CATEGORIES = [
    "sci.space",
    "rec.sport.hockey",
    "talk.politics.misc",
    "comp.graphics",
]
DISPLAY_NAMES = {
    "sci.space": "Science & Space",
    "rec.sport.hockey": "Hockey",
    "talk.politics.misc": "Politics",
    "comp.graphics": "Computer Graphics",
}
OUTPUT_DIR = Path(__file__).parent
DATASET_FILE = OUTPUT_DIR / "newsgroups_dataset.csv"


def create_local_dataset() -> None:
    """Download the corpus through Python and save a portable local CSV copy."""
    dataset = fetch_20newsgroups(
        subset="all",
        categories=CATEGORIES,
        remove=("headers", "footers", "quotes"),
        shuffle=True,
        random_state=42,
        data_home=OUTPUT_DIR / ".sklearn_data",
    )
    with DATASET_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["text", "label", "category"])
        for text, dataset_label in zip(dataset.data, dataset.target):
            category = dataset.target_names[dataset_label]
            label = CATEGORIES.index(category)
            writer.writerow([text, label, category])
    print(f"LOCAL DATASET CREATED: {DATASET_FILE.name}")


def load_local_dataset():
    """Load the experiment data only from the CSV stored in this folder."""
    if not DATASET_FILE.exists():
        create_local_dataset()

    texts = []
    labels = []
    with DATASET_FILE.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            texts.append(row["text"])
            labels.append(int(row["label"]))
    return texts, labels, CATEGORIES


def build_model() -> Pipeline:
    """Create a reproducible TF-IDF + MultinomialNB pipeline."""
    return Pipeline(
        [
            (
                "tfidf",
                TfidfVectorizer(
                    lowercase=True,
                    stop_words="english",
                    ngram_range=(1, 2),
                    min_df=2,
                    max_df=0.95,
                    sublinear_tf=True,
                ),
            ),
            ("classifier", MultinomialNB(alpha=0.10)),
        ]
    )


def save_confusion_matrix(y_true, y_pred, target_names) -> None:
    matrix = confusion_matrix(y_true, y_pred)
    display_names = [DISPLAY_NAMES[name] for name in target_names]
    figure, axis = plt.subplots(figsize=(8, 6))
    ConfusionMatrixDisplay(
        confusion_matrix=matrix,
        display_labels=display_names,
    ).plot(
        ax=axis,
        cmap="Blues",
        values_format="d",
        xticks_rotation=25,
        colorbar=False,
    )
    axis.set_title("Naive Bayes News-Topic Confusion Matrix")
    figure.tight_layout()
    figure.savefig(OUTPUT_DIR / "viz_naive_bayes_confusion_matrix.svg", dpi=180)
    plt.close(figure)


def save_class_distribution(target, target_names) -> None:
    counts = [sum(label == index for label in target) for index in range(len(target_names))]
    figure, axis = plt.subplots(figsize=(8, 5))
    axis.bar(
        [DISPLAY_NAMES[name] for name in target_names],
        counts,
        color=["#2563eb", "#16a34a", "#f59e0b", "#9333ea"],
    )
    axis.set_title("20 Newsgroups Class Distribution")
    axis.set_ylabel("Number of documents")
    axis.tick_params(axis="x", rotation=18)
    figure.tight_layout()
    figure.savefig(OUTPUT_DIR / "viz_newsgroups_class_distribution.svg", dpi=180)
    plt.close(figure)


def main() -> None:
    texts, labels, target_names = load_local_dataset()
    x_train, x_test, y_train, y_test = train_test_split(
        texts,
        labels,
        test_size=0.25,
        random_state=42,
        stratify=labels,
    )

    model = build_model()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)
    macro_f1 = f1_score(y_test, predictions, average="macro")
    print("DATASET: Local newsgroups_dataset.csv")
    print(f"TOTAL DOCUMENTS: {len(texts)}")
    print(f"TRAIN DOCUMENTS: {len(x_train)}")
    print(f"TEST DOCUMENTS: {len(x_test)}")
    print(f"VOCABULARY SIZE: {len(model.named_steps['tfidf'].vocabulary_)}")
    print(f"ACCURACY: {accuracy:.4f}")
    print(f"MACRO F1-SCORE: {macro_f1:.4f}")
    print("\nCLASSIFICATION REPORT")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=[DISPLAY_NAMES[name] for name in target_names],
            digits=4,
            zero_division=0,
        )
    )

    examples = [
        "The telescope captured a new image of a distant galaxy.",
        "The goaltender made a brilliant save in the third period.",
        "The government announced a new national policy today.",
        "The rendering uses polygons, textures, and a graphics pipeline.",
    ]
    print("SAMPLE PREDICTIONS")
    for text, predicted_class in zip(examples, model.predict(examples)):
        print(f"- {text} -> {DISPLAY_NAMES[target_names[predicted_class]]}")

    save_confusion_matrix(y_test, predictions, target_names)
    save_class_distribution(labels, target_names)
    print("\nSaved visualisations:")
    print("- viz_naive_bayes_confusion_matrix.svg")
    print("- viz_newsgroups_class_distribution.svg")


if __name__ == "__main__":
    main()
