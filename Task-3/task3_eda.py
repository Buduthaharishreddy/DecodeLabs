"""
Task 3 - Exploratory Data Analysis

This script loads the cleaned dataset, calculates basic statistics,
checks trends and outliers, and saves a short findings report.
"""

from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
INPUT_FILE = BASE_DIR / 'data' / 'cleaned_teen_mental_health_dataset.csv'
OUT_DIR = BASE_DIR / 'outputs'
OUT_DIR.mkdir(exist_ok=True)


def get_input_file():
    if INPUT_FILE.exists():
        return INPUT_FILE
    fallback = ROOT_DIR / 'Task-2' / 'outputs' / 'cleaned_teen_mental_health_dataset.csv'
    if fallback.exists():
        return fallback
    return ROOT_DIR / 'Teen_Mental_Health_Dataset.csv'


def load_data(path):
    try:
        return pd.read_csv(path, low_memory=False)
    except Exception:
        return pd.read_csv(path, encoding='latin1', low_memory=False)


def save_markdown(path, lines):
    path.write_text('\n'.join(lines), encoding='utf8')


def get_numeric_columns(df):
    return df.select_dtypes(include=['number']).columns.tolist()


def get_categorical_columns(df):
    return [c for c in df.columns if pd.api.types.is_string_dtype(df[c]) or str(df[c].dtype) == 'category']


def basic_statistics(df):
    rows, cols = df.shape
    numeric_cols = get_numeric_columns(df)
    cat_cols = get_categorical_columns(df)

    df.describe(include='all').T.to_csv(OUT_DIR / 'basic_statistics.csv')
    if numeric_cols:
        df[numeric_cols].describe().T.to_csv(OUT_DIR / 'numeric_statistics.csv')

    summary = [
        'Task 3 - Exploratory Data Analysis',
        '',
        f'Dataset shape: {rows} rows x {cols} columns',
        f'Numeric columns: {len(numeric_cols)}',
        f'Categorical columns: {len(cat_cols)}',
    ]
    return summary, numeric_cols, cat_cols


def trend_analysis(df, numeric_cols, cat_cols):
    trend_frames = []
    key_cats = [c for c in ['gender', 'platform_usage', 'social_interaction_level'] if c in cat_cols]
    for cat in key_cats:
        grouped = df.groupby(cat)[numeric_cols].mean(numeric_only=True).round(3)
        grouped.to_csv(OUT_DIR / f'trend_by_{cat}.csv')
        grouped_reset = grouped.reset_index()
        grouped_reset.insert(0, 'group_column', cat)
        trend_frames.append(grouped_reset)

    if trend_frames:
        pd.concat(trend_frames, ignore_index=True).to_csv(OUT_DIR / 'trend_summary.csv', index=False)


def outlier_analysis(df, numeric_cols):
    rows = []
    for col in numeric_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outlier_count = int(((df[col] < lower) | (df[col] > upper)).sum())
        rows.append({
            'column': col,
            'min': df[col].min(),
            'max': df[col].max(),
            'q1': q1,
            'q3': q3,
            'iqr': iqr,
            'lower_bound': lower,
            'upper_bound': upper,
            'outlier_count': outlier_count,
        })

    outlier_df = pd.DataFrame(rows).sort_values('outlier_count', ascending=False)
    outlier_df.to_csv(OUT_DIR / 'outlier_summary.csv', index=False)

    if numeric_cols:
        top_cols = outlier_df.head(4)['column'].tolist()
        fig, axes = plt.subplots(len(top_cols), 1, figsize=(10, 3 * max(1, len(top_cols))))
        if len(top_cols) == 1:
            axes = [axes]
        for ax, col in zip(axes, top_cols):
            sns.boxplot(x=df[col], ax=ax, color='#7da87b')
            ax.set_title(f'Outlier check: {col}')
        plt.tight_layout()
        plt.savefig(OUT_DIR / 'outlier_boxplots.png', dpi=150)
        plt.close(fig)


def correlation_analysis(df, numeric_cols):
    if not numeric_cols:
        return None

    corr = df[numeric_cols].corr().round(3)
    corr.to_csv(OUT_DIR / 'correlation_matrix.csv')

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation heatmap')
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'correlation_heatmap.png', dpi=150)
    plt.close()
    return corr


def summarize_findings(df, numeric_cols, cat_cols, corr, outlier_df):
    findings = []
    findings.append('# Task 3 Findings')
    findings.append('')
    findings.append(f'- Rows: {df.shape[0]}')
    findings.append(f'- Columns: {df.shape[1]}')
    findings.append(f'- Numeric columns: {len(numeric_cols)}')
    findings.append(f'- Categorical columns: {len(cat_cols)}')
    findings.append('')

    if not outlier_df.empty:
        top_outlier = outlier_df.iloc[0]
        findings.append('## Outliers')
        findings.append(f"- Most outlier-prone column: {top_outlier['column']} ({int(top_outlier['outlier_count'])} outliers)")
        findings.append('')

    if corr is not None:
        corr_abs = corr.abs().copy()
        for i in range(len(corr_abs)):
            corr_abs.iat[i, i] = 0
        if not corr_abs.empty:
            stacked = corr_abs.stack().sort_values(ascending=False)
            if not stacked.empty:
                top_pair = stacked.index[0]
                findings.append('## Trends')
                findings.append(f'- Strongest numeric relationship: {top_pair[0]} and {top_pair[1]} ({corr.loc[top_pair[0], top_pair[1]]})')
                findings.append('')

    findings.append('## Summary')
    findings.append('- The cleaned dataset is ready for deeper analysis.')
    findings.append('- Basic statistics and group trends were calculated.')
    findings.append('- Outliers were checked using the IQR method.')

    save_markdown(OUT_DIR / 'task3_findings.md', findings)


def main():
    input_file = get_input_file()
    if not input_file.exists():
        print(f'Input file not found: {input_file}')
        return

    print('Loading cleaned dataset...')
    df = load_data(input_file)

    summary_lines, numeric_cols, cat_cols = basic_statistics(df)
    trend_analysis(df, numeric_cols, cat_cols)

    outlier_rows = []
    for col in numeric_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outlier_rows.append({
            'column': col,
            'outlier_count': int(((df[col] < lower) | (df[col] > upper)).sum())
        })
    outlier_df = pd.DataFrame(outlier_rows).sort_values('outlier_count', ascending=False)
    outlier_analysis(df, numeric_cols)
    corr = correlation_analysis(df, numeric_cols)

    summary_lines.append('')
    summary_lines.append('Outputs created:')
    summary_lines.append('- basic_statistics.csv')
    summary_lines.append('- numeric_statistics.csv')
    summary_lines.append('- trend_summary.csv')
    summary_lines.append('- outlier_summary.csv')
    summary_lines.append('- correlation_matrix.csv')
    summary_lines.append('- correlation_heatmap.png')
    summary_lines.append('- outlier_boxplots.png')
    summary_lines.append('- task3_findings.md')

    save_markdown(OUT_DIR / 'task3_report.md', summary_lines)
    summarize_findings(df, numeric_cols, cat_cols, corr, outlier_df)

    print('EDA complete.')
    print(f'Report saved to: {OUT_DIR / "task3_report.md"}')


if __name__ == '__main__':
    main()
