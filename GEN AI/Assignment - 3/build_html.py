import nbformat

notebook_path = r"c:\Users\adity\Desktop\Subjects\GEN AI\Assignment - 3\assignment_3.ipynb"
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

images = []
# Extract the first comment line of each cell to use as the specific title
for cell in nb.cells:
    if cell.cell_type == 'code':
        img_data = None
        for output in cell.get('outputs', []):
            if output.output_type in ['display_data', 'execute_result']:
                if 'image/png' in output.data:
                    img_data = output.data['image/png']
                    break
        
        if img_data:
            # Extract title from the first comment line
            lines = cell.source.split('\n')
            title = "Visualization"
            for line in lines:
                if line.startswith('#') and not line.startswith('# ---') and not 'Load and prepare' in line:
                    title = line.strip('# \n')
                    break
            images.append({'title': title, 'data': img_data})

def get_description(title):
    t = title.lower()
    if 'clustermap' in t:
        return "<strong>How it works:</strong> Performs hierarchical agglomerative clustering on the data to group similar features. It calculates euclidean distances to plot a heatmap accompanied by dendrograms showing the cluster hierarchy."
    elif 'ecdf' in t:
        return "<strong>How it works:</strong> Empirical Cumulative Distribution Function. Plots the exact proportion of data points that are less than or equal to each value, providing a cumulative view of the distribution without binning bias."
    elif 'ridge' in t:
        return "<strong>How it works:</strong> Creates overlapping density plots (KDEs) for multiple variables, offering a compact and visually appealing way to compare distributions across many features simultaneously."
    elif 'heatmap' in t:
        return "<strong>How it works:</strong> Calculates the Pearson correlation coefficient matrix across numeric features and maps the correlation strengths (-1 to 1) to a color gradient, easily revealing multi-collinearity."
    elif 'pair plot' in t or 'pairplot' in t:
        return "<strong>How it works:</strong> Generates a grid matrix of scatter plots and histograms, pairwise crossing every numeric feature. It calculates the intersections of all dimensions to visualize multidimensional relationships instantly."
    elif 'swarm' in t:
        return "<strong>How it works:</strong> A scatter plot for categorical variables where points are adjusted algorithmically so they do not overlap, providing a precise, granular view of the density and individual distributions."
    elif 'strip' in t or 'point' in t:
        return "<strong>How it works:</strong> Calculates the point estimate (mean) with confidence intervals. Layered with a strip plot which drops all raw data points along a single axis with random jitter to show raw density."
    elif 'kde' in t:
        return "<strong>How it works:</strong> Kernel Density Estimation. Calculates a continuous probability density curve by placing a smooth Gaussian kernel over each data point and summing them, revealing the underlying continuous distribution."
    elif 'lmplot' in t or 'regression' in t:
        return "<strong>How it works:</strong> Fits a linear regression model to the scatter data using least squares optimization. It plots the line of best fit alongside a shaded confidence interval region."
    elif 'count plot' in t:
        return "<strong>How it works:</strong> A specific type of bar plot that simply calculates and visualizes the raw frequency (count) of observations for each categorical class."
    elif 'stem' in t:
        return "<strong>How it works:</strong> Plots vertical lines from a baseline to the data point, topped with a marker. Useful for highlighting the discrete nature of sequential or positional data."
    elif 'fill between' in t or 'contour' in t:
        return "<strong>How it works:</strong> Visualizes regions of variance or 3D surfaces mapped onto a 2D plane by interpolating z-values and drawing continuous iso-lines or shaded regions."
    elif 'error bar' in t:
        return "<strong>How it works:</strong> Shows the variability of data. Calculates the standard deviation or standard error and plots it as a visual line extending from the mean to indicate statistical uncertainty."
    elif 'hexbin' in t or 'joint plot' in t:
        return "<strong>How it works:</strong> Bins 2D space into hexagonal regions and colors them based on the count of points inside. Extremely useful for highly dense scatter datasets where individual points heavily overlap."
    elif 'step' in t:
        return "<strong>How it works:</strong> Connects points with horizontal and vertical lines, emphasizing discrete structural jumps in the dataset rather than continuous flow."
    elif 'pie' in t:
        return "<strong>How it works:</strong> Displays the proportion of categorical classes as slices of a circle, where the arc length corresponds to the percentage of the whole dataset."
    elif 'violin' in t:
        return "<strong>How it works:</strong> Combines a box plot with a symmetric Kernel Density Estimation (KDE). It calculates a smoothed density curve to show the full distribution shape alongside central quartiles."
    elif 'box' in t or 'boxen' in t:
        return "<strong>How it works:</strong> Visualizes the five-number summary of a dataset. It calculates the interquartile range (IQR) to highlight the central 50% of data and aggressively isolates statistical outliers."
    elif 'hist' in t:
        return "<strong>How it works:</strong> Shows the distribution of a continuous variable by dividing the data range into discrete 'bins' and counting the number of observations that fall into each specific bin."
    elif 'bar' in t:
        return "<strong>How it works:</strong> Represents categorical data with rectangular bars where the height is proportional to the aggregated values they represent (often calculating the mean of that category)."
    elif '3d scatter' in t:
        return "<strong>How it works:</strong> Extends the standard scatter plot into three mathematical dimensions (x, y, z axes), allowing visualization of complex multi-feature vector spaces simultaneously."
    elif 'scatter' in t:
        return "<strong>How it works:</strong> Visualizes the raw relationship between continuous variables by plotting individual data points on a Cartesian plane. Size and color are mapped dynamically to extra dimensions."
    elif 'line' in t:
        return "<strong>How it works:</strong> Displays data points connected by straight line segments. Calculated by sorting the dataset along one dimension and plotting the values sequentially to visualize structural trends."
    else:
        return "<strong>How it works:</strong> Maps dataset variables to visual properties (position, color, size) to reveal underlying data geometry and statistical distributions."

html_head = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Assignment 3</title>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
body {
  font-family: Arial, sans-serif;
  font-size: 12pt;
  line-height: 1.5;
  color: #000;
  background: #e5e7eb;
  padding: 20px;
}
.container {
  max-width: 8.5in;
  margin: 0 auto;
}
.page {
  min-height: 11in;
  width: 8.5in;
  padding: 0.8in;
  background: #ffffff;
  margin: 0 auto 20px auto;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  position: relative;
  box-sizing: border-box;
}
.page:focus-within {
  outline: 2px dashed #4299e1;
}
@media print {
  body {
    background: #ffffff;
    padding: 0;
  }
  .container {
    max-width: 100%;
    margin: 0;
    box-shadow: none;
  }
  .page {
    width: 100%;
    min-height: auto;
    margin: 0;
    padding: 0.2in;
    box-shadow: none;
    border: none;
    page-break-after: always;
  }
}
.cover-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 25px;
  font-family: 'Times New Roman', Times, serif;
}
.cover-table td {
  border: 1px solid #000;
  padding: 8px 12px;
}
.cover-table .college-info {
  text-align: center;
  font-weight: bold;
  font-size: 16pt;
  line-height: 1.4;
}
.cover-table .row-centered { text-align: center; font-weight: bold; font-size: 14pt; }
.cover-table .row-left { text-align: left; font-weight: bold; font-size: 14pt; }
.logo-container { text-align: center; width: 18%; padding: 5px !important; }
.logo-container img { max-width: 100px; height: auto; display: block; margin: 0 auto; }
h2 { font-family: Arial; font-size: 16pt; color: #000; margin-top: 25px; margin-bottom: 10px; }
h3 { font-family: Arial; font-size: 14pt; color: #000; margin-top: 18px; margin-bottom: 5px; border-bottom: 1px solid #ddd; padding-bottom: 5px; }
p { font-family: Arial; font-size: 11pt; text-align: justify; line-height: 1.5; margin-bottom: 15px; }
.plot-desc { font-family: Arial; font-size: 10.5pt; color: #444; background: #f9fafb; padding: 10px; margin-bottom: 15px; border-radius: 4px;}
ul, ol { margin-left: 20px; font-size: 11pt; margin-bottom: 15px; }
li { margin-bottom: 6px; }
img.plot { max-width: 90%; height: auto; display: block; margin: 15px auto 25px auto; border: 1px solid #eee; padding: 10px; border-radius: 8px; }
</style>
</head>
<body>
<div class="container" contenteditable="true">
"""

page1 = """
<div class="page">
<table class="cover-table">
  <tr>
    <td class="logo-container">
      <img src="../Assignment - 1/pccoelogo.jfif" alt="PCCOE Logo" contenteditable="false">
    </td>
    <td class="college-info">
      Pimpri Chinchwad Education Trust's<br>
      Pimpri Chinchwad college of Engineering
    </td>
  </tr>
  <tr>
    <td colspan="2" class="row-centered">
      Assignment No. 3
    </td>
  </tr>
  <tr>
    <td colspan="2" class="row-left">
      Course:- Generative AI
    </td>
  </tr>
  <tr>
    <td colspan="2" class="row-left">
      Name:- Aditya Chandrajit Deore
    </td>
  </tr>
  <tr>
    <td colspan="2" class="row-left">
      PRN:- 124B1F116
    </td>
  </tr>
</table>

<h2>TITLE:</h2>
<p>Advanced Data Visualization & Distribution Analysis in Generative AI using Matplotlib and Seaborn.</p>
<h2>OBJECTIVES:</h2>
<p>To master advanced Python data visualization libraries and uncover hidden data geometries critical for Generative AI model training.</p>
<h2>OUTCOME:</h2>
<p>Implement robust Python preprocessing pipelines, utilizing 40 distinct visualization techniques across Matplotlib and Seaborn to analyze multivariate correlations, variance, and distributions.</p>

<h2>THEORY & METHODOLOGY:</h2>
<p>In this assignment, data visualization is explored not merely as a reporting tool, but as a crucial mathematical prerequisite for training Generative AI models. Understanding the latent space, feature variance, and inter-variable correlations directly influences how autoencoders, GANs, and diffusion models interpret dataset geometries. By utilizing the <strong>Breast Cancer Wisconsin (Diagnostic)</strong> dataset, we conduct an exhaustive exploratory data analysis (EDA) pipeline.</p>
<p>We deploy <strong>Matplotlib</strong> to build foundational visualizations such as 3D Scatter plots, Hexbin density grids, discrete Stem plots, and stacked variance histograms. This grants us absolute control over the coordinate geometries. Subsequently, we utilize <strong>Seaborn</strong> for high-level statistical plotting, implementing Clustermaps, ECDF distributions, Ridge plots (FacetGrids), and layered Swarm-Violin combinations. These approaches automatically resolve kernel density estimations (KDE) and complex categorical mapping, which are indispensable when handling high-dimensional Generative AI datasets.</p>

<h2>Advanced Techniques Implemented:</h2>
<ul>
  <li><strong>Distribution Tracking:</strong> Employing KDEs, Ridge plots, Boxen plots, and Empirical Cumulative Distribution Functions (ECDF) to trace skewness and variance.</li>
  <li><strong>Multivariate Correlation:</strong> Utilizing hierarchical Clustermaps, Masked Heatmaps, and Pair Plots to identify covariant and redundant features that could introduce bias into generative systems.</li>
  <li><strong>Density & Outlier Detection:</strong> Implementing Hexbin plots, 2D Contours, and layered Swarm-Violin topologies to robustly isolate outliers in the diagnostic data space.</li>
</ul>

</div>
"""

html_tail = """
</div>
</body>
</html>
"""

# Chunk the images into pages (2 images per page to fit descriptions and avoid overflowing 11 inches)
image_pages = ""
images_per_page = 2
for i in range(0, len(images), images_per_page):
    chunk = images[i:i+images_per_page]
    page_html = '<div class="page">\n'
    for img_obj in chunk:
        title = img_obj['title']
        desc = get_description(title)
        img_b64 = img_obj['data']
        page_html += f'<h3>{title}</h3>\n'
        page_html += f'<div class="plot-desc">{desc}</div>\n'
        page_html += f'<img class="plot" src="data:image/png;base64,{img_b64}">\n'
    page_html += '</div>\n'
    image_pages += page_html

final_html = html_head + page1 + image_pages + html_tail

output_path = r"c:\Users\adity\Desktop\Subjects\GEN AI\Assignment - 3\assignment_3.html"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Custom HTML created successfully with advanced content and fixed line breaks.")
