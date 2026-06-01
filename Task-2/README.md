# Task 2 - Data Cleaning and Preprocessing

This folder contains the code for **Task 2**.

## Goal

Prepare the dataset for analysis by cleaning and organizing the data.

## Key Requirements

- Handle missing values
- Remove duplicates
- Format data correctly

## Files in this task

1. `task2_preprocessing.py` - the main cleaning script.
2. `requirements.txt` - Python packages needed for the script.
3. `data/Teen_Mental_Health_Dataset.csv` - the input dataset.
4. `outputs/cleaned_teen_mental_health_dataset.csv` - the cleaned dataset.
5. `outputs/task2_cleaning_report.txt` - the cleaning summary report.

## Step-by-step explanation

### Step 1 - Load the dataset

The script reads the CSV file using `pandas.read_csv()`.

### Step 2 - Clean column names

The script changes column names to lowercase and replaces spaces or hyphens with underscores.

### Step 3 - Clean text values

The script removes extra spaces from text columns and converts empty strings to missing values.

### Step 4 - Convert numeric values

The script makes sure numeric columns are really numeric.

### Step 5 - Handle missing values

The script fills missing numeric values with the median and fills missing text values with the most common value.

### Step 6 - Remove duplicates

The script removes duplicate rows so the dataset is cleaner.

### Step 7 - Format data correctly

The script converts whole-number numeric columns to integer format.

### Step 8 - Save outputs

The cleaned dataset and a short report are saved in the `outputs/` folder.

## Features

- Data loading
- Column name standardization
- Missing value handling
- Duplicate removal
- Data type formatting
- Cleaned CSV export
- Cleaning report export

## How to run

From the repository root:

```bash
pip install -r Task-2/requirements.txt
python Task-2/task2_preprocessing.py
```

## Output files

- [Cleaned CSV](outputs/cleaned_teen_mental_health_dataset.csv)
- [Cleaning report](outputs/task2_cleaning_report.txt)

## Short conclusion

This task makes the dataset ready for analysis by keeping the data clean, removing duplicates, and formatting the values correctly.
