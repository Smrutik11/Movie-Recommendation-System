import streamlit as st
import pickle
import os
import pandas as pd


MODEL_PATH = "models/svd_model.pkl"
DATA_PATH = "data/ml-100k/u.item"


@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as file:
        return pickle.load(file)


@st.cache_data
def load_movies():
    movie_cols = [
        "movie_id",
        "title",
        "release_date",
        "video_release_date",
        "IMDb_URL",
        "unknown",
        "Action",
        "Adventure",
        "Animation",
        "Children",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama",
        "Fantasy",
        "Film-Noir",
        "Horror",
        "Musical",
        "Mystery",
        "Romance",
        "Sci-Fi",
        "Thriller",
        "War",
        "Western"
    ]

    movies = pd.read_csv(
        DATA_PATH,
        sep="|",
        names=movie_cols,
        encoding="latin-1",
        header=None
    )

    return movies


def get_recommendations(model, movies, user_id, top_n=10):
    recommendations = []

    for movie_id in movies["movie_id"]:
        prediction = model.predict(user_id, movie_id)

        recommendations.append(
            (movie_id, prediction.est)
        )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    top_movies = recommendations[:top_n]

    results = []

    for movie_id, score in top_movies:
        title = movies.loc[
            movies["movie_id"] == movie_id,
            "title"
        ].values[0]

        results.append(
            {
                "Movie": title,
                "Predicted Rating": round(score, 2)
            }
        )

    return pd.DataFrame(results)


st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)


st.title("🎬 Movie Recommendation System")

st.markdown(
    """
    A collaborative filtering recommendation system
    using Matrix Factorization (SVD).
    """
)

st.divider()


user_id = st.number_input(
    "Enter User ID",
    min_value=1,
    max_value=943,
    value=1,
    step=1
)


top_n = st.slider(
    "Number of Recommendations",
    min_value=5,
    max_value=20,
    value=10
)


if st.button("Get Recommendations"):

    try:
        model = load_model()
        movies = load_movies()

        recommendations = get_recommendations(
            model,
            movies,
            user_id,
            top_n
        )

        st.subheader(
            f"Top {top_n} Recommendations"
        )

        st.dataframe(
            recommendations,
            use_container_width=True,
            hide_index=True
        )

    except FileNotFoundError:

        st.error(
            "Model or dataset files are missing. "
            "Please check the project structure."
        )

    except Exception as e:

        st.error(f"Error: {e}")
