"""
Task 5 - Predictive Model

This script trains a simple classification model to predict depression_label
from the cleaned teen mental health dataset.
"""

from __future__ import annotations

from pathlib import Path
import json
import warnings

import joblib
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


warnings.filterwarnings("ignore", category=FutureWarning)

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
DATA_FILE = BASE_DIR / "data" / "cleaned_teen_mental_health_dataset.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

TARGET_COLUMN = "depression_label"
RANDOM_STATE = 42


def get_input_file() -> Path:
    if DATA_FILE.exists():
        return DATA_FILE
    fallback = ROOT_DIR / "Task-2" / "outputs" / "cleaned_teen_mental_health_dataset.csv"
    if fallback.exists():
        return fallback
    return ROOT_DIR / "Teen_Mental_Health_Dataset.csv"


def load_data(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, low_memory=False)
    except Exception:
        return pd.read_csv(path, encoding="latin1", low_memory=False)


def save_markdown(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines), encoding="utf-8")


def build_preprocessor(features: pd.DataFrame) -> tuple[ColumnTransformer, list[str], list[str]]:
    numeric_columns = features.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns = [column for column in features.columns if column not in numeric_columns]

    numeric_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        [
            ("numeric", numeric_pipeline, numeric_columns),
            ("categorical", categorical_pipeline, categorical_columns),
        ]
    )
    return preprocessor, numeric_columns, categorical_columns


def make_feature_importance_table(model: Pipeline) -> pd.DataFrame:
    preprocessor = model.named_steps["preprocessor"]
    classifier = model.named_steps["classifier"]
    feature_names = preprocessor.get_feature_names_out()
    coefficients = classifier.coef_[0]
    table = pd.DataFrame(
        {
            "feature": feature_names,
            "coefficient": coefficients,
            "absolute_coefficient": [abs(value) for value in coefficients],
        }
    )
    return table.sort_values("absolute_coefficient", ascending=False)


def plot_confusion_matrix(matrix: list[list[int]], output_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues", cbar=False, ax=ax)
    ax.set_xlabel("Predicted label")
    ax.set_ylabel("Actual label")
    ax.set_title("Confusion Matrix")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close(fig)


def plot_roc_curve(y_true: pd.Series, y_score: list[float], output_path: Path) -> float:
    fpr, tpr, _ = roc_curve(y_true, y_score)
    auc_score = roc_auc_score(y_true, y_score)
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(fpr, tpr, label=f"ROC AUC = {auc_score:.3f}", color="#4c78a8")
    ax.plot([0, 1], [0, 1], linestyle="--", color="gray")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("ROC Curve")
    ax.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close(fig)
    return auc_score


def plot_feature_importance(table: pd.DataFrame, output_path: Path, top_n: int = 12) -> None:
    top_features = table.head(top_n).sort_values("absolute_coefficient")
    fig, ax = plt.subplots(figsize=(9, 6))
    colors = ["#d1495b" if value < 0 else "#4c78a8" for value in top_features["coefficient"]]
    ax.barh(top_features["feature"], top_features["coefficient"], color=colors)
    ax.set_xlabel("Coefficient")
    ax.set_ylabel("Feature")
    ax.set_title("Top Model Drivers")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close(fig)


def summarize_model(metrics: dict[str, float], baseline_metrics: dict[str, float], data_shape: tuple[int, int], class_distribution: dict[int, int], outputs: list[str]) -> list[str]:
    report_lines = [
        "# Task 5 - Predictive Model",
        "",
        "## Goal",
        "Build a simple predictive model that estimates `depression_label` from the cleaned dataset.",
        "",
        "## Dataset",
        f"- Rows: {data_shape[0]}",
        f"- Columns: {data_shape[1]}",
        f"- Class distribution: {json.dumps(class_distribution)}",
        "",
        "## Model",
        "- Algorithm: Logistic Regression",
        "- Strategy: Train/test split with stratification",
        "- Preprocessing: Median imputation for numeric fields, most-frequent imputation plus one-hot encoding for categorical fields",
        "- Balance handling: `class_weight='balanced'`",
        "",
        "## Results",
        f"- Accuracy: {metrics['accuracy']:.4f}",
        f"- Precision: {metrics['precision']:.4f}",
        f"- Recall: {metrics['recall']:.4f}",
        f"- F1 score: {metrics['f1']:.4f}",
        f"- ROC AUC: {metrics['roc_auc']:.4f}",
        "",
        "## Baseline",
        f"- Majority-class accuracy: {baseline_metrics['accuracy']:.4f}",
        f"- Majority-class precision: {baseline_metrics['precision']:.4f}",
        f"- Majority-class recall: {baseline_metrics['recall']:.4f}",
        f"- Majority-class F1: {baseline_metrics['f1']:.4f}",
        "",
        "## Outputs",
    ]
    report_lines.extend([f"- {item}" for item in outputs])
    report_lines.extend(
        [
            "",
            "## Insight",
            "The model captures a strong separation signal in the cleaned data and is more useful than a simple always-negative baseline because it identifies positive cases.",
        ]
    )
    return report_lines


def main() -> None:
    input_file = get_input_file()
    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        return

    df = load_data(input_file)
    if TARGET_COLUMN not in df.columns:
        print(f"Target column not found: {TARGET_COLUMN}")
        return

    features = df.drop(columns=[TARGET_COLUMN])
    target = df[TARGET_COLUMN]

    preprocessor, _, _ = build_preprocessor(features)
    X_train, X_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=RANDOM_STATE,
        stratify=target,
    )

    model = Pipeline(
        [
            ("preprocessor", preprocessor),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    class_weight="balanced",
                    solver="liblinear",
                    random_state=RANDOM_STATE,
                ),
            ),
        ]
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    prediction_probabilities = model.predict_proba(X_test)[:, 1]

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions, zero_division=0),
        "recall": recall_score(y_test, predictions, zero_division=0),
        "f1": f1_score(y_test, predictions, zero_division=0),
        "roc_auc": roc_auc_score(y_test, prediction_probabilities),
    }

    baseline = DummyClassifier(strategy="most_frequent")
    baseline.fit(X_train, y_train)
    baseline_predictions = baseline.predict(X_test)
    baseline_metrics = {
        "accuracy": accuracy_score(y_test, baseline_predictions),
        "precision": precision_score(y_test, baseline_predictions, zero_division=0),
        "recall": recall_score(y_test, baseline_predictions, zero_division=0),
        "f1": f1_score(y_test, baseline_predictions, zero_division=0),
    }

    confusion = confusion_matrix(y_test, predictions)
    feature_table = make_feature_importance_table(model)

    metrics_frame = pd.DataFrame([metrics])
    metrics_frame.to_csv(OUTPUT_DIR / "task5_model_metrics.csv", index=False)
    pd.DataFrame([baseline_metrics]).to_csv(OUTPUT_DIR / "task5_baseline_metrics.csv", index=False)
    feature_table.to_csv(OUTPUT_DIR / "task5_feature_importance.csv", index=False)
    pd.DataFrame(
        {
            "actual": y_test.reset_index(drop=True),
            "predicted": pd.Series(predictions),
            "predicted_probability": pd.Series(prediction_probabilities),
        }
    ).to_csv(OUTPUT_DIR / "task5_test_predictions.csv", index=False)

    plot_confusion_matrix(confusion.tolist(), OUTPUT_DIR / "task5_confusion_matrix.png")
    auc_score = plot_roc_curve(y_test, prediction_probabilities, OUTPUT_DIR / "task5_roc_curve.png")
    plot_feature_importance(feature_table, OUTPUT_DIR / "task5_top_drivers.png")

    joblib.dump(model, OUTPUT_DIR / "task5_depression_model.joblib")

    class_distribution = target.value_counts().sort_index().to_dict()
    report_lines = summarize_model(
        {**metrics, "roc_auc": auc_score},
        baseline_metrics,
        df.shape,
        class_distribution,
        [
            "task5_model_metrics.csv",
            "task5_baseline_metrics.csv",
            "task5_feature_importance.csv",
            "task5_test_predictions.csv",
            "task5_confusion_matrix.png",
            "task5_roc_curve.png",
            "task5_top_drivers.png",
            "task5_depression_model.joblib",
        ],
    )
    save_markdown(OUTPUT_DIR / "task5_model_report.md", report_lines)

    print("Task 5 predictive model complete.")
    print(f"Report saved to: {OUTPUT_DIR / 'task5_model_report.md'}")


if __name__ == "__main__":
    main()
