# Task 3 - Exploratory Data Analysis (EDA)

This folder contains the code for **Task 3**.

## Goal

Analyze the dataset to discover patterns and trends.

## Key Requirements

- Calculate basic statistics
- Identify trends and outliers
- Summarize findings

## Files in this task

1. `task3_eda.py` - main EDA script.
2. `requirements.txt` - Python packages needed for the script.
3. `data/cleaned_teen_mental_health_dataset.csv` - cleaned dataset used for analysis.
4. `outputs/task3_report.md` - overview of the analysis.
5. `outputs/task3_findings.md` - summary of the findings.
6. `outputs/basic_statistics.csv` - basic dataset statistics.
7. `outputs/numeric_statistics.csv` - numeric statistics.
8. `outputs/trend_summary.csv` - trend summary by category.
9. `outputs/outlier_summary.csv` - outlier information.
10. `outputs/correlation_matrix.csv` - numeric correlation matrix.
11. `outputs/correlation_heatmap.png` - correlation heatmap image.
12. `outputs/outlier_boxplots.png` - outlier boxplot image.

## Step-by-step explanation

### Step 1 - Load the cleaned dataset

The script reads the cleaned dataset from `data/cleaned_teen_mental_health_dataset.csv`.

### Step 2 - Calculate basic statistics

The script creates a full summary of the dataset and saves it to CSV files.

### Step 3 - Identify trends

The script groups the data by important categorical columns and calculates average numeric values.

### Step 4 - Detect outliers

The script uses the IQR method to find outliers in numeric columns.

### Step 5 - Check correlations

The script calculates a correlation matrix and saves a heatmap image.

### Step 6 - Summarize findings

The script writes a final markdown report with the main findings.

## Features

- Dataset loading
- Basic statistics
- Trend analysis
- Outlier detection
- Correlation analysis
- Markdown summary report
- Heatmap and boxplot images

## How to run

From the repository root:

```bash
pip install -r Task-3/requirements.txt
python Task-3/task3_eda.py
```

## Output files

- [Task 3 report](outputs/task3_report.md)
- [Task 3 findings](outputs/task3_findings.md)
- [Basic statistics](outputs/basic_statistics.csv)
- [Numeric statistics](outputs/numeric_statistics.csv)
- [Trend summary](outputs/trend_summary.csv)
- [Outlier summary](outputs/outlier_summary.csv)
- [Correlation matrix](outputs/correlation_matrix.csv)
- [Correlation heatmap](outputs/correlation_heatmap.png)
- [Outlier boxplots](outputs/outlier_boxplots.png)

## Short conclusion

This task helps you understand the dataset more deeply by showing numeric patterns, category trends, outliers, and relationships between variables.
