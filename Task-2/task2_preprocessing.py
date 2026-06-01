"""
Task 2 - Data Cleaning and Preprocessing

This script loads the dataset, cleans it, and saves a cleaned CSV plus a
short report.
"""

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
INPUT_FILE = BASE_DIR / 'data' / 'Teen_Mental_Health_Dataset.csv'
OUT_DIR = BASE_DIR / 'outputs'
OUT_DIR.mkdir(exist_ok=True)


def get_input_file():
    if INPUT_FILE.exists():
        return INPUT_FILE
    return ROOT_DIR / 'Teen_Mental_Health_Dataset.csv'


def load_data(path):
    try:
        return pd.read_csv(path, low_memory=False)
    except Exception:
        return pd.read_csv(path, encoding='latin1', low_memory=False)


def clean_column_names(df):
    df.columns = [
        str(col).strip().lower().replace(' ', '_').replace('-', '_')
        for col in df.columns
    ]
    return df


def clean_text_values(df):
    for col in df.columns:
        if pd.api.types.is_object_dtype(df[col]) or pd.api.types.is_string_dtype(df[col]):
            df[col] = df[col].astype('string').str.strip()
            df[col] = df[col].replace('', pd.NA)
    return df


def convert_numeric_values(df):
    for col in df.columns:
        if pd.api.types.is_object_dtype(df[col]) or pd.api.types.is_string_dtype(df[col]):
            continue
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def handle_missing_values(df):
    missing_before = df.isna().sum().sum()

    for col in df.columns:
        if df[col].isna().any():
            if pd.api.types.is_numeric_dtype(df[col]):
                fill_value = df[col].median()
                df[col] = df[col].fillna(fill_value)
            else:
                mode_values = df[col].mode(dropna=True)
                fill_value = mode_values.iloc[0] if not mode_values.empty else 'Unknown'
                df[col] = df[col].fillna(fill_value)

    missing_after = df.isna().sum().sum()
    return df, int(missing_before), int(missing_after)


def remove_duplicates(df):
    duplicates_before = int(df.duplicated().sum())
    df = df.drop_duplicates().reset_index(drop=True)
    duplicates_after = int(df.duplicated().sum())
    return df, duplicates_before, duplicates_after


def format_data(df):
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            non_missing = df[col].dropna()
            if not non_missing.empty and (non_missing % 1 == 0).all():
                df[col] = df[col].round().astype('Int64')
    return df


def save_report(path, lines):
    path.write_text('\n'.join(lines), encoding='utf8')


def main():
    input_file = get_input_file()

    if not input_file.exists():
        print(f'Input file not found: {input_file}')
        return

    print('Loading dataset...')
    df = load_data(input_file)

    rows_before, cols_before = df.shape
    df = clean_column_names(df)
    df = clean_text_values(df)
    df = convert_numeric_values(df)
    df, missing_before, missing_after = handle_missing_values(df)
    df, duplicates_before, duplicates_after = remove_duplicates(df)
    df = format_data(df)

    output_file = OUT_DIR / 'cleaned_teen_mental_health_dataset.csv'
    df.to_csv(output_file, index=False)

    report_lines = [
        'Task 2 - Data Cleaning and Preprocessing',
        '',
        f'Input file: {input_file.name}',
        f'Original shape: {rows_before} rows x {cols_before} columns',
        f'Cleaned shape: {df.shape[0]} rows x {df.shape[1]} columns',
        '',
        'Cleaning steps:',
        '- Column names were standardized to lowercase with underscores.',
        '- Text values were stripped of extra spaces.',
        '- Numeric columns were converted to numeric type when possible.',
        '- Missing values were filled using median for numeric columns and mode for text columns.',
        '- Duplicate rows were removed.',
        '- Numeric columns that contained whole numbers were formatted as integers.',
        '',
        'Results:',
        f'- Missing values before cleaning: {missing_before}',
        f'- Missing values after cleaning: {missing_after}',
        f'- Duplicate rows before cleaning: {duplicates_before}',
        f'- Duplicate rows after cleaning: {duplicates_after}',
        '',
        f'Cleaned dataset saved to: {output_file}',
    ]

    save_report(OUT_DIR / 'task2_cleaning_report.txt', report_lines)

    print('Cleaning finished.')
    print(f'Cleaned file saved to: {output_file}')
    print(f'Report saved to: {OUT_DIR / "task2_cleaning_report.txt"}')


if __name__ == '__main__':
    main()
