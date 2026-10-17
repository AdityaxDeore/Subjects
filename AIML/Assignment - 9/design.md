# Assignment 9 Design Specification

Assignment 9 implements the Bagging technique using the Random Forest algorithm to classify the Iris dataset and compare its accuracy with a single Decision Tree model.

- **Course**: Artificial Intelligence and Machine Learning (AIML)
- **Institution**: Pimpri Chinchwad College of Engineering (PCCOE)
- **Student**: Aditya Chandrajit Deore (PRN: 124B1F116)
- **Topic**: Bagging Ensemble Learning & Random Forest Algorithm
- **Dataset**: Fisher's Iris Flower Dataset (150 samples, 4 numerical features, 3 balanced species classes).
- **Dataset Persistence**: Exported as `iris_dataset.csv` in the assignment folder for local reproducibility.
- **Models Compared**:
  1. Single Baseline Decision Tree (`DecisionTreeClassifier(random_state=42)`)
  2. Random Forest Ensemble (`RandomForestClassifier(n_estimators=100, max_features='sqrt', bootstrap=True, random_state=42)`)
- **Evaluation Metrics**: Accuracy, Macro Precision, Macro Recall, Macro F1-Score, Confusion Matrices, and Gini Feature Importance.
- **Visual Artifacts Generated**:
  1. `viz_model_comparison.png` & `.svg`
  2. `viz_confusion_matrices.png` & `.svg`
  3. `viz_feature_importance.png` & `.svg`
  4. `viz_majority_voting_demo.png` & `.svg`
- **Output Documents**:
  - `Assignment_9_Report.html`: Full theoretical report and practical documentation following the PCCOE format.
  - `Assignment_9_Output_and_AI_Usage.html`: Model execution trace, evaluation charts, confusion matrix breakdown, and AI usage disclosure.
