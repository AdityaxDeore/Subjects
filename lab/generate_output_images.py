import matplotlib
matplotlib.use('Agg')
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

out_dir = r"c:\Users\adity\Desktop\Subjects\lab\output_images"
os.makedirs(out_dir, exist_ok=True)

df = pd.read_csv(r"c:\Users\adity\Desktop\Subjects\lab\hanoi_dataset.csv")

# 1. Class Distribution
plt.figure(figsize=(6, 4))
df['complexity'].value_counts().plot(kind='bar', color=['steelblue', 'coral', 'green'])
plt.title('Class Distribution')
plt.xlabel('Complexity')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, '1_class_distribution.png'), dpi=200)
plt.close()

# Data Split & Train
X = df.drop(columns=['complexity'])
y = df['complexity']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

train_acc = accuracy_score(y_train, clf.predict(X_train))
test_acc  = accuracy_score(y_test, y_pred)

# 2. Accuracy Chart
plt.figure(figsize=(6, 4))
plt.bar(['Train Accuracy', 'Test Accuracy'], [train_acc * 100, test_acc * 100], color=['steelblue', 'coral'])
plt.title('Training vs Testing Accuracy')
plt.ylabel('Accuracy (%)')
plt.ylim(0, 110)
for i, v in enumerate([train_acc * 100, test_acc * 100]):
    plt.text(i, v + 2, f"{v:.1f}%", ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, '2_accuracy_comparison.png'), dpi=200)
plt.close()

# 3. Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4.5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=clf.classes_, yticklabels=clf.classes_)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, '3_confusion_matrix.png'), dpi=200)
plt.close()

# 4. Feature Importance
plt.figure(figsize=(7, 4))
importances = pd.Series(clf.feature_importances_, index=X.columns)
importances.sort_values().plot(kind='barh', color='steelblue')
plt.title('Feature Importances')
plt.xlabel('Importance')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, '4_feature_importance.png'), dpi=200)
plt.close()

# 5. Feature Correlation Heatmap
plt.figure(figsize=(7, 5))
sns.heatmap(df.drop(columns=['complexity']).corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Feature Correlation')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, '5_feature_correlation.png'), dpi=200)
plt.close()

# 6. Decision Tree
plt.figure(figsize=(16, 8))
plot_tree(
    clf,
    feature_names=list(X.columns),
    class_names=list(clf.classes_),
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title('Decision Tree')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, '6_decision_tree.png'), dpi=200)
plt.close()

print("ALL_IMAGES_SAVED")
