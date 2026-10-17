# Assignment 8 Design

Assignment 8 uses the PCCOE editable HTML report format from the previous AIML assignments.

- Problem: four-class news-topic classification, not spam detection.
- Dataset source: scikit-learn 20 Newsgroups, downloaded through Python.
- Dataset copy: `newsgroups_dataset.csv` is generated in this folder and loaded for the experiment.
- Visual outputs: `viz_newsgroups_class_distribution.svg` and `viz_naive_bayes_confusion_matrix.svg` are saved in this folder and embedded by the output HTML.
- Features: English stop-word removal, TF-IDF unigrams and bigrams.
- Classifier: Multinomial Naive Bayes with `alpha=0.10`.
- Evaluation: accuracy, per-class precision/recall/F1, macro F1, and confusion matrix.
- Reproducibility: fixed `random_state=42`, stratified 75:25 split.
