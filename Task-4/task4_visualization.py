"""
Task 4 - Data Visualization

This script loads the cleaned dataset and creates charts to communicate
the main patterns clearly.
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


def save_note(path, lines):
    path.write_text('\n'.join(lines), encoding='utf8')


def style_plot(title):
    plt.title(title, fontsize=14, weight='bold')
    plt.tight_layout()


def main():
    input_file = get_input_file()
    if not input_file.exists():
        print(f'Input file not found: {input_file}')
        return

    df = load_data(input_file)

    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    cat_cols = [c for c in df.columns if pd.api.types.is_string_dtype(df[c]) or str(df[c].dtype) == 'category']

    outputs = []

    # 1. Gender count plot
    if 'gender' in df.columns:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.countplot(data=df, x='gender', hue='gender', palette=['#6b8f71', '#a3c4bc'], legend=False, ax=ax)
        ax.set_xlabel('Gender')
        ax.set_ylabel('Count')
        style_plot('Gender Distribution')
        out = OUT_DIR / 'gender_distribution.png'
        plt.savefig(out, dpi=150)
        plt.close(fig)
        outputs.append(out.name)

    # 2. Platform usage count plot
    if 'platform_usage' in df.columns:
        fig, ax = plt.subplots(figsize=(8, 5))
        order = df['platform_usage'].value_counts().index
        sns.countplot(data=df, x='platform_usage', hue='platform_usage', order=order, palette='viridis', legend=False, ax=ax)
        ax.set_xlabel('Platform usage')
        ax.set_ylabel('Count')
        style_plot('Platform Usage Distribution')
        out = OUT_DIR / 'platform_usage_distribution.png'
        plt.savefig(out, dpi=150)
        plt.close(fig)
        outputs.append(out.name)

    # 3. Social interaction level plot
    if 'social_interaction_level' in df.columns:
        fig, ax = plt.subplots(figsize=(8, 5))
        order = ['low', 'medium', 'high'] if set(['low', 'medium', 'high']).issubset(set(df['social_interaction_level'].dropna().astype(str).str.lower().unique())) else df['social_interaction_level'].value_counts().index
        sns.countplot(data=df, x='social_interaction_level', hue='social_interaction_level', order=order, palette='Set2', legend=False, ax=ax)
        ax.set_xlabel('Social interaction level')
        ax.set_ylabel('Count')
        style_plot('Social Interaction Level')
        out = OUT_DIR / 'social_interaction_level.png'
        plt.savefig(out, dpi=150)
        plt.close(fig)
        outputs.append(out.name)

    # 4. Numeric histograms
    hist_cols = [c for c in ['age', 'daily_social_media_hours', 'sleep_hours', 'screen_time_before_sleep', 'academic_performance', 'physical_activity', 'stress_level', 'anxiety_level', 'addiction_level'] if c in numeric_cols]
    for col in hist_cols[:4]:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(df[col].dropna(), bins=20, kde=True, color='#5b7db1', ax=ax)
        ax.set_xlabel(col.replace('_', ' ').title())
        ax.set_ylabel('Frequency')
        style_plot(f'Distribution of {col.replace("_", " ").title()}')
        out = OUT_DIR / f'{col}_histogram.png'
        plt.savefig(out, dpi=150)
        plt.close(fig)
        outputs.append(out.name)

    # 5. Correlation heatmap
    if numeric_cols:
        corr = df[numeric_cols].corr()
        fig, ax = plt.subplots(figsize=(11, 8))
        sns.heatmap(corr, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
        style_plot('Correlation Heatmap')
        out = OUT_DIR / 'correlation_heatmap.png'
        plt.savefig(out, dpi=150)
        plt.close(fig)
        outputs.append(out.name)

    # 6. Relationship between social media and sleep
    if 'daily_social_media_hours' in numeric_cols and 'sleep_hours' in numeric_cols:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.scatterplot(data=df, x='daily_social_media_hours', y='sleep_hours', hue='depression_label' if 'depression_label' in df.columns else None, palette='Set1', ax=ax)
        ax.set_xlabel('Daily Social Media Hours')
        ax.set_ylabel('Sleep Hours')
        style_plot('Social Media Use vs Sleep Hours')
        out = OUT_DIR / 'social_media_vs_sleep.png'
        plt.savefig(out, dpi=150)
        plt.close(fig)
        outputs.append(out.name)

    # 7. Short report
    report_lines = [
        'Task 4 - Data Visualization',
        '',
        f'Input file: {input_file.name}',
        f'Dataset shape: {df.shape[0]} rows x {df.shape[1]} columns',
        f'Numeric columns: {len(numeric_cols)}',
        f'Categorical columns: {len(cat_cols)}',
        '',
        'Charts created:',
    ]
    for item in outputs:
        report_lines.append(f'- {item}')

    report_lines.extend([
        '',
        'Key insights:',
        '- Bar charts show the distribution of categorical columns.',
        '- Histograms show the shape of numeric features.',
        '- The correlation heatmap shows how numeric columns relate to each other.',
        '- The scatter plot compares social media use and sleep hours.',
    ])

    save_note(OUT_DIR / 'task4_visual_report.md', report_lines)

    print('Task 4 visualization complete.')
    print(f'Report saved to: {OUT_DIR / "task4_visual_report.md"}')


if __name__ == '__main__':
    main()
