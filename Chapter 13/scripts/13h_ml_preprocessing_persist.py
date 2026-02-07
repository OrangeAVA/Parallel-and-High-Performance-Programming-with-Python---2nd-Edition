from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from joblib import dump, load

def main():
    iris = load_iris()
    X, y = iris.data, iris.target

    try:
        X_scaled = load("dataset_transformed.joblib")
        scaler = load("scaler.joblib")
        print("Loaded transformed dataset & scaler.")
    except:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        dump(X_scaled, "dataset_transformed.joblib")
        dump(scaler, "scaler.joblib")
        print("Saved transformed dataset & scaler.")

    try:
        best = load("best_random_forest_model.joblib")
        print("Loaded best model.")
    except:
        raise RuntimeError("Run 13g_ml_gridsearch_parallel.py first to create best model.")

    print("Pred (first 5 on scaled):", best.predict(X_scaled[:5]))

if __name__ == "__main__":
    main()
