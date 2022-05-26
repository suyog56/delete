import streamlit as st
import pickle 
import pandas as pd
import requests


movies=pickle.load(open("list.pkl","rb"))
similarity=pickle.load(open("sim.pkl","rb"))

st.title("MOVIE RECOMMENDATION SYSTEM")

options= st.selectbox("Select Movie",movies['title'])

def recommend(movie):
    l=[]
    p=[]
    index = movies[movies[  'title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        p.append(fetch_poster(movies.iloc[i[0]].movie_id))
        l.append(movies.iloc[i[0]].title)
    return l,p
 
def fetch_poster(m_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(m_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
       
    
    
if st.button("Recommend"):
    recommended_movie_names,recommended_movie_posters = recommend(options)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])