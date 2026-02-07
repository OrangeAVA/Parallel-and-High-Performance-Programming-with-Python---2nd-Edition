from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from joblib import dump, load

def main():
    iris = load_iris()
    X, y = iris.data, iris.target

    model = RandomForestClassifier(n_estimators=100, random_state=0)
    model.fit(X, y)

    dump(model, "random_forest_model.joblib")
    print("Model saved -> random_forest_model.joblib")

    loaded = load("random_forest_model.joblib")
    print("Predictions on first 5:", loaded.predict(X[:5]))

if __name__ == "__main__":
    main()
