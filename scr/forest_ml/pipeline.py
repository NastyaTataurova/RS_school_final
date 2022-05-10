from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def create_pipeline(
    use_scaler: bool, max_iter: int, logreg_C: float, random_state: int, model: str, max_depth: int, n_estimators: int
) -> Pipeline:
    pipeline_steps = []
    if use_scaler:
        pipeline_steps.append(("scaler", StandardScaler()))
    if model == 'logreg':
        pipeline_steps.append(
            (
                "classifier",
                LogisticRegression(
                    random_state=random_state,
                    max_iter=max_iter,
                    C=logreg_C
                ),
            )
        )
    elif model == 'forest':
        pipeline_steps.append(
            (
                "classifier",
                RandomForestClassifier(
                    random_state=random_state,
                    n_estimators=n_estimators,
                    max_depth=max_depth
                ),
            )
        )
    
    return Pipeline(steps=pipeline_steps)