# DecodeLabs Internship Projects

A reproducible pipeline to explore teen mental health survey data: cleaning, exploratory analysis, visualization, and a simple predictive model.

## About

This project explores a teen mental health dataset with the goal of demonstrating
data cleaning, exploratory analysis, visualization, and a simple predictive
model. The repository is organized into separate Task folders (Task-1..Task-5)
so each step of the workflow is reproducible and easy to review.

Key points:

- Dataset: Teen_Mental_Health_Dataset.csv (1200 rows, 13 columns)
- Focus: cleaning, EDA, visualization, simple ML model
- Outputs: CSV reports, PNG charts, PDF and markdown reports, and a saved model

If you want to run everything locally, follow the `README.md` in each Task folder.

## Task 1 - Data Collection and Dataset Understanding
[](https://github.com/Buduthaharishreddy/DecodeLabs#task-1---data-collection-and-dataset-understanding)

- [Task-1/README.md](Task-1/README.md)
- [Task-1/task1_simple.py](Task-1/task1_simple.py)
- [Task-1/generate_report.py](Task-1/generate_report.py)
- [Task-1/requirements.txt](Task-1/requirements.txt)

## What Task 1 does

- Loads the dataset
- Shows column names and data types
- Checks dataset size
- Checks missing values
- Summarizes categorical and numeric columns

## Run Task 1

```bash
pip install -r Task-1/requirements.txt
python Task-1/task1_simple.py
python Task-1/generate_report.py
```

## Task 2 - Data Cleaning & Preprocessing

- [Task-2/README.md](Task-2/README.md)
- [Task-2/task2_preprocessing.py](Task-2/task2_preprocessing.py)
- [Task-2/requirements.txt](Task-2/requirements.txt)
- [Task-2/data/Teen_Mental_Health_Dataset.csv](Task-2/data/Teen_Mental_Health_Dataset.csv)
- [Task-2/outputs/cleaned_teen_mental_health_dataset.csv](Task-2/outputs/cleaned_teen_mental_health_dataset.csv)
- [Task-2/outputs/task2_cleaning_report.txt](Task-2/outputs/task2_cleaning_report.txt)

## What Task 2 does

- Handles missing values
- Removes duplicate rows
- Formats data correctly
- Saves a cleaned dataset
- Writes a cleaning report

## Run Task 2

```bash
pip install -r Task-2/requirements.txt
python Task-2/task2_preprocessing.py
```

## Task 3 - Exploratory Data Analysis (EDA)

- [Task-3/README.md](Task-3/README.md)
- [Task-3/task3_eda.py](Task-3/task3_eda.py)
- [Task-3/requirements.txt](Task-3/requirements.txt)
- [Task-3/data/cleaned_teen_mental_health_dataset.csv](Task-3/data/cleaned_teen_mental_health_dataset.csv)
- [Task-3/outputs/task3_report.md](Task-3/outputs/task3_report.md)
- [Task-3/outputs/task3_findings.md](Task-3/outputs/task3_findings.md)
- [Task-3/outputs/basic_statistics.csv](Task-3/outputs/basic_statistics.csv)
- [Task-3/outputs/numeric_statistics.csv](Task-3/outputs/numeric_statistics.csv)
- [Task-3/outputs/trend_summary.csv](Task-3/outputs/trend_summary.csv)
- [Task-3/outputs/outlier_summary.csv](Task-3/outputs/outlier_summary.csv)
- [Task-3/outputs/correlation_matrix.csv](Task-3/outputs/correlation_matrix.csv)
- [Task-3/outputs/correlation_heatmap.png](Task-3/outputs/correlation_heatmap.png)
- [Task-3/outputs/outlier_boxplots.png](Task-3/outputs/outlier_boxplots.png)

## What Task 3 does

- Calculates basic statistics
- Identifies trends and outliers
- Summarizes findings
- Saves CSV, markdown, and image outputs

## Run Task 3

```bash
pip install -r Task-3/requirements.txt
python Task-3/task3_eda.py
```

## Task 4 - Data Visualization

- [Task-4/README.md](Task-4/README.md)
- [Task-4/task4_visualization.py](Task-4/task4_visualization.py)
- [Task-4/requirements.txt](Task-4/requirements.txt)
- [Task-4/data/cleaned_teen_mental_health_dataset.csv](Task-4/data/cleaned_teen_mental_health_dataset.csv)
- [Task-4/outputs/task4_visual_report.md](Task-4/outputs/task4_visual_report.md)
- [Task-4/outputs/gender_distribution.png](Task-4/outputs/gender_distribution.png)
- [Task-4/outputs/platform_usage_distribution.png](Task-4/outputs/platform_usage_distribution.png)
- [Task-4/outputs/social_interaction_level.png](Task-4/outputs/social_interaction_level.png)
- [Task-4/outputs/correlation_heatmap.png](Task-4/outputs/correlation_heatmap.png)
- [Task-4/outputs/social_media_vs_sleep.png](Task-4/outputs/social_media_vs_sleep.png)

## What Task 4 does

- Creates charts and graphs
- Chooses appropriate visual types
- Highlights key insights
- Saves chart images and a visual report

## Run Task 4

```bash
pip install -r Task-4/requirements.txt
python Task-4/task4_visualization.py
```

## Task 5 - Predictive Model or Insight Project

- [Task-5/README.md](Task-5/README.md)
- [Task-5/task5_predictive_model.py](Task-5/task5_predictive_model.py)
- [Task-5/requirements.txt](Task-5/requirements.txt)
- [Task-5/data/cleaned_teen_mental_health_dataset.csv](Task-5/data/cleaned_teen_mental_health_dataset.csv)
- [Task-5/outputs/task5_model_report.md](Task-5/outputs/task5_model_report.md)
- [Task-5/outputs/task5_model_metrics.csv](Task-5/outputs/task5_model_metrics.csv)
- [Task-5/outputs/task5_confusion_matrix.png](Task-5/outputs/task5_confusion_matrix.png)
- [Task-5/outputs/task5_roc_curve.png](Task-5/outputs/task5_roc_curve.png)
- [Task-5/outputs/task5_top_drivers.png](Task-5/outputs/task5_top_drivers.png)

## What Task 5 does

- Trains a predictive classification model
- Handles preprocessing automatically
- Evaluates model performance
- Saves charts, metrics, and the trained model

## Run Task 5

```bash
pip install -r Task-5/requirements.txt
python Task-5/task5_predictive_model.py
```
