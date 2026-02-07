from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from joblib import dump, load

def main():
    iris = load_iris()
    X, y = iris.data, iris.target

    try:
        base_model = load("random_forest_model.joblib")
        print("Loaded base model.")
    except:
        base_model = RandomForestClassifier(n_estimators=100, random_state=0)

    params = {
        "n_estimators": [50, 100, 200],
        "max_depth": [None, 10, 20]
    }

    grid = GridSearchCV(base_model, params, cv=5, n_jobs=-1)
    grid.fit(X, y)
    print("Best params:", grid.best_params_)

    best = grid.best_estimator_
    dump(best, "best_random_forest_model.joblib")
    print("Saved best model -> best_random_forest_model.joblib")
    print("Pred (first 5):", best.predict(X[:5]))

if __name__ == "__main__":
    main()
