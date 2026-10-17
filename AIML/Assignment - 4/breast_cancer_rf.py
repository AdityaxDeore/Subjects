#!/usr/bin/env python3
"""
================================================================================
PCCOE Lab Assignment No. 7 (Assignment - 4)
Title       : Breast Cancer Diagnosis Prediction Using Bagging with Random Forest
Course      : Artificial Intelligence & Machine Learning (AIML Lab)
Student     : Aditya Chandrajit Deore
PRN         : 124B1F116 | Batch: B3
Department  : Department of Information Technology
Institution : Pimpri Chinchwad College of Engineering (PCCOE, Pune)
================================================================================
Core Concepts:
- Ensemble Learning via Bootstrap Aggregating (Bagging)
- De-correlated Decision Trees with Random Feature Subspacing (mtry = sqrt(p))
- Predefined Wisconsin Diagnostic Breast Cancer Dataset (scikit-learn)
- Performance Evaluation: Accuracy, Precision, Recall, F1-Score, Confusion Matrix, ROC-AUC
- Clinical Feature Importance & Out-of-Bag (OOB) Generalization Estimation
================================================================================
"""

import sys
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_curve, auc
)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
DATASET_CSV = BASE_DIR / "dataset.csv"

def export_dataset_to_csv(data) -> pd.DataFrame:
    """Exports Scikit-Learn's predefined Wisconsin Diagnostic Breast Cancer dataset to dataset.csv."""
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df["Diagnosis"] = [data.target_names[t].capitalize() for t in data.target]
    df["Target"] = data.target
    df.insert(0, "Sample_ID", [f"WDBC_{i+1:03d}" for i in range(len(df))])
    df.to_csv(DATASET_CSV, index=False)
    print(f">> Predefined Wisconsin Dataset saved to: {DATASET_CSV.name} ({len(df)} records)")
    return df

def generate_visualisations(model, feature_names, class_names, X_test, y_test, y_pred, y_proba):
    """Generates 4 high-resolution, vivid, colorful academic charts."""
    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'axes.spines.top': False,
        'axes.spines.right': False,
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
        'axes.edgecolor': '#334155',
        'xtick.color': '#1e293b',
        'ytick.color': '#1e293b',
        'axes.labelcolor': '#0f172a',
        'text.color': '#0f172a',
    })

    # 1. COLORFUL CONFUSION MATRIX (Vivid YlGnBu / Teal palette)
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(8.2, 6.4), dpi=200)
    sns.heatmap(cm, annot=True, fmt='d', cmap='YlGnBu', cbar=True,
                xticklabels=class_names, yticklabels=class_names, ax=ax,
                linewidths=2.0, linecolor='#ffffff',
                annot_kws={"size": 15, "fontweight": "bold", "color": "#0f172a"})
    ax.set_title("Random Forest Confusion Matrix — Test Evaluation", fontsize=13, fontweight='bold', pad=14, color='#0f172a')
    ax.set_xlabel("Predicted Diagnosis", fontsize=11, labelpad=8, fontweight='bold', color='#1e293b')
    ax.set_ylabel("Actual Ground Truth", fontsize=11, labelpad=8, fontweight='bold', color='#1e293b')
    plt.xticks(fontsize=10.5, fontweight='600')
    plt.yticks(fontsize=10.5, fontweight='600')
    plt.tight_layout()
    plt.savefig(BASE_DIR / "viz_confusion_matrix.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Saved: viz_confusion_matrix.png")

    # 2. TOP-12 FEATURE IMPORTANCE (Vibrant gradient / rainbow bar chart)
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1][:12]
    top_features = [feature_names[i] for i in indices]
    top_importances = importances[indices]

    palette = ['#e11d48', '#2563eb', '#059669', '#d97706', '#7c3aed', '#0891b2', 
               '#ea580c', '#4f46e5', '#16a34a', '#db2777', '#ca8a04', '#0284c7']
    bar_colors = palette[:len(top_features)]

    fig, ax = plt.subplots(figsize=(10.5, 6.2), dpi=200)
    bars = ax.barh(range(len(top_features)), top_importances[::-1], color=bar_colors[::-1], 
                   edgecolor='#1e293b', linewidth=0.8, height=0.68)
    ax.set_yticks(range(len(top_features)))
    ax.set_yticklabels(top_features[::-1], fontsize=10, fontweight='600')
    ax.set_xlabel("Mean Impurity Reduction (Gini Feature Importance)", fontsize=11, labelpad=8, fontweight='bold', color='#1e293b')
    ax.set_title("Random Forest Top-12 Diagnostic Biomarkers", fontsize=13, fontweight='bold', pad=14, color='#0f172a')
    for bar in bars:
        w = bar.get_width()
        if w > 0.005:
            ax.text(w + 0.003, bar.get_y() + bar.get_height()/2, f"{w:.4f}", 
                    va='center', fontsize=9.5, fontweight='bold', color='#0f172a')
    ax.set_xlim(0, max(top_importances) * 1.18)
    ax.xaxis.grid(True, linestyle='--', alpha=0.5, color='#94a3b8')
    plt.tight_layout()
    plt.savefig(BASE_DIR / "viz_feature_importance.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Saved: viz_feature_importance.png")

    # 3. ENSEMBLE TREE ESTIMATOR CONVERGENCE & OOB ERROR
    tree_range = range(10, 160, 10)
    test_errors = []
    for n in tree_range:
        rf_temp = RandomForestClassifier(n_estimators=n, random_state=42)
        rf_temp.fit(X_test, y_test)
        test_errors.append((1 - rf_temp.score(X_test, y_test)) * 100)

    fig, ax = plt.subplots(figsize=(10.5, 5.5), dpi=200)
    ax.plot(tree_range, test_errors, marker='o', color='#2563eb', linewidth=2.4, 
            markersize=6, markerfacecolor='#e11d48', markeredgecolor='#9f1239', label='Ensemble Generalization Error (%)')
    ax.set_title("Bagging Variance Reduction: Error Convergence vs Number of Trees", fontsize=13, fontweight='bold', pad=14, color='#0f172a')
    ax.set_xlabel("Number of Estimators (Decision Trees)", fontsize=11, labelpad=8, fontweight='bold', color='#1e293b')
    ax.set_ylabel("Error Rate (%)", fontsize=11, labelpad=8, fontweight='bold', color='#1e293b')
    ax.grid(True, linestyle='--', alpha=0.5, color='#94a3b8')
    ax.legend(loc='upper right', fontsize=10.5, framealpha=0.95, edgecolor='#cbd5e1')
    plt.tight_layout()
    plt.savefig(BASE_DIR / "viz_bagging_convergence.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Saved: viz_bagging_convergence.png")

    # 4. ROC CURVE (RECEIVER OPERATING CHARACTERISTIC)
    # y=0 is Malignant, y=1 is Benign. ROC for Malignant (class 0 probability is 1 - p(1))
    fpr, tpr, _ = roc_curve(y_test, y_proba[:, 1])
    roc_auc = auc(fpr, tpr)

    fig, ax = plt.subplots(figsize=(8.5, 6.2), dpi=200)
    ax.plot(fpr, tpr, color='#059669', lw=2.5, label=f'Random Forest ROC (AUC = {roc_auc:.4f})')
    ax.plot([0, 1], [0, 1], color='#ef4444', lw=1.8, linestyle='--', label='Random Chance (AUC = 0.5000)')
    ax.fill_between(fpr, tpr, color='#d1fae5', alpha=0.45)
    ax.set_xlim([-0.02, 1.02])
    ax.set_ylim([-0.02, 1.05])
    ax.set_xlabel('False Positive Rate (1 - Specificity)', fontsize=11, fontweight='bold', color='#1e293b')
    ax.set_ylabel('True Positive Rate (Sensitivity / Recall)', fontsize=11, fontweight='bold', color='#1e293b')
    ax.set_title('Receiver Operating Characteristic (ROC) Diagnostic Curve', fontsize=13, fontweight='bold', pad=14, color='#0f172a')
    ax.legend(loc="lower right", fontsize=10.5, framealpha=0.98, edgecolor='#cbd5e1')
    ax.grid(True, linestyle='--', alpha=0.5, color='#94a3b8')
    plt.tight_layout()
    plt.savefig(BASE_DIR / "viz_roc_curve.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Saved: viz_roc_curve.png")

def main():
    if sys.stdout.encoding.lower() != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    print("Initializing PCCOE CancerGuard-RF Diagnostic Engine...")
    print("=" * 86)
    print(" PCCOE CANCERGUARD-RF: BREAST TUMOR DIAGNOSIS ENSEMBLE SYSTEM")
    print(" Department of Information Technology | Pimpri Chinchwad College of Engineering")
    print("=" * 86)

    # 1. Load predefined Breast Cancer Wisconsin Dataset
    data = load_breast_cancer()
    df = export_dataset_to_csv(data)

    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target
    class_names = [name.capitalize() for name in data.target_names]

    # 2. Stratified Train-Test Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    print(f"Dataset Samples Profiled     : {len(df)} patient cell nuclei records")
    print(f"Diagnostic Biomarker Features: {X.shape[1]} morphological attributes")
    print(f"Target Diagnostic Classes    : 0 -> {class_names[0]} (Tumor), 1 -> {class_names[1]} (Healthy/Non-cancerous)")
    print("-" * 86)
    print(f"Training Set Size            : {len(X_train)} patient records (80%)")
    print(f"Testing Set Size             : {len(X_test)} patient records (20%)")
    print("-" * 86)

    # 3. Model Training with Random Forest (Bagging + Feature Subspacing)
    print("Training Random Forest Classifier (n_estimators=100, max_features='sqrt', oob_score=True)...")
    model = RandomForestClassifier(
        n_estimators=100,
        criterion="gini",
        max_features="sqrt",
        oob_score=True,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    # 4. Predictions & Evaluation
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)

    acc = accuracy_score(y_test, y_pred) * 100
    prec = precision_score(y_test, y_pred, average="weighted") * 100
    rec = recall_score(y_test, y_pred, average="weighted") * 100
    f1 = f1_score(y_test, y_pred, average="weighted") * 100
    oob = model.oob_score_ * 100

    print("RANDOM FOREST ENSEMBLE PERFORMANCE EVALUATION:")
    print(f">> Model Accuracy            : {acc:.2f} %")
    print(f">> Out-of-Bag (OOB) Score    : {oob:.2f} % (Unbiased Generalized Validation)")
    print(f">> Weighted Precision        : {prec:.2f} %")
    print(f">> Weighted Recall           : {rec:.2f} %")
    print(f">> Weighted F1-Score         : {f1:.2f} %")
    print("-" * 86)

    print("CLASSIFICATION REPORT PER TUMOR CATEGORY:")
    print(classification_report(y_test, y_pred, target_names=class_names, digits=4))
    print("-" * 86)

    print("CONFUSION MATRIX:")
    cm = confusion_matrix(y_test, y_pred)
    header = f"{'Actual \\ Pred':<18}" + "".join([f"{c:>14}" for c in class_names])
    print(header)
    for i, row_name in enumerate(class_names):
        row_str = f"{row_name:<18}" + "".join([f"{cm[i][j]:>14}" for j in range(len(class_names))])
        print(row_str)
    print("-" * 86)

    # Top Features
    importance_series = pd.Series(model.feature_importances_, index=data.feature_names).sort_values(ascending=False)
    print("TOP 10 CLINICAL BIOMARKERS (GINI IMPURITY IMPORTANCE):")
    for rank, (feat, score) in enumerate(importance_series.head(10).items(), 1):
        print(f" {rank:02d}. {feat:<28} : {score:.4f} ({score*100:.2f}%)")
    print("-" * 86)

    # 5. Clinical Inference Demonstration
    print("CLINICAL INFERENCE & ONCOLOGICAL DECISION RECOMMENDATIONS:")
    sample_indices = [3, 12, 25, 48, 70]
    for idx in sample_indices:
        x_patient = X_test.iloc[[idx]]
        true_diag = class_names[y_test[idx]]
        pred_diag = class_names[model.predict(x_patient)[0]]
        confidence = np.max(model.predict_proba(x_patient)) * 100
        print(f">> Patient WDBC_{idx+1:03d} | Actual: {true_diag:<10} | Predicted: [{pred_diag.upper()}] (Confidence: {confidence:.1f}%)")
        if pred_diag == "Malignant":
            print("   Action: URGENT ONCOLOGY REFERRAL: Immediate histopathology biopsy and staging scan indicated.")
        else:
            print("   Action: ROUTINE MONITORING: Benign cytology; schedule periodic screening in 6 months.")
        print()

    # 6. Benchmark: Random Forest (Bagging) vs Single Decision Tree
    from sklearn.tree import DecisionTreeClassifier
    dt_model = DecisionTreeClassifier(random_state=42)
    dt_model.fit(X_train, y_train)
    y_pred_dt = dt_model.predict(X_test)
    acc_dt = accuracy_score(y_test, y_pred_dt) * 100
    prec_dt = precision_score(y_test, y_pred_dt, average="weighted") * 100
    rec_dt = recall_score(y_test, y_pred_dt, average="weighted") * 100
    f1_dt = f1_score(y_test, y_pred_dt, average="weighted") * 100

    print("-" * 86)
    print("BENCHMARK COMPARISON: RANDOM FOREST (BAGGING) VS SINGLE DECISION TREE:")
    print("-" * 86)
    print(f"{'Model Architecture':<28} {'Accuracy':<12} {'Precision':<12} {'Recall':<12} {'F1-Score':<12}")
    print(f"{'Single Decision Tree':<28} {acc_dt:<11.2f}% {prec_dt:<11.2f}% {rec_dt:<11.2f}% {f1_dt:<11.2f}%")
    print(f"{'Random Forest (Bagging)':<28} {acc:<11.2f}% {prec:<11.2f}% {rec:<11.2f}% {f1:<11.2f}%")
    print(f"{'Performance Delta (Gain)':<28} {f'+{acc-acc_dt:.2f}%':<12} {f'+{prec-prec_dt:.2f}%':<12} {f'+{rec-rec_dt:.2f}%':<12} {f'+{f1-f1_dt:.2f}%':<12}")
    print("-" * 86)

    print("=" * 86)
    print("Generating Academic Diagnostic Visualisations...")
    generate_visualisations(model, data.feature_names, class_names, X_test, y_test, y_pred, y_proba)
    print("All diagnostic charts successfully saved.")
    print("=" * 86)

if __name__ == "__main__":
    main()
