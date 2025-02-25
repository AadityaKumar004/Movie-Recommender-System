import pickle
import streamlit as st
import requests


#def fetch_poster(movie_id):
 #   url = "http://img.omdbapi.com/?apikey=24583cf9&".format(movie_id)
  #  data = requests.get(url)
   # data = data.json()
    #poster_path = data['poster_path']
    #full_path = "http://img.omdbapi.com/?apikey=24583cf9&" + poster_path
    #return full_path 

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    #recommended_movie_posters = []
    
    for i in distances[1:6]:
        # fetch the movie poster
        #movie_id = movies.iloc[i[0]].movie_id
        #recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names #recommended_movie_posters


st.header('Movie Recommender System')

movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Recommend') :
    recommendation = recommend(selected_movie)
    for i in recommendation:
        st.write(i)




