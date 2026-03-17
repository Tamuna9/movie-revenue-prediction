import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

from data_preprocessing import load_and_prepare_data


def train_model():
    df = load_and_prepare_data("data/tmdb_5000_movies.csv")

    X = df[[
        "budget",
        "runtime",
        "vote_average",
        "vote_count",
        "popularity",
        "release_year"
    ]]

    y = df["revenue"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"MAE: {mae:.2f}")
    print(f"R2 Score: {r2:.4f}")

    joblib.dump(model, "models/movie_model.pkl")
    print("Model saved to models/movie_model.pkl")


if __name__ == "__main__":
    train_model()