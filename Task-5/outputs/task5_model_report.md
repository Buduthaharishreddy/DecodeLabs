# Task 5 - Predictive Model

## Goal
Build a simple predictive model that estimates `depression_label` from the cleaned dataset.

## Dataset
- Rows: 1200
- Columns: 13
- Class distribution: {"0": 1169, "1": 31}

## Model
- Algorithm: Logistic Regression
- Strategy: Train/test split with stratification
- Preprocessing: Median imputation for numeric fields, most-frequent imputation plus one-hot encoding for categorical fields
- Balance handling: `class_weight='balanced'`

## Results
- Accuracy: 0.9667
- Precision: 0.4286
- Recall: 1.0000
- F1 score: 0.6000
- ROC AUC: 0.9936

## Baseline
- Majority-class accuracy: 0.9750
- Majority-class precision: 0.0000
- Majority-class recall: 0.0000
- Majority-class F1: 0.0000

## Outputs
- task5_model_metrics.csv
- task5_baseline_metrics.csv
- task5_feature_importance.csv
- task5_test_predictions.csv
- task5_confusion_matrix.png
- task5_roc_curve.png
- task5_top_drivers.png
- task5_depression_model.joblib

## Insight
The model captures a strong separation signal in the cleaned data and is more useful than a simple always-negative baseline because it identifies positive cases.