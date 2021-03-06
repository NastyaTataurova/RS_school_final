from pathlib import Path
from joblib import dump

import click
import mlflow
import mlflow.sklearn
# from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.model_selection import cross_val_score

from .data import get_dataset
from .pipeline import create_pipeline


@click.command()
@click.option(
    "-d",
    "--dataset-path",
    default="data/forest-cover-type-prediction/train.csv",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    show_default=True,
)
@click.option(
    "-s",
    "--save-model-path",
    default="data/model.joblib",
    type=click.Path(dir_okay=False, writable=True, path_type=Path),
    show_default=True,
)
@click.option(
    "--random-state",
    default=42,
    type=int,
    show_default=True,
)
@click.option(
    "--test-split-ratio",
    default=0.2,
    type=click.FloatRange(0, 1, min_open=True, max_open=True),
    show_default=True,
)
@click.option(
    "--use-scaler",
    default=True,
    type=bool,
    show_default=True,
)
@click.option(
    "--max-iter",
    default=100,
    type=int,
    show_default=True,
)
@click.option(
    "--logreg-c",
    default=1.0,
    type=float,
    show_default=True,
)
@click.option(
    "--model",
    default='logreg',
    type=str,
    show_default=True,
)
@click.option(
    "--max_depth",
    default=10,
    type=int,
    show_default=True,
)
@click.option(
    "--n_estimators",
    default=100,
    type=int,
    show_default=True,
)
def train(
    dataset_path: Path,
    save_model_path: Path,
    random_state: int,
    test_split_ratio: float,
    use_scaler: bool,
    max_iter: int,
    logreg_c: float,
    model: str,
    max_depth: int,
    n_estimators: int,
) -> None:
    features_train, features_val, target_train, target_val = get_dataset(
        dataset_path,
        random_state,
        test_split_ratio,
    )
    with mlflow.start_run():
        pipeline = create_pipeline(use_scaler, max_iter, logreg_c, random_state, model, max_depth, n_estimators)
        pipeline.fit(features_train, target_train)
        accuracy = cross_val_score(pipeline, features_val, target_val, scoring = "accuracy", cv=5).mean()
        recall = cross_val_score(pipeline, features_val, target_val, scoring = "recall_weighted", cv=5).mean()
        precision = cross_val_score(pipeline, features_val, target_val, scoring = "precision_weighted", cv=5).mean()
        f1 = cross_val_score(pipeline, features_val, target_val, scoring = "f1_weighted", cv=5).mean() 
        mlflow.log_param("use_scaler", use_scaler)
        mlflow.log_param("max_iter", max_iter)
        mlflow.log_param("logreg_c", logreg_c)
        mlflow.log_param("model", model)
        mlflow.sklearn.log_model("model", model)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("f1", f1)
        click.echo(f"Accuracy: {accuracy}.")
        click.echo(f"Recall: {recall}.")
        click.echo(f"Precision: {precision}.")
        click.echo(f"F1-score: {f1}.")
        dump(pipeline, save_model_path)
        click.echo(f"Model is saved to {save_model_path}.")