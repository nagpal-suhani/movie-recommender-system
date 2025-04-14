import streamlit as st
import pickle 
import pandas as pd
import numpy as np
import requests

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies_data = pd.DataFrame(movies_dict)
movies_list = movies_data['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')


api_key = "ffdcdd512fdf7171aa83e7fb43939811"


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=ffdcdd512fdf7171aa83e7fb43939811&language=en-US".format(movie_id))
    data = response.json()
    poster = "https://image.tmdb.org/t/p/original" + data['poster_path']
    return poster 
    

def recommend(movie):
    movie_index = movies_data[movies_data['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x: x[1])[1:6]
    
    recs=[]
    recommended_movies_poster = []
    for i in movies_list:
        rec = movies_data.iloc[i[0]].title
        movie_id = movies_data.iloc[i[0]].id
        recs.append(rec)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recs, recommended_movies_poster

selected_movie_name = st.selectbox('Enter movie name', (movies_list))

if st.button('Recommend'):
    names, posters  = recommend(selected_movie_name)
    st.write("OHH you've seen ", selected_movie_name)
    st.write("then you should watch these - ")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])





