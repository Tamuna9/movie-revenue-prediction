import joblib
import pandas as pd


def predict_revenue(
    budget: float,
    runtime: float,
    vote_average: float,
    vote_count: float,
    popularity: float,
    release_year: int
):
    model = joblib.load("models/movie_model.pkl")

    input_data = pd.DataFrame([{
        "budget": budget,
        "runtime": runtime,
        "vote_average": vote_average,
        "vote_count": vote_count,
        "popularity": popularity,
        "release_year": release_year
    }])

    prediction = model.predict(input_data)[0]
    return prediction


if __name__ == "__main__":
    result = predict_revenue(
        budget=150000000,
        runtime=130,
        vote_average=7.5,
        vote_count=12000,
        popularity=80,
        release_year=2020
    )

    print(f"Predicted revenue: {result:.2f}")