import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import os
import sys

OUTPUT_DIR = Path(__file__).parent
ITEMS_FILE = OUTPUT_DIR / "20191226-items.csv"
REVIEWS_FILE = OUTPUT_DIR / "20191226-reviews.csv"

def load_and_preprocess_data():
    if not ITEMS_FILE.exists() or not REVIEWS_FILE.exists():
        print(f"Error: Dataset files not found in {OUTPUT_DIR}")
        print(f"Please ensure both {ITEMS_FILE.name} and {REVIEWS_FILE.name} are present.")
        sys.exit(1)
        
    print("Loading datasets...")
    items_df = pd.read_csv(ITEMS_FILE)
    reviews_df = pd.read_csv(REVIEWS_FILE)
    
    # Merge on asin to get brand information for each review
    df = pd.merge(reviews_df, items_df[['asin', 'brand']], on='asin', how='inner')
    
    # Drop rows with missing body text or rating
    df = df.dropna(subset=['body', 'rating', 'brand'])
    
    # Define sentiment based on rating (1-5)
    # 4,5 -> Positive (1)
    # 1,2 -> Negative (0)
    # We will exclude 3 (Neutral) for clearer binary classification
    df = df[df['rating'] != 3].copy()
    df['sentiment'] = df['rating'].apply(lambda x: 'Positive' if x > 3 else 'Negative')
    
    return df

def analyze_brands(df, y_true, y_pred):
    df_test = df.copy()
    df_test['predicted_sentiment'] = y_pred
    
    print("\n--- BRAND ANALYSIS ---")
    
    # 1. Which brand has the highest positive sentiment? (Based on predictions)
    brand_sentiments = df_test.groupby('brand')['predicted_sentiment'].value_counts(normalize=True).unstack(fill_value=0)
    
    if 'Positive' in brand_sentiments.columns:
        highest_positive_brand = brand_sentiments['Positive'].idxmax()
        highest_positive_pct = brand_sentiments['Positive'].max() * 100
        print(f"1. Brand with highest positive sentiment: {highest_positive_brand} ({highest_positive_pct:.1f}%)")
    
    # 2. Which brand has the most negative reviews? (Absolute count)
    negative_counts = df_test[df_test['predicted_sentiment'] == 'Negative'].groupby('brand').size()
    if not negative_counts.empty:
        most_negative_brand = negative_counts.idxmax()
        most_negative_count = negative_counts.max()
        print(f"2. Brand with most negative reviews (count): {most_negative_brand} ({most_negative_count} reviews)")
        
    # 3. Which brands have the most complaints? (Can be same as 2, or percentage-wise)
    if 'Negative' in brand_sentiments.columns:
        highest_complaint_brand = brand_sentiments['Negative'].idxmax()
        highest_complaint_pct = brand_sentiments['Negative'].max() * 100
        print(f"3. Brand with highest percentage of negative reviews (complaints): {highest_complaint_brand} ({highest_complaint_pct:.1f}%)")
        
    # 4. Does sentiment agree with star ratings?
    # Since we defined true sentiment from star ratings, we can check accuracy
    accuracy = accuracy_score(y_true, y_pred)
    print(f"4. Does predicted sentiment agree with star ratings? Yes, they agree {accuracy*100:.1f}% of the time.")

def extract_top_negative_words(vectorizer, classifier, n=20):
    feature_names = vectorizer.get_feature_names_out()
    # class 0 is Negative, class 1 is Positive
    neg_class_prob_sorted = classifier.feature_log_prob_[0, :].argsort()[::-1]
    
    top_negative_words = np.take(feature_names, neg_class_prob_sorted[:n])
    print("\n5. Words most associated with negative reviews:")
    print(", ".join(top_negative_words))

def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred, labels=["Negative", "Positive"])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Negative", "Positive"])
    fig, ax = plt.subplots(figsize=(6, 5))
    disp.plot(cmap="Blues", ax=ax, colorbar=False)
    ax.set_title("Sentiment Classification Confusion Matrix")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "viz_sentiment_confusion_matrix.svg", dpi=180)
    plt.close(fig)

def main():
    df = load_and_preprocess_data()
    print(f"Total reviews after preprocessing: {len(df)}")
    
    X = df['body']
    y = df['sentiment']
    
    X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(
        X, y, df.index, test_size=0.25, random_state=42, stratify=y
    )
    
    print("Vectorizing text...")
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10000, ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    print("Training Naive Bayes classifier...")
    classifier = MultinomialNB(alpha=0.1)
    classifier.fit(X_train_vec, y_train)
    
    print("Evaluating model...")
    y_pred = classifier.predict(X_test_vec)
    
    print("\n--- CLASSIFICATION REPORT ---")
    print(classification_report(y_test, y_pred))
    
    # Plot confusion matrix
    plot_confusion_matrix(y_test, y_pred)
    print("Saved confusion matrix visualization.")
    
    # Analysis answering project questions
    df_test_subset = df.loc[indices_test]
    analyze_brands(df_test_subset, y_test, y_pred)
    
    extract_top_negative_words(vectorizer, classifier)

if __name__ == "__main__":
    main()
