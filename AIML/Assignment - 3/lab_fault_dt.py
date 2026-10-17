#!/usr/bin/env python3
"""
================================================================================
PCCOE LabFault-DT: Computer Lab Fault Detection and Diagnosis Model
Assignment No. 6 (Index No. 3): Decision Tree Classification
================================================================================
Student    : Aditya Chandrajit Deore
PRN        : 124B1F116 | Batch: B3
Department : Information Technology
College    : Pimpri Chinchwad College of Engineering (PCCOE, Pune)
Course     : Artificial Intelligence & Machine Learning (AIML Lab)
================================================================================
"""

import sys
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "dataset.csv"

def generate_synthetic_lab_dataset(n_samples: int = 400, random_state: int = 42) -> pd.DataFrame:
    """
    Generates a realistic, logically consistent dataset for computer laboratory fault diagnosis.
    Target Classes:
      0: No_Fault (Normal)
      1: Hardware_Fault (High temp, fan failed, high CPU, crashes)
      2: Software_Fault (Excessive RAM, OS unstable, error spikes, leaks)
      3: Network_Fault (Link down, high latency, packet drops)
      4: Storage_Fault (Degraded disk health, high disk I/O, slow response, boot failures)
    """
    np.random.seed(random_state)
    records = []
    
    samples_per_class = n_samples // 5
    
    # Class 0: No_Fault (Normal Healthy Operation)
    for i in range(samples_per_class):
        records.append({
            "Boot_Status": 1,
            "CPU_Temperature": int(np.clip(np.random.normal(45, 5), 35, 60)),
            "CPU_Usage": int(np.clip(np.random.normal(35, 12), 10, 65)),
            "RAM_Usage": int(np.clip(np.random.normal(45, 12), 20, 70)),
            "Disk_Health": int(np.clip(np.random.normal(94, 4), 85, 100)),
            "Disk_Usage": int(np.clip(np.random.normal(45, 12), 15, 75)),
            "Network_Status": 1,
            "Network_Latency": int(np.clip(np.random.normal(12, 4), 2, 28)),
            "Packet_Loss": round(float(np.clip(np.random.exponential(0.2), 0.0, 1.2)), 1),
            "Fan_Status": 1,
            "Error_Count": int(np.clip(np.random.poisson(1), 0, 4)),
            "Crash_Count": 0,
            "Response_Time": round(float(np.clip(np.random.normal(0.8, 0.2), 0.3, 1.5)), 1),
            "OS_Status": 1,
            "Power_Status": 1,
            "Fault_Type": "No_Fault"
        })
        
    # Class 1: Hardware_Fault (Thermal / Fan / CPU Stress / Hard Crashes)
    for i in range(samples_per_class):
        fan = np.random.choice([0, 1], p=[0.75, 0.25])
        temp = int(np.clip(np.random.normal(84, 6), 74, 98)) if fan == 0 else int(np.clip(np.random.normal(78, 5), 70, 92))
        records.append({
            "Boot_Status": int(np.random.choice([1, 0], p=[0.85, 0.15])),
            "CPU_Temperature": temp,
            "CPU_Usage": int(np.clip(np.random.normal(88, 7), 72, 99)),
            "RAM_Usage": int(np.clip(np.random.normal(65, 15), 35, 90)),
            "Disk_Health": int(np.clip(np.random.normal(88, 8), 70, 99)),
            "Disk_Usage": int(np.clip(np.random.normal(55, 15), 20, 85)),
            "Network_Status": 1,
            "Network_Latency": int(np.clip(np.random.normal(18, 6), 5, 40)),
            "Packet_Loss": round(float(np.clip(np.random.exponential(0.5), 0.0, 2.5)), 1),
            "Fan_Status": fan,
            "Error_Count": int(np.clip(np.random.normal(9, 3), 4, 18)),
            "Crash_Count": int(np.clip(np.random.poisson(3) + 1, 1, 7)),
            "Response_Time": round(float(np.clip(np.random.normal(2.8, 0.6), 1.6, 4.5)), 1),
            "OS_Status": int(np.random.choice([1, 0], p=[0.70, 0.30])),
            "Power_Status": int(np.random.choice([1, 0], p=[0.85, 0.15])),
            "Fault_Type": "Hardware_Fault"
        })

    # Class 2: Software_Fault (Memory Leaks / OS Instability / Application Faults)
    for i in range(samples_per_class):
        records.append({
            "Boot_Status": 1,
            "CPU_Temperature": int(np.clip(np.random.normal(58, 8), 45, 75)),
            "CPU_Usage": int(np.clip(np.random.normal(68, 14), 40, 92)),
            "RAM_Usage": int(np.clip(np.random.normal(92, 4), 84, 99)),
            "Disk_Health": int(np.clip(np.random.normal(91, 5), 80, 100)),
            "Disk_Usage": int(np.clip(np.random.normal(60, 12), 30, 85)),
            "Network_Status": 1,
            "Network_Latency": int(np.clip(np.random.normal(16, 5), 6, 35)),
            "Packet_Loss": round(float(np.clip(np.random.exponential(0.3), 0.0, 1.8)), 1),
            "Fan_Status": 1,
            "Error_Count": int(np.clip(np.random.normal(16, 4), 8, 28)),
            "Crash_Count": int(np.clip(np.random.poisson(3) + 1, 1, 6)),
            "Response_Time": round(float(np.clip(np.random.normal(3.6, 0.7), 2.1, 5.5)), 1),
            "OS_Status": 0,
            "Power_Status": 1,
            "Fault_Type": "Software_Fault"
        })

    # Class 3: Network_Fault (Interface Down / Latency Spike / Dropped Packets)
    for i in range(samples_per_class):
        net_status = np.random.choice([0, 1], p=[0.65, 0.35])
        latency = int(np.clip(np.random.normal(260, 60), 120, 500)) if net_status == 1 else 999
        loss = round(float(np.clip(np.random.normal(14.5, 5.0), 5.0, 35.0)), 1) if net_status == 1 else 100.0
        records.append({
            "Boot_Status": 1,
            "CPU_Temperature": int(np.clip(np.random.normal(48, 6), 38, 62)),
            "CPU_Usage": int(np.clip(np.random.normal(38, 10), 15, 60)),
            "RAM_Usage": int(np.clip(np.random.normal(48, 12), 25, 70)),
            "Disk_Health": int(np.clip(np.random.normal(92, 5), 80, 100)),
            "Disk_Usage": int(np.clip(np.random.normal(46, 12), 15, 75)),
            "Network_Status": net_status,
            "Network_Latency": latency,
            "Packet_Loss": loss,
            "Fan_Status": 1,
            "Error_Count": int(np.clip(np.random.poisson(3), 0, 8)),
            "Crash_Count": 0,
            "Response_Time": round(float(np.clip(np.random.normal(1.2, 0.4), 0.5, 2.5)), 1),
            "OS_Status": 1,
            "Power_Status": 1,
            "Fault_Type": "Network_Fault"
        })

    # Class 4: Storage_Fault (Bad Sectors / Disk Thrashing / Extreme I/O Latency)
    for i in range(samples_per_class):
        records.append({
            "Boot_Status": int(np.random.choice([1, 0], p=[0.60, 0.40])),
            "CPU_Temperature": int(np.clip(np.random.normal(54, 7), 42, 70)),
            "CPU_Usage": int(np.clip(np.random.normal(55, 15), 25, 85)),
            "RAM_Usage": int(np.clip(np.random.normal(58, 14), 30, 85)),
            "Disk_Health": int(np.clip(np.random.normal(32, 8), 10, 48)),
            "Disk_Usage": int(np.clip(np.random.normal(93, 4), 82, 100)),
            "Network_Status": 1,
            "Network_Latency": int(np.clip(np.random.normal(15, 5), 5, 30)),
            "Packet_Loss": round(float(np.clip(np.random.exponential(0.3), 0.0, 1.5)), 1),
            "Fan_Status": 1,
            "Error_Count": int(np.clip(np.random.normal(11, 3), 4, 20)),
            "Crash_Count": int(np.clip(np.random.poisson(2), 0, 5)),
            "Response_Time": round(float(np.clip(np.random.normal(4.2, 0.8), 2.5, 6.8)), 1),
            "OS_Status": int(np.random.choice([1, 0], p=[0.55, 0.45])),
            "Power_Status": 1,
            "Fault_Type": "Storage_Fault"
        })

    df = pd.DataFrame(records)
    # Shuffle dataset
    df = df.sample(frac=1.0, random_state=random_state).reset_index(drop=True)
    df.insert(0, "Computer_ID", [f"PC_{i+1:03d}" for i in range(len(df))])
    return df

def generate_visualisations(clf, feature_names, class_names, X_test, y_test, y_pred, df):
    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'axes.spines.top': False,
        'axes.spines.right': False,
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
        'axes.edgecolor': '#444444',
        'xtick.color': '#222222',
        'ytick.color': '#222222',
        'axes.labelcolor': '#111111',
        'text.color': '#111111',
    })

    # Figure 1: Decision Tree Architecture (Filled with distinct pastel/vibrant class colors)
    fig, ax = plt.subplots(figsize=(22, 11), dpi=200)
    plot_tree(
        clf,
        feature_names=feature_names,
        class_names=class_names,
        filled=True,
        rounded=True,
        fontsize=9,
        ax=ax,
        precision=2,
        impurity=True
    )
    plt.title("Trained Decision Tree Model for Computer Lab Fault Diagnosis (Criterion=Entropy, Max_Depth=5)", 
              fontsize=14, fontweight='bold', pad=16, color='#1e3a8a')
    plt.tight_layout()
    plt.savefig(BASE_DIR / "viz_decision_tree.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Saved: viz_decision_tree.png")

    # Figure 2: Confusion Matrix Heatmap (Vivid YlGnBu / colorful heatmap with crisp contrast)
    cm = confusion_matrix(y_test, y_pred, labels=class_names)
    fig, ax = plt.subplots(figsize=(8.5, 6.8), dpi=200)
    sns.heatmap(cm, annot=True, fmt='d', cmap='YlGnBu', cbar=True,
                xticklabels=class_names, yticklabels=class_names, ax=ax,
                linewidths=1.8, linecolor='#ffffff',
                annot_kws={"size": 13, "fontweight": "bold", "color": "#0f172a"})
    ax.set_title("Confusion Matrix Heatmap — Test Evaluation", fontsize=13, fontweight='bold', pad=14, color='#0f172a')
    ax.set_xlabel("Predicted Fault Class", fontsize=11, labelpad=8, fontweight='bold', color='#1e293b')
    ax.set_ylabel("Actual Ground Truth Class", fontsize=11, labelpad=8, fontweight='bold', color='#1e293b')
    plt.xticks(rotation=22, ha='right', fontsize=9.5, fontweight='600')
    plt.yticks(rotation=0, fontsize=9.5, fontweight='600')
    plt.tight_layout()
    plt.savefig(BASE_DIR / "viz_confusion_matrix.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Saved: viz_confusion_matrix.png")

    # Figure 3: Feature Importance Bar Plot (Vivid Multi-color palette)
    importances = clf.feature_importances_
    indices = np.argsort(importances)[::-1]
    sorted_features = [feature_names[i] for i in indices]
    sorted_importances = importances[indices]

    palette = ['#e11d48', '#2563eb', '#059669', '#d97706', '#7c3aed', '#0891b2', '#ea580c', '#4f46e5', '#16a34a', '#db2777', '#ca8a04', '#0284c7', '#9333ea', '#65a30d', '#64748b']
    bar_colors = palette[:len(sorted_features)]

    fig, ax = plt.subplots(figsize=(10.5, 6.0), dpi=200)
    bars = ax.barh(range(len(sorted_features)), sorted_importances[::-1], color=bar_colors[::-1], edgecolor='#1e293b', linewidth=0.8, height=0.68)
    ax.set_yticks(range(len(sorted_features)))
    ax.set_yticklabels(sorted_features[::-1], fontsize=10, fontweight='600')
    ax.set_xlabel("Information Gain / Feature Importance (Entropy Reduction)", fontsize=11, labelpad=8, fontweight='bold', color='#1e293b')
    ax.set_title("Feature Importance Hierarchy in Lab Fault Diagnosis", fontsize=13, fontweight='bold', pad=14, color='#0f172a')
    for bar in bars:
        w = bar.get_width()
        if w > 0.005:
            ax.text(w + 0.008, bar.get_y() + bar.get_height()/2, f"{w:.3f}", 
                    va='center', fontsize=9.5, fontweight='bold', color='#0f172a')
    ax.set_xlim(0, max(sorted_importances) * 1.16)
    ax.xaxis.grid(True, linestyle='--', alpha=0.5, color='#94a3b8')
    plt.tight_layout()
    plt.savefig(BASE_DIR / "viz_feature_importance.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Saved: viz_feature_importance.png")

    # Figure 4: Model Performance Metrics Across Fault Classes (Vibrant Tri-Color Palette)
    report = classification_report(y_test, y_pred, target_names=class_names, output_dict=True)
    metrics_df = pd.DataFrame({
        "Precision": [report[c]["precision"] * 100 for c in class_names],
        "Recall": [report[c]["recall"] * 100 for c in class_names],
        "F1-Score": [report[c]["f1-score"] * 100 for c in class_names],
    }, index=class_names)

    fig, ax = plt.subplots(figsize=(10.5, 5.6), dpi=200)
    x = np.arange(len(class_names))
    width = 0.25
    rects1 = ax.bar(x - width, metrics_df["Precision"], width, label='Precision', color='#3b82f6', edgecolor='#1d4ed8', linewidth=1.2)
    rects2 = ax.bar(x, metrics_df["Recall"], width, label='Recall', color='#10b981', edgecolor='#047857', linewidth=1.2)
    rects3 = ax.bar(x + width, metrics_df["F1-Score"], width, label='F1-Score', color='#f59e0b', edgecolor='#b45309', linewidth=1.2)

    ax.set_ylabel('Score Percentage (%)', fontsize=11, fontweight='bold', color='#1e293b')
    ax.set_title('Per-Class Diagnostic Precision, Recall, and F1-Score Breakdown', fontsize=13, fontweight='bold', pad=14, color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(class_names, fontsize=10.5, fontweight='600')
    ax.set_ylim(0, 118)
    ax.legend(loc='lower right', fontsize=10.5, framealpha=0.98, edgecolor='#cbd5e1')
    ax.yaxis.grid(True, linestyle='--', alpha=0.5, color='#94a3b8')

    for rects in [rects1, rects2, rects3]:
        for bar in rects:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, h + 1.6, f"{h:.1f}%",
                    ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    plt.tight_layout()
    plt.savefig(BASE_DIR / "viz_model_metrics.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Saved: viz_model_metrics.png")

def main():
    if sys.stdout.encoding.lower() != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    print("Initializing PCCOE LabFault-DT Diagnostic Engine...")
    print("=" * 86)
    print(" PCCOE LABFAULT-DT: COMPUTER LABORATORY FAULT DIAGNOSIS SYSTEM")
    print(" Department of Information Technology | Pimpri Chinchwad College of Engineering")
    print("=" * 86)
    
    # 1. Dataset Generation or Loading
    if not DATASET_PATH.exists():
        print(f">> Generating synthetic diagnostic telemetry dataset ({DATASET_PATH.name})...")
        df = generate_synthetic_lab_dataset(n_samples=400, random_state=42)
        df.to_csv(DATASET_PATH, index=False)
        print(f">> Saved {len(df)} telemetry records to {DATASET_PATH.name}")
    else:
        print(f">> Loading telemetry dataset from {DATASET_PATH.name}...")
        df = pd.read_csv(DATASET_PATH)

    print(f"Total Systems Profiled       : {len(df)}")
    print(f"Diagnostic Attributes        : {df.shape[1] - 2} features (1 Identifier, 1 Target Class)")
    print(f"Target Fault Categories      : {list(df['Fault_Type'].unique())}")
    print("-" * 86)

    # 2. Data Preprocessing & Train-Test Split
    feature_cols = [c for c in df.columns if c not in ["Computer_ID", "Fault_Type"]]
    X = df[feature_cols]
    y = df["Fault_Type"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"Training Set Size            : {X_train.shape[0]} samples (80%)")
    print(f"Testing Set Size             : {X_test.shape[0]} samples (20%)")
    print("-" * 86)

    # 3. Model Training
    print("Training Decision Tree Classifier (Criterion=Entropy, Max_Depth=5)...")
    clf = DecisionTreeClassifier(
        criterion="entropy",
        max_depth=5,
        min_samples_split=4,
        min_samples_leaf=2,
        random_state=42
    )
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # 4. Evaluation Metrics
    acc = accuracy_score(y_test, y_pred) * 100
    class_names = sorted(list(y.unique()))
    prec = precision_score(y_test, y_pred, average="weighted") * 100
    rec = recall_score(y_test, y_pred, average="weighted") * 100
    f1 = f1_score(y_test, y_pred, average="weighted") * 100

    print("DECISION TREE MODEL PERFORMANCE EVALUATION:")
    print(f">> Model Accuracy            : {acc:.2f} %")
    print(f">> Weighted Precision        : {prec:.2f} %")
    print(f">> Weighted Recall           : {rec:.2f} %")
    print(f">> Weighted F1-Score         : {f1:.2f} %")
    print("-" * 86)

    print("CLASSIFICATION REPORT PER FAULT TYPE:")
    print(classification_report(y_test, y_pred, digits=4))
    print("-" * 86)

    print("CONFUSION MATRIX:")
    cm = confusion_matrix(y_test, y_pred, labels=class_names)
    header = f"{'Actual \\ Pred':<18}" + "".join([f"{c[:10]:>12}" for c in class_names])
    print(header)
    for i, row_name in enumerate(class_names):
        row_str = f"{row_name:<18}" + "".join([f"{cm[i][j]:>12}" for j in range(len(class_names))])
        print(row_str)
    print("-" * 86)

    # 5. Production Inference Simulation & Rule-Based Recommendation
    print("INFERENCE DEMONSTRATION & MAINTENANCE ACTION ENGINE:")
    sample_queries = [
        {"ID": "PC_127", "Boot": 1, "CPU_T": 88, "CPU_U": 92, "RAM": 65, "D_Hlth": 85, "D_Use": 55, "Net_S": 1, "Lat": 18, "Loss": 0.2, "Fan": 0, "Err": 9, "Crash": 3, "Resp": 2.9, "OS": 1, "Pwr": 1},
        {"ID": "PC_042", "Boot": 1, "CPU_T": 54, "CPU_U": 62, "RAM": 95, "D_Hlth": 92, "D_Use": 60, "Net_S": 1, "Lat": 14, "Loss": 0.1, "Fan": 1, "Err": 18, "Crash": 4, "Resp": 3.7, "OS": 0, "Pwr": 1},
        {"ID": "PC_089", "Boot": 1, "CPU_T": 46, "CPU_U": 35, "RAM": 45, "D_Hlth": 90, "D_Use": 45, "Net_S": 0, "Lat": 999, "Loss": 100.0, "Fan": 1, "Err": 2, "Crash": 0, "Resp": 1.1, "OS": 1, "Pwr": 1},
        {"ID": "PC_156", "Boot": 0, "CPU_T": 52, "CPU_U": 50, "RAM": 55, "D_Hlth": 28, "D_Use": 96, "Net_S": 1, "Lat": 16, "Loss": 0.3, "Fan": 1, "Err": 14, "Crash": 2, "Resp": 4.8, "OS": 0, "Pwr": 1},
        {"ID": "PC_201", "Boot": 1, "CPU_T": 44, "CPU_U": 28, "RAM": 40, "D_Hlth": 96, "D_Use": 40, "Net_S": 1, "Lat": 10, "Loss": 0.1, "Fan": 1, "Err": 0, "Crash": 0, "Resp": 0.7, "OS": 1, "Pwr": 1},
    ]

    action_map = {
        "Hardware_Fault": "PRIORITY 1: Inspect CPU thermal paste, clean/replace cooling fan, verify heatsink seating.",
        "Software_Fault": "PRIORITY 2: Check memory-leak processes, rebuild corrupted OS profile, update software stack.",
        "Network_Fault":  "PRIORITY 2: Verify RJ-45 patch cable, test switch port VLAN, reset lab gateway adapter.",
        "Storage_Fault":  "PRIORITY 1: Backup user data immediately; clone sector to replacement NVMe/SATA SSD.",
        "No_Fault":       "PRIORITY 4: Routine maintenance only; system operating within optimal nominal thresholds."
    }

    for q in sample_queries:
        x_vec = pd.DataFrame([{
            "Boot_Status": q["Boot"], "CPU_Temperature": q["CPU_T"], "CPU_Usage": q["CPU_U"],
            "RAM_Usage": q["RAM"], "Disk_Health": q["D_Hlth"], "Disk_Usage": q["D_Use"],
            "Network_Status": q["Net_S"], "Network_Latency": q["Lat"], "Packet_Loss": q["Loss"],
            "Fan_Status": q["Fan"], "Error_Count": q["Err"], "Crash_Count": q["Crash"],
            "Response_Time": q["Resp"], "OS_Status": q["OS"], "Power_Status": q["Pwr"]
        }])
        pred = clf.predict(x_vec)[0]
        proba = np.max(clf.predict_proba(x_vec)) * 100
        print(f">> Computer: {q['ID']} | Diagnostic: CPU={q['CPU_T']}°C, RAM={q['RAM']}%, DiskH={q['D_Hlth']}%, NetStat={q['Net_S']}, Fan={q['Fan']}")
        print(f"   Classification : [{pred.upper()}] (Confidence: {proba:.1f}%)")
        print(f"   Recommendation : {action_map[pred]}")
        print()

    print("=" * 86)
    print("Generating Academic Diagnostic Visualisations...")
    generate_visualisations(clf, feature_cols, class_names, X_test, y_test, y_pred, df)
    print("All diagnostic charts successfully saved.")
    print("=" * 86)

if __name__ == "__main__":
    main()
