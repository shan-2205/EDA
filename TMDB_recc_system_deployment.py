





### first show the codes of dumping model in Jupyter Notebook..



import streamlit as st
import pandas as pd
import joblib

# --- Load Data and Models ---
# Using st.cache_data for DataFrames and st.cache_resource for models



def load_data(file_path):
    data = pd.read_csv(file_path + "/" + 'movie_data_for_app.csv')
    dataframe = pd.read_csv(file_path + "/" + 'movie_dataframe_for_app.csv')
    return data, dataframe


def load_models(file_path):
    tfv = joblib.load(file_path + "/" + "tfidf_vectorizer.pkl")
    sig = joblib.load(file_path + "/" + "sigmoid_kernel.pkl")
    return tfv, sig

# Load everything ( dataframes , models)
data, dataframe = load_data(r"R:\2.. Entire_Data_Science_Projects\4.. Recommendation_systems\1..TMDB\datasets")
tfv, sig = load_models(r"R:\2.. Entire_Data_Science_Projects\4.. Recommendation_systems\1..TMDB\datasets") 








# --- Recommendation Function ---
def give_recommendations(movie_title, model, data, dataframe):
    if movie_title not in data['original_title'].values:
        return "Movie not found in our database."

    indices = pd.Series(data=data.index, index=data['original_title'])
    idx = indices[movie_title]

    # Get similarity scores and sort them
    model_scores = list(enumerate(model[idx]))
    model_scores_sorted = sorted(model_scores, key=lambda x: x[1], reverse=True)

    # Get the top 10 similar movies (excluding itself)
    top_10_movies = model_scores_sorted[1:11]

    # Get movie titles based on indices
    movie_indices = [i[0] for i in top_10_movies]
    return dataframe['original_title'].iloc[movie_indices]







# --- Streamlit App ---

## set_page_config() : configure the basic settings of your web application page.
## page_title = "Bitcoin Dashboard":
## This sets the title that appears in your browser tab or window..
## layout = "centered": , This sets the layout of the app to be centered (content appears in the middle of the page).
# --- Configuration ---



# --- Streamlit App Layout ---
st.set_page_config(page_title="Simple Movie Recommender", layout="centered")

st.title("🎬 Simple Movie Recommender")
## 🎬 - movie emoji emoji

st.write("Find movies similar to your favorite one!")

# Get list of movies for the dropdown
movie_list = data['original_title'].sort_values().tolist()
## sort_values() : to sort movies name alphabatically 


# Selectbox for user to choose a movie
selected_movie = st.selectbox("Select a movie:", movie_list)

# Button to trigger recommendations
if st.button("Get Recommendations"): ## if user clicks on Get Recommendations button, the code inside the block runs.
    if selected_movie: ## if the user has selected a movie.
        recommendations = give_recommendations(selected_movie, sig, data, dataframe)

        st.subheader("Movies similar to : " + selected_movie)
        for i, movie in enumerate(recommendations):
            st.write(str(i+1) + ". " + movie)

st.markdown("---") ## to add dotted horizontal line 
st.markdown("This app uses content-based filtering.")







## open powershell prompt : 
## cd "R:/2.. Entire_Data_Science_Projects/4.. Recommendation_systems/1..TMDB/"
## streamlit run TMDB_recc_system_deployment.py






