# Task 4 - Data Visualization

This folder contains the code for **Task 4**.

## Goal

Create visual representations to communicate insights clearly.

## Key Requirements

- Create charts and graphs
- Choose appropriate visual types
- Highlight key insights

## Files in this task

1. `task4_visualization.py` - main visualization script.
2. `requirements.txt` - Python packages needed for the script.
3. `data/cleaned_teen_mental_health_dataset.csv` - cleaned dataset used for visualization.
4. `outputs/task4_visual_report.md` - summary report.
5. `outputs/*.png` - the charts and graphs created by the script.

## Step-by-step explanation

### Step 1 - Load the cleaned dataset

The script reads the cleaned CSV file from the `data/` folder.

### Step 2 - Choose visual types

The script uses count plots, histograms, a correlation heatmap, and a scatter plot because these fit the data types well.

### Step 3 - Create charts

The script creates plots for gender, platform usage, social interaction level, numeric distributions, correlations, and relationships.

### Step 4 - Highlight key insights

The script saves a markdown report that lists all created charts and summarizes the main visual insights.

## Features

- Data loading
- Count plots for categories
- Histograms for numeric values
- Correlation heatmap
- Scatter plot for relationship analysis
- Markdown report generation

## How to run

From the repository root:

```bash
pip install -r Task-4/requirements.txt
python Task-4/task4_visualization.py
```

## Output files

- [Visualization report](outputs/task4_visual_report.md)
- [Gender distribution](outputs/gender_distribution.png)
- [Platform usage distribution](outputs/platform_usage_distribution.png)
- [Social interaction level](outputs/social_interaction_level.png)
- [Correlation heatmap](outputs/correlation_heatmap.png)
- [Social media vs sleep](outputs/social_media_vs_sleep.png)

## Short conclusion

This task turns the dataset into visual charts that make the patterns easier to understand and explain.
