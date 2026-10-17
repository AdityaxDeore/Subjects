import nbformat

notebook_path = r"c:\Users\adity\Desktop\Subjects\GEN AI\Assignment - 3\assignment_3.ipynb"
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

markdown_content = """# Assignment No- 3

**TITLE**: Use Matplotlib or Seaborn to visualize data distributions and patterns in Generative AI datasets. Plot histograms, scatter plots, and heatmaps to analyze data characteristics.

**OBJECTIVES**: To learn Python and TensorFlow skills for Generative AI.

**OUTCOME**: Implement Python and TensorFlow basics, including data handling and preprocessing techniques.

**THEORY**:
In this assignment, students will explore data visualization techniques that are essential in understanding and analyzing Generative AI datasets. Using Python libraries such as Matplotlib and Seaborn, students will plot visualizations that reveal patterns, distributions, correlations, and insights from the data.
The task involves working with a real-world dataset and applying various types of plots to explore the structure and relationships in the data. These visualizations are crucial in preparing data for training machine learning and generative models.

**Dataset Reference**: Breast Cancer Wisconsin (Diagnostic) Dataset (scikit-learn)

**Tools to be Used**: Python, Pandas, Numpy, Matplotlib, Seaborn

**Tasks to Perform**:
1. **Histogram**
Visualize the distribution of continuous features to understand data skewness.
2. **Scatter Plot**
Plot relationships between two variables to explore trends or anomalies.
3. **Heatmap**
Use a correlation heatmap to analyze how features are correlated with each other, helping identify redundant or useful variables.

---

### 1. Histogram
A histogram is a graphical representation that organizes a group of data points into user-specified ranges or bins. It is commonly used to depict the distribution of a single continuous variable. In the context of Generative AI datasets, histograms help in understanding the frequency and spread of numerical features. They can reveal if the data is normally distributed, skewed, or contains outliers. This is critical for preprocessing steps like normalization or transformation.

### 2. Scatter Plot
A scatter plot displays individual data points based on two continuous variables. It helps identify relationships, patterns, or clusters between features. Scatter plots also assist in detecting outliers or anomalies, which can be significant in training generative models and avoiding bias.

### 3. Heatmap
A heatmap is a two-dimensional visual representation of data where values are represented by color. When used with a correlation matrix, it displays the degree of correlation between numerical features in the dataset. In a Generative AI context, heatmaps help determine which features are strongly or weakly correlated. This insight is useful for feature selection, dimensionality reduction, and improving model performance by removing redundant data.
"""

md_cell = nbformat.v4.new_markdown_cell(markdown_content)
nb.cells.insert(0, md_cell)

with open(notebook_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
