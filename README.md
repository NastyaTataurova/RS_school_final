# RS_school_final

## Description
This repository is a homework assignment for the RS School Machine Learning course.
The project uses the [Forest train dataset](https://www.kaggle.com/competitions/forest-cover-type-prediction). This package allows you to train models ([LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) and [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)) to classify forest categories.

## Usage
1. Clone this repository to your machine.
2. Download [Forest train dataset](https://www.kaggle.com/competitions/forest-cover-type-prediction), save csv locally (default path is data/forest-cover-type-prediction/train.csv in repository's root).
3. Make sure Python 3.9 is installed on your machine.
4. Download poetry with this command:
```bash
bash ./workspace.sh
```
5. Install the project dependencies (run this and following commands in a terminal, from the root of a cloned repository):
```bash
poetry install --no-dev
```
6. Run train with the following command:
```bash
poetry run train -d <path to csv with data> -s <path to save trained model>
```
7. To get a full list of configure additional options:
```bash
poetry run train --help
```
8. Run MLflow UI to see the information about experiments you conducted:
```bash
poetry run mlflow ui
```

## Experiments with models (MLFlow)
The figure below shows the results of experiments with two models. Different hyperparameters were selected for each model, the best quality was obtained by model forest (RandomForestClassifier) with parameters: max_depht = 15 and n_estimators = 100.
<img width="606" alt="image" src="https://user-images.githubusercontent.com/49210968/167652720-ff0ba8cd-f060-4321-b28b-5f51483fe5f7.png">
