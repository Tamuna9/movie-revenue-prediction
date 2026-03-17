import pandas as pd


def load_and_prepare_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    columns_needed = [
        "budget",
        "revenue",
        "runtime",
        "vote_average",
        "vote_count",
        "popularity",
        "release_date"
    ]

    df = df[columns_needed].copy()

    df = df.dropna()

    df = df[
        (df["budget"] > 0) &
        (df["revenue"] > 0) &
        (df["runtime"] > 0)
    ]

    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    df = df.dropna()

    df["release_year"] = df["release_date"].dt.year

    df = df.drop(columns=["release_date"])

    return df


if __name__ == "__main__":
    df = load_and_prepare_data("data/tmdb_5000_movies.csv")
    print(df.head())
    print(df.info())