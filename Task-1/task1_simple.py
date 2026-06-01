"""
Task 1 simple dataset exploration

This version is written in a simple style and reads the dataset from the
repository root. It prints basic information and saves a small text report.
"""

from pathlib import Path
import os
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
TASK1_DIR = Path(__file__).resolve().parent
INPUT_FILE = TASK1_DIR / 'data' / 'Teen_Mental_Health_Dataset.csv'
OUT_DIR = Path(__file__).resolve().parent / 'outputs'


def ensure_outdir():
    if not OUT_DIR.exists():
        OUT_DIR.mkdir(parents=True)


def load_data(path):
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.read_csv(path, encoding='latin1')


def basic_info(df):
    print('\n=== Basic Info ===')
    print('Shape:', df.shape)
    print('\nColumns and types:')
    print(df.dtypes)


def show_head(df, n=5):
    print('\n=== First rows ===')
    print(df.head(n))


def missing_summary(df):
    miss = df.isnull().sum()
    miss = miss[miss > 0].sort_values(ascending=False)
    print('\n=== Missing values (columns with missing) ===')
    if miss.empty:
        print('No missing values found.')
    else:
        print(miss)
    return miss


def categorical_overview(df):
    cat_cols = [c for c in df.columns if pd.api.types.is_string_dtype(df[c]) or str(df[c].dtype) == 'category']
    if not cat_cols:
        print('\nNo categorical/object columns found.')
        return {}

    print('\n=== Categorical columns overview (top values) ===')
    top_values = {}
    for c in cat_cols:
        vc = df[c].value_counts(dropna=False).head(10)
        print(f"\nColumn: {c}")
        print(vc)
        top_values[c] = vc.to_dict()
    return top_values


def numeric_summary(df):
    num = df.select_dtypes(include=['number'])
    if num.empty:
        print('\nNo numeric columns found.')
        return None
    print('\n=== Numeric summary ===')
    print(num.describe().T)
    return num.describe().T


def save_simple_report(path, info_lines):
    with open(path, 'w', encoding='utf8') as f:
        f.write('\n'.join(info_lines))


def main():
    ensure_outdir()

    input_file = INPUT_FILE
    if not input_file.exists():
        input_file = BASE_DIR / 'Teen_Mental_Health_Dataset.csv'

    if not input_file.exists():
        print(f'Input file not found: {input_file}')
        return

    print('Loading data...')
    df = load_data(input_file)

    basic_info(df)
    show_head(df, n=5)
    miss = missing_summary(df)
    top_values = categorical_overview(df)
    num_desc = numeric_summary(df)

    lines = []
    lines.append(f'Dataset: {input_file.name}')
    lines.append(f'Rows,Columns: {df.shape}')
    lines.append('')
    lines.append('Columns and types:')
    for c, t in df.dtypes.items():
        lines.append(f'- {c}: {t}')

    lines.append('')
    lines.append('Missing values (top):')
    if miss.empty:
        lines.append('- None')
    else:
        for c, v in miss.items():
            lines.append(f'- {c}: {int(v)} missing')

    lines.append('')
    lines.append('Top categorical values (sample):')
    if top_values:
        for c, vc in top_values.items():
            lines.append(f'- {c}:')
            for val, cnt in list(vc.items())[:5]:
                lines.append(f'    - {val}: {cnt}')
    else:
        lines.append('- None')

    lines.append('')
    lines.append('Numeric summary (first 10 columns if present):')
    if num_desc is not None:
        for i, (col, row) in enumerate(num_desc.iterrows()):
            if i >= 10:
                break
            count_value = int(row['count']) if not pd.isna(row['count']) else 'NA'
            lines.append(f"- {col}: count={count_value}, mean={row.get('mean', 'NA')}")
    else:
        lines.append('- None')

    report_path = OUT_DIR / 'simple_report.txt'
    save_simple_report(report_path, lines)
    print(f"\nSimple report written to: {report_path}")


if __name__ == '__main__':
    main()
