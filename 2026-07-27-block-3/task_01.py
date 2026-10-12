from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import GridSearchCV, train_test_split


def load_data(random_state=42, test_size=0.25):
    diabetes = load_diabetes()
    return train_test_split(
        diabetes["data"], diabetes["target"],
        train_size=1 - test_size, test_size=test_size, random_state=random_state,
    )


def train_tuned_ridge(X_train, y_train, alphas=(0.01, 0.1, 0.15, 0.2, 0.5)):
    search = GridSearchCV(Ridge(), {"alpha": list(alphas)})
    search.fit(X_train, y_train)
    return search


def train_random_forest(X_train, y_train):
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model


def evaluate(model, X_test, y_test):
    predictions = model.predict(X_test)
    return root_mean_squared_error(y_test, predictions)


def main():
    X_train, X_test, y_train, y_test = load_data()

    ridge_model = train_tuned_ridge(X_train, y_train)
    forest_model = train_random_forest(X_train, y_train)

    ridge_rmse = evaluate(ridge_model, X_test, y_test)
    forest_rmse = evaluate(forest_model, X_test, y_test)

    print("Ridge RMSE:", ridge_rmse)
    print("RandomForest RMSE:", forest_rmse)


if __name__ == "__main__":
    main()
