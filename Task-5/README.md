# Task 5 - Predictive Model or Insight Project

This folder contains the code for **Task 5**.

## Goal

Build a simple predictive model or generate meaningful insights from data.

## Key Skills

- Basic machine learning concepts
- Model understanding
- Data preprocessing
- Model evaluation

## What this task does

This task trains a classification model to predict `depression_label` from the cleaned teen mental health dataset.

## Files in this task

1. `task5_predictive_model.py` - main training and reporting script.
2. `requirements.txt` - Python packages needed for the script.
3. `data/cleaned_teen_mental_health_dataset.csv` - cleaned dataset used for modeling.
4. `outputs/task5_model_report.md` - summary of the model and results.
5. `outputs/*.png` - charts showing evaluation and feature impact.
6. `outputs/*.csv` - metrics and prediction outputs.
7. `outputs/task5_depression_model.joblib` - saved trained model.

## Step-by-step explanation

### Step 1 - Load the cleaned data

The script reads the cleaned CSV file from the `data/` folder.

### Step 2 - Split features and target

The target column is `depression_label`, and all other columns are used as input features.

### Step 3 - Preprocess the data

Numeric columns are imputed with the median and scaled. Categorical columns are imputed with the most common value and one-hot encoded.

### Step 4 - Train the model

The script trains a logistic regression classifier with class balancing to handle the uneven class distribution.

### Step 5 - Evaluate the model

The script creates accuracy, precision, recall, F1 score, ROC AUC, and a confusion matrix.

### Step 6 - Save outputs

The script saves charts, CSV files, a markdown report, and the trained model file.

## How to run

From the repository root:

```bash
pip install -r Task-5/requirements.txt
python Task-5/task5_predictive_model.py
```

## Output files

- [Model report](outputs/task5_model_report.md)
- [Model metrics](outputs/task5_model_metrics.csv)
- [Baseline metrics](outputs/task5_baseline_metrics.csv)
- [Feature importance](outputs/task5_feature_importance.csv)
- [Confusion matrix](outputs/task5_confusion_matrix.png)
- [ROC curve](outputs/task5_roc_curve.png)
- [Top drivers](outputs/task5_top_drivers.png)
