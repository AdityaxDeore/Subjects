"""
AIML Assignment No. 9 - Random Forest Classifier on Iris Dataset
PCCOE - Department of Information Technology
Author: Aditya Chandrajit Deore (PRN: 124B1F116)
Aim: Implement the Bagging technique using the Random Forest algorithm to classify
     the Iris dataset and compare its accuracy with a single Decision Tree model.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# Set seed and working directory
np.random.seed(42)
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(OUTPUT_DIR)

def run_experiment():
    print("=" * 75)
    print(" AIML ASSIGNMENT NO. 9: RANDOM FOREST VS DECISION TREE (IRIS DATASET) ")
    print("=" * 75)

    # 1. Load Dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names

    # Clean feature names for table presentation
    clean_feature_names = [f.replace(" (cm)", "").title() for f in feature_names]

    # Save to local CSV for complete reproducibility
    df = pd.DataFrame(X, columns=clean_feature_names)
    df['Species_ID'] = y
    df['Species_Name'] = [target_names[i] for i in y]
    csv_path = os.path.join(OUTPUT_DIR, "iris_dataset.csv")
    df.to_csv(csv_path, index=False)
    print(f"[OK] Saved local dataset copy to: {csv_path}")
    print(f"    Total Observations: {X.shape[0]}")
    print(f"    Features ({X.shape[1]}): {clean_feature_names}")
    print(f"    Target Classes ({len(target_names)}): {list(target_names)}\n")

    # 2. Train-Test Split (80% Train, 20% Test, Stratified)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"[OK] Dataset partitioned: Train Set = {X_train.shape[0]} samples, Test Set = {X_test.shape[0]} samples (Balanced: 10 per class)\n")

    # 3. Model 1: Standalone Single Decision Tree
    dt_model = DecisionTreeClassifier(random_state=42)
    dt_model.fit(X_train, y_train)
    y_pred_dt = dt_model.predict(X_test)

    dt_acc = accuracy_score(y_test, y_pred_dt)
    dt_prec = precision_score(y_test, y_pred_dt, average='macro')
    dt_rec = recall_score(y_test, y_pred_dt, average='macro')
    dt_f1 = f1_score(y_test, y_pred_dt, average='macro')
    dt_cm = confusion_matrix(y_test, y_pred_dt)

    # 4. Model 2: Random Forest Ensemble (Bagging with 100 Trees & sqrt feature subspacing)
    rf_model = RandomForestClassifier(
        n_estimators=100,
        max_features='sqrt',
        bootstrap=True,
        oob_score=True,
        random_state=42
    )
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)

    rf_acc = accuracy_score(y_test, y_pred_rf)
    rf_prec = precision_score(y_test, y_pred_rf, average='macro')
    rf_rec = recall_score(y_test, y_pred_rf, average='macro')
    rf_f1 = f1_score(y_test, y_pred_rf, average='macro')
    rf_cm = confusion_matrix(y_test, y_pred_rf)
    rf_oob = rf_model.oob_score_

    # 5. Print Comparative Benchmark Summary
    print("-" * 75)
    print(" MODEL PERFORMANCE BENCHMARK COMPARISON ")
    print("-" * 75)
    print(f"{'Performance Metric':<24} {'Single Decision Tree':<24} {'Random Forest (Ensemble)'}")
    print("-" * 75)
    print(f"{'Accuracy':<24} {dt_acc * 100:>6.2f}%{'':<17} {rf_acc * 100:>6.2f}%")
    print(f"{'Macro Precision':<24} {dt_prec * 100:>6.2f}%{'':<17} {rf_prec * 100:>6.2f}%")
    print(f"{'Macro Recall':<24} {dt_rec * 100:>6.2f}%{'':<17} {rf_rec * 100:>6.2f}%")
    print(f"{'Macro F1-Score':<24} {dt_f1 * 100:>6.2f}%{'':<17} {rf_f1 * 100:>6.2f}%")
    print(f"{'Out-Of-Bag (OOB) Score':<24} {'N/A (No Bootstrap)':<24} {rf_oob * 100:>6.2f}%")
    print(f"{'Ensemble Base Estimators':<24} {'1 Single Tree':<24} {'100 Decision Trees'}")
    print("-" * 75)
    print(f"Observation: Random Forest achieves {rf_acc*100:.2f}% test accuracy with de-correlated bagging.")
    print("-" * 75 + "\n")

    # 6. Classification Reports
    print("DECISION TREE CLASSIFICATION REPORT:")
    print(classification_report(y_test, y_pred_dt, target_names=target_names))

    print("RANDOM FOREST CLASSIFICATION REPORT:")
    print(classification_report(y_test, y_pred_rf, target_names=target_names))

    # 7. Confusion Matrices
    print("DECISION TREE CONFUSION MATRIX:")
    print(dt_cm)
    print("\nRANDOM FOREST CONFUSION MATRIX:")
    print(rf_cm)
    print()

    # 8. Feature Importance from Random Forest
    importances = rf_model.feature_importances_
    feat_df = pd.DataFrame({
        'Feature': clean_feature_names,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)
    print("RANDOM FOREST GINI FEATURE IMPORTANCES:")
    for _, row in feat_df.iterrows():
        print(f"  - {row['Feature']:<16} : {row['Importance']*100:>6.2f}%")
    print()

    # 9. Majority Voting Demonstration on Sample Test Instances
    print("-" * 75)
    print(" ENSEMBLE MAJORITY VOTING DEMONSTRATION (Sample Test Observations) ")
    print("-" * 75)
    sample_indices = [0, 10, 20]  # One from each class region in test set
    voting_records = []

    for idx in sample_indices:
        sample_x = X_test[idx].reshape(1, -1)
        actual_class = target_names[y_test[idx]]
        dt_pred = target_names[dt_model.predict(sample_x)[0]]
        
        # Get individual tree votes from the 100 trees
        tree_preds = [tree.predict(sample_x)[0] for tree in rf_model.estimators_]
        vote_counts = {target_names[c]: tree_preds.count(c) for c in range(3)}
        rf_pred = target_names[rf_model.predict(sample_x)[0]]
        
        voting_records.append({
            'Test_Index': idx,
            'Features': X_test[idx].tolist(),
            'Actual': actual_class,
            'DT_Pred': dt_pred,
            'Votes': vote_counts,
            'RF_Pred': rf_pred
        })

        print(f"Test Sample #{idx} (Features: {X_test[idx]}):")
        print(f"  Actual Class        : {actual_class.upper()}")
        print(f"  Decision Tree Pred  : {dt_pred}")
        print(f"  Tree Vote Breakdown : Setosa: {vote_counts['setosa']} votes | Versicolor: {vote_counts['versicolor']} votes | Virginica: {vote_counts['virginica']} votes")
        print(f"  Random Forest Final : {rf_pred.upper()} (Majority Vote)\n")

    # 10. Generate High-Quality Visualizations
    generate_visualizations(dt_acc, rf_acc, dt_prec, rf_prec, dt_rec, rf_rec, dt_f1, rf_f1,
                            dt_cm, rf_cm, feat_df, voting_records, target_names)

    print("[OK] All visualization graphics generated successfully in SVG and PNG formats.")
    print("=" * 75)


def generate_visualizations(dt_acc, rf_acc, dt_prec, rf_prec, dt_rec, rf_rec, dt_f1, rf_f1,
                            dt_cm, rf_cm, feat_df, voting_records, target_names):
    # Set styling
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['axes.edgecolor'] = '#94a3b8'
    plt.rcParams['axes.linewidth'] = 0.9

    # -------------------------------------------------------------
    # Visualization 1: Metric Benchmark Comparison (Bar Chart)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    dt_scores = [dt_acc * 100, dt_prec * 100, dt_rec * 100, dt_f1 * 100]
    rf_scores = [rf_acc * 100, rf_prec * 100, rf_rec * 100, rf_f1 * 100]

    x = np.arange(len(metrics))
    width = 0.32

    rects1 = ax.bar(x - width/2, dt_scores, width, label='Single Decision Tree', color='#f59e0b', edgecolor='#d97706')
    rects2 = ax.bar(x + width/2, rf_scores, width, label='Random Forest (100 Trees)', color='#10b981', edgecolor='#059669')

    ax.set_ylabel('Score (%)', fontsize=11, fontweight='bold', color='#1e293b')
    ax.set_title('Performance Comparison: Single Decision Tree vs. Random Forest Ensemble', fontsize=12, fontweight='bold', pad=12, color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=10.5, fontweight='bold')
    ax.set_ylim(85, 103)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.legend(frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', fontsize=10)

    # Attach score labels on top of bars
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.1f}%',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points",
                        ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#1e293b')

    autolabel(rects1)
    autolabel(rects2)

    plt.tight_layout()
    plt.savefig('viz_model_comparison.svg')
    plt.savefig('viz_model_comparison.png')
    plt.close()

    # -------------------------------------------------------------
    # Visualization 2: Side-by-Side Confusion Matrices
    # -------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.2), dpi=300)
    cms = [(dt_cm, 'Single Decision Tree', axes[0], plt.cm.Oranges),
           (rf_cm, 'Random Forest (100 Trees)', axes[1], plt.cm.Greens)]

    for cm_data, title, cax, cmap in cms:
        im = cax.imshow(cm_data, interpolation='nearest', cmap=cmap)
        cax.set_title(f'Confusion Matrix\n{title}', fontsize=11, fontweight='bold', pad=10, color='#0f172a')
        
        tick_marks = np.arange(len(target_names))
        cax.set_xticks(tick_marks)
        cax.set_yticks(tick_marks)
        cax.set_xticklabels([t.capitalize() for t in target_names], fontsize=9.5, fontweight='bold')
        cax.set_yticklabels([t.capitalize() for t in target_names], fontsize=9.5, fontweight='bold')
        cax.set_xlabel('Predicted Label', fontsize=10, fontweight='bold', color='#1e293b', labelpad=6)
        cax.set_ylabel('True Label', fontsize=10, fontweight='bold', color='#1e293b', labelpad=6)

        thresh = cm_data.max() / 2.
        for i in range(cm_data.shape[0]):
            for j in range(cm_data.shape[1]):
                val = cm_data[i, j]
                cax.text(j, i, format(val, 'd'),
                         ha="center", va="center", fontsize=11, fontweight='bold',
                         color="white" if val > thresh else "black")

    plt.tight_layout()
    plt.savefig('viz_confusion_matrices.svg')
    plt.savefig('viz_confusion_matrices.png')
    plt.close()

    # -------------------------------------------------------------
    # Visualization 3: Gini Feature Importance (Horizontal Bar)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8, 3.8), dpi=300)
    feat_df_sorted = feat_df.sort_values(by='Importance', ascending=True)
    bars = ax.barh(feat_df_sorted['Feature'], feat_df_sorted['Importance'] * 100, color='#3b82f6', edgecolor='#1d4ed8', height=0.55)

    ax.set_xlabel('Relative Importance (Gini Impurity Reduction %)', fontsize=10, fontweight='bold', color='#1e293b')
    ax.set_title('Random Forest Feature Importance on Iris Attributes', fontsize=12, fontweight='bold', pad=12, color='#0f172a')
    ax.set_xlim(0, max(feat_df['Importance'] * 100) + 8)
    ax.grid(axis='x', linestyle='--', alpha=0.5)

    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.8, bar.get_y() + bar.get_height()/2, f'{width:.2f}%',
                ha='left', va='center', fontsize=9.5, fontweight='bold', color='#1e293b')

    plt.tight_layout()
    plt.savefig('viz_feature_importance.svg')
    plt.savefig('viz_feature_importance.png')
    plt.close()

    # -------------------------------------------------------------
    # Visualization 4: Majority Voting Distribution on Sample Test Instances
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 4.2), dpi=300)
    sample_labels = [f"Sample #{r['Test_Index']}\n(Actual: {r['Actual'].capitalize()})" for r in voting_records]
    x = np.arange(len(sample_labels))
    bar_w = 0.25

    setosa_votes = [r['Votes']['setosa'] for r in voting_records]
    versicolor_votes = [r['Votes']['versicolor'] for r in voting_records]
    virginica_votes = [r['Votes']['virginica'] for r in voting_records]

    r1 = ax.bar(x - bar_w, setosa_votes, bar_w, label='Setosa Votes', color='#60a5fa', edgecolor='#2563eb')
    r2 = ax.bar(x, versicolor_votes, bar_w, label='Versicolor Votes', color='#34d399', edgecolor='#059669')
    r3 = ax.bar(x + bar_w, virginica_votes, bar_w, label='Virginica Votes', color='#f472b6', edgecolor='#db2777')

    ax.set_ylabel('Number of Tree Votes (out of 100 Trees)', fontsize=10.5, fontweight='bold', color='#1e293b')
    ax.set_title('Bagging Ensemble Demonstration: Tree Vote Distribution Across 100 Estimators', fontsize=11.5, fontweight='bold', pad=12, color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(sample_labels, fontsize=9.5, fontweight='bold')
    ax.set_ylim(0, 115)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.legend(frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', fontsize=9.5)

    def attach_vote_labels(rects):
        for rect in rects:
            h = rect.get_height()
            if h > 0:
                ax.annotate(f'{h}',
                            xy=(rect.get_x() + rect.get_width() / 2, h),
                            xytext=(0, 2), textcoords="offset points",
                            ha='center', va='bottom', fontsize=9, fontweight='bold')

    attach_vote_labels(r1)
    attach_vote_labels(r2)
    attach_vote_labels(r3)

    plt.tight_layout()
    plt.savefig('viz_majority_voting_demo.svg')
    plt.savefig('viz_majority_voting_demo.png')
    plt.close()


if __name__ == "__main__":
    run_experiment()
