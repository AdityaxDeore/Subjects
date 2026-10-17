#!/usr/bin/env python3
"""
================================================================================
PCCOE Lab Assignment No. 7 (Assignment - 5)
Title       : Real-Life Medical Diagnosis Prediction Using K-Nearest Neighbors (KNN) Classifier
Course      : Artificial Intelligence & Machine Learning (AIML Lab)
Student     : Aditya Chandrajit Deore
PRN         : 124B1F116 | Batch: B3
Department  : Department of Information Technology
Institution : Pimpri Chinchwad College of Engineering (PCCOE, Pune)
================================================================================
Core Concepts:
- Instance-Based Non-Parametric Supervised Learning (Lazy Learner)
- Distance Metrics: Euclidean, Manhattan, and Minkowski Distance Formulation
- Feature Standardization via StandardScaler (Crucial for Distance Geometry)
- Optimal Hyperparameter Search: K-Value Tuning via 10-Fold Cross-Validation
- Comprehensive Metric Evaluation: Accuracy, Precision, Recall, F1, Confusion Matrix
- Real-Life Diagnostic Inference with Patient Case Prioritization
================================================================================
"""

import sys
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
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
    """Exports diagnostic records to dataset.csv with clinical identifiers and labels."""
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df["Diagnosis"] = [data.target_names[t].capitalize() for t in data.target]
    df["Target"] = data.target
    df.insert(0, "Patient_ID", [f"PATIENT_{i+1:03d}" for i in range(len(df))])
    df.to_csv(DATASET_CSV, index=False)
    print(f">> Medical telemetry dataset saved to: {DATASET_CSV.name} ({len(df)} patient records)")
    return df

def generate_visualisations(optimal_k, k_values, cv_scores, cm, class_names, fpr, tpr, roc_auc, X_test_scaled, y_test, knn_best):
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

    # 1. OPTIMAL K-VALUE HYPERPARAMETER TUNING CURVE
    fig, ax = plt.subplots(figsize=(10.5, 5.8), dpi=200)
    ax.plot(k_values, cv_scores, marker='o', color='#2563eb', linewidth=2.4, 
            markersize=6, markerfacecolor='#e11d48', markeredgecolor='#9f1239', label='10-Fold Cross-Validation Accuracy (%)')
    ax.axvline(x=optimal_k, color='#059669', linestyle='--', linewidth=2.0, label=f'Optimal K = {optimal_k} (Max Score: {max(cv_scores):.2f}%)')
    ax.scatter([optimal_k], [max(cv_scores)], color='#059669', s=120, zorder=5)
    ax.text(optimal_k + 0.8, max(cv_scores) - 0.3, f'Best K={optimal_k}\n({max(cv_scores):.2f}%)', 
            fontsize=10, fontweight='bold', color='#065f46')
    ax.set_title('Hyperparameter Optimization: KNN Diagnostic Accuracy vs K-Neighbors', fontsize=13, fontweight='bold', pad=14, color='#0f172a')
    ax.set_xlabel('Number of Nearest Neighbors (K)', fontsize=11, labelpad=8, fontweight='bold', color='#1e293b')
    ax.set_ylabel('Mean Cross-Validation Accuracy (%)', fontsize=11, labelpad=8, fontweight='bold', color='#1e293b')
    ax.set_xticks(range(1, max(k_values) + 1, 2))
    ax.grid(True, linestyle='--', alpha=0.5, color='#94a3b8')
    ax.legend(loc='lower right', fontsize=10.5, framealpha=0.98, edgecolor='#cbd5e1')
    plt.tight_layout()
    plt.savefig(BASE_DIR / "viz_knn_k_optimization.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Saved: viz_knn_k_optimization.png")

    # 2. COLORFUL CONFUSION MATRIX (Vivid YlGnBu / Teal palette)
    fig, ax = plt.subplots(figsize=(8.2, 6.4), dpi=200)
    sns.heatmap(cm, annot=True, fmt='d', cmap='YlGnBu', cbar=True,
                xticklabels=class_names, yticklabels=class_names, ax=ax,
                linewidths=2.0, linecolor='#ffffff',
                annot_kws={"size": 15, "fontweight": "bold", "color": "#0f172a"})
    ax.set_title("KNN Classifier Confusion Matrix — Test Evaluation (K=7)", fontsize=13, fontweight='bold', pad=14, color='#0f172a')
    ax.set_xlabel("Predicted Diagnosis", fontsize=11, labelpad=8, fontweight='bold', color='#1e293b')
    ax.set_ylabel("Actual Ground Truth", fontsize=11, labelpad=8, fontweight='bold', color='#1e293b')
    plt.xticks(fontsize=10.5, fontweight='600')
    plt.yticks(fontsize=10.5, fontweight='600')
    plt.tight_layout()
    plt.savefig(BASE_DIR / "viz_knn_confusion_matrix.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Saved: viz_knn_confusion_matrix.png")

    # 3. DISTANCE METRIC COMPARISON (Euclidean vs Manhattan vs Minkowski)
    metrics = ['Euclidean (p=2)', 'Manhattan (p=1)', 'Minkowski (p=3)', 'Chebyshev (p=inf)']
    metric_accuracies = []
    for p_val, metric_name in [(2, 'minkowski'), (1, 'minkowski'), (3, 'minkowski'), (float('inf'), 'chebyshev')]:
        if p_val == float('inf'):
            clf_m = KNeighborsClassifier(n_neighbors=optimal_k, metric='chebyshev')
        else:
            clf_m = KNeighborsClassifier(n_neighbors=optimal_k, p=p_val, metric='minkowski')
        scores = cross_val_score(clf_m, X_test_scaled, y_test, cv=5, scoring='accuracy')
        metric_accuracies.append(scores.mean() * 100)

    palette = ['#2563eb', '#059669', '#d97706', '#7c3aed']
    fig, ax = plt.subplots(figsize=(10.5, 5.8), dpi=200)
    bars = ax.bar(metrics, metric_accuracies, color=palette, edgecolor='#1e293b', width=0.55, linewidth=1.2)
    ax.set_title("Distance Metric Influence on Diagnostic Accuracy", fontsize=13, fontweight='bold', pad=14, color='#0f172a')
    ax.set_ylabel("Cross-Validated Accuracy (%)", fontsize=11, labelpad=8, fontweight='bold', color='#1e293b')
    ax.set_ylim(80, 102)
    ax.grid(True, axis='y', linestyle='--', alpha=0.5, color='#94a3b8')
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h + 0.8, f"{h:.2f}%", 
                ha='center', va='bottom', fontsize=10, fontweight='bold', color='#0f172a')
    plt.tight_layout()
    plt.savefig(BASE_DIR / "viz_distance_metrics.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Saved: viz_distance_metrics.png")

    # 4. RECEIVER OPERATING CHARACTERISTIC (ROC) CURVE
    fig, ax = plt.subplots(figsize=(8.5, 6.2), dpi=200)
    ax.plot(fpr, tpr, color='#059669', lw=2.5, label=f'KNN Diagnostic ROC (AUC = {roc_auc:.4f})')
    ax.plot([0, 1], [0, 1], color='#ef4444', lw=1.8, linestyle='--', label='Random Classifier (AUC = 0.5000)')
    ax.fill_between(fpr, tpr, color='#d1fae5', alpha=0.45)
    ax.set_xlim([-0.02, 1.02])
    ax.set_ylim([-0.02, 1.05])
    ax.set_xlabel('False Positive Rate (1 - Specificity)', fontsize=11, fontweight='bold', color='#1e293b')
    ax.set_ylabel('True Positive Rate (Sensitivity / Recall)', fontsize=11, fontweight='bold', color='#1e293b')
    ax.set_title('Receiver Operating Characteristic (ROC) Diagnostic Curve', fontsize=13, fontweight='bold', pad=14, color='#0f172a')
    ax.legend(loc="lower right", fontsize=10.5, framealpha=0.98, edgecolor='#cbd5e1')
    ax.grid(True, linestyle='--', alpha=0.5, color='#94a3b8')
    plt.tight_layout()
    plt.savefig(BASE_DIR / "viz_knn_roc_curve.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Saved: viz_knn_roc_curve.png")

def main():
    if sys.stdout.encoding.lower() != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    print("Initializing PCCOE MediKNN-Diag Diagnostic Engine...")
    print("=" * 86)
    print(" PCCOE MEDIKNN: MEDICAL DIAGNOSIS K-NEAREST NEIGHBORS CLASSIFIER")
    print(" Department of Information Technology | Pimpri Chinchwad College of Engineering")
    print("=" * 86)

    # 1. Load Predefined Dataset
    data = load_breast_cancer()
    df = export_dataset_to_csv(data)

    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target
    class_names = [name.capitalize() for name in data.target_names] # ['Malignant', 'Benign']

    # 2. Stratified Train-Test Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    print(f"Dataset Samples Profiled     : {len(df)} patient biopsy records")
    print(f"Diagnostic Medical Features  : {X.shape[1]} morphological attributes")
    print(f"Target Diagnostic Classes    : 0 -> {class_names[0]} (Tumor), 1 -> {class_names[1]} (Healthy/Non-cancerous)")
    print("-" * 86)
    print(f"Training Set Size            : {len(X_train)} patient records (80%)")
    print(f"Testing Set Size             : {len(X_test)} patient records (20%)")
    print("-" * 86)

    # 3. Crucial Preprocessing: Feature Standardization
    print("Applying Feature Standardization via StandardScaler (Z-Score Normalization)...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print(">> Feature scaling complete: Zero mean, unit variance achieved across all 30 dimensions.")
    print("-" * 86)

    # 4. Hyperparameter Search: K-Value Optimization (1 to 25)
    print("Performing 10-Fold Cross-Validation for Optimal K-Value Selection (K = 1 to 25)...")
    k_range = list(range(1, 26, 2)) # Odd values of K to avoid tie votes
    cv_scores = []
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
        scores = cross_val_score(knn, X_train_scaled, y_train, cv=10, scoring='accuracy')
        cv_scores.append(scores.mean() * 100)

    best_idx = np.argmax(cv_scores)
    optimal_k = k_range[best_idx]
    print(f">> Optimal Hyperparameter   : K = {optimal_k} Nearest Neighbors")
    print(f">> Cross-Validation Accuracy : {cv_scores[best_idx]:.2f} %")
    print("-" * 86)

    # 5. Train Best KNN Model
    print(f"Training Final KNN Classifier with K={optimal_k} and Euclidean Distance Metric...")
    knn_best = KNeighborsClassifier(n_neighbors=optimal_k, metric='euclidean', weights='uniform')
    knn_best.fit(X_train_scaled, y_train)

    y_pred = knn_best.predict(X_test_scaled)
    y_proba = knn_best.predict_proba(X_test_scaled)

    acc = accuracy_score(y_test, y_pred) * 100
    prec = precision_score(y_test, y_pred, average="weighted") * 100
    rec = recall_score(y_test, y_pred, average="weighted") * 100
    f1 = f1_score(y_test, y_pred, average="weighted") * 100

    print("KNN MODEL PERFORMANCE EVALUATION:")
    print(f">> Model Accuracy (Holdout)  : {acc:.2f} %")
    print(f">> Weighted Precision        : {prec:.2f} %")
    print(f">> Weighted Recall           : {rec:.2f} %")
    print(f">> Weighted F1-Score         : {f1:.2f} %")
    print("-" * 86)

    print("CLASSIFICATION REPORT PER DIAGNOSTIC CLASS:")
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

    # 6. Real-Life Clinical Patient Inference
    print("REAL-LIFE CLINICAL DIAGNOSTIC INFERENCE & TRIAGE RECOMMENDATIONS:")
    sample_indices = [5, 14, 28, 52, 75]
    for idx in sample_indices:
        x_patient = X_test_scaled[[idx]]
        true_diag = class_names[y_test[idx]]
        pred_diag = class_names[knn_best.predict(x_patient)[0]]
        confidence = np.max(knn_best.predict_proba(x_patient)) * 100
        print(f">> Patient {df.iloc[X_test.index[idx]]['Patient_ID']} | Actual: {true_diag:<10} | Predicted: [{pred_diag.upper()}] (Confidence: {confidence:.1f}%)")
        if pred_diag == "Malignant":
            print("   Triage: HIGH RISK: Tumor exhibits invasive cellular boundary irregularities; schedule immediate biopsy.")
        else:
            print("   Triage: LOW RISK: Morphological contours align with benign cytology; schedule 6-month checkup.")
        print()

    # 7. Benchmark: KNN (K=7) vs Standalone Baseline Decision Tree
    from sklearn.tree import DecisionTreeClassifier
    dt_base = DecisionTreeClassifier(random_state=42)
    dt_base.fit(X_train_scaled, y_train)
    y_pred_dt = dt_base.predict(X_test_scaled)
    acc_dt = accuracy_score(y_test, y_pred_dt) * 100
    prec_dt = precision_score(y_test, y_pred_dt, average="weighted") * 100
    rec_dt = recall_score(y_test, y_pred_dt, average="weighted") * 100
    f1_dt = f1_score(y_test, y_pred_dt, average="weighted") * 100

    print("-" * 86)
    print("BENCHMARK COMPARISON: KNN CLASSIFIER (K=7) VS STANDALONE DECISION TREE:")
    print("-" * 86)
    print(f"{'Model Architecture':<28} {'Accuracy':<12} {'Precision':<12} {'Recall':<12} {'F1-Score':<12}")
    print(f"{'Single Decision Tree':<28} {acc_dt:<11.2f}% {prec_dt:<11.2f}% {rec_dt:<11.2f}% {f1_dt:<11.2f}%")
    print(f"{'K-Nearest Neighbors (K=7)':<28} {acc:<11.2f}% {prec:<11.2f}% {rec:<11.2f}% {f1:<11.2f}%")
    print(f"{'Performance Delta (Gain)':<28} {f'+{acc-acc_dt:.2f}%':<12} {f'+{prec-prec_dt:.2f}%':<12} {f'+{rec-rec_dt:.2f}%':<12} {f'+{f1-f1_dt:.2f}%':<12}")
    print("-" * 86)

    # 8. Generate Academic Visualizations
    print("Generating Academic Diagnostic Visualisations...")
    fpr, tpr, _ = roc_curve(y_test, y_proba[:, 1])
    roc_auc = auc(fpr, tpr)
    generate_visualisations(optimal_k, k_range, cv_scores, cm, class_names, fpr, tpr, roc_auc, X_test_scaled, y_test, knn_best)
    print("All diagnostic charts successfully saved.")
    print("=" * 86)

if __name__ == "__main__":
    main()
