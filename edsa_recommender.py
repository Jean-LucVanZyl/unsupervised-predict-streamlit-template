"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():
    st.sidebar.title("Movie Recommendation System")
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Welcome","Recommender System", "Team","Process","Conclusion"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm doesn't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm doesn't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    

    if page_selection == "Welcome":
        st.title("Welcome to your Movie Recommender App")

        st.image('Images/movie_night1.jpg',width = 640)

        st.write("The aim for this application is to give users the ability to discover new movies based on their 3 favourite movies.")

        about = st.sidebar.checkbox("About")
        if about:
            st.title("Problem Statement")
            st.markdown(" ")
    
    if page_selection == "Team":
        st.title("Meet the team")
    #Create checkbox to display team member names
    
                
        st.subheader("**Unsupervised AE4**")
        st.write("The team:")
        st.markdown("* Jean-Luc Van Zyl- Team Coordinator")
        st.markdown("* Pearl Matsane")
        st.markdown("* Lydia Lehutjo")
        st.markdown("* Tyrone Khanyile")
        st.markdown("* Katleho Mphuthi")

        st.subheader("**Superviser**")
        st.write("Ali Elimam")
    if page_selection == "Process":
        st.sidebar.subheader("Exploratory Data Analysis")
        
        source = st.sidebar.checkbox("Data Source")
        if source:
            st.subheader("Where did we get the data from?")
        
        look = st.sidebar.checkbox("Data")
        if look:
            st.subheader("What did the data consists?")
        user = st.sidebar.checkbox("User analysis")
        if user:
            st.subheader("Insights from users")
        movies = st.sidebar.checkbox("Movie analysis")
        if movies:
            st.subheader("Insights from Movies")
        conclusion = st.sidebar.checkbox("General Insights")
        if conclusion:
            st.subheader("General Insights from EDA")
        st.sidebar.subheader("Modelling")
        model = st.sidebar.checkbox("Content-based")
        if model:
            st.subheader("Content based Model")
    
    if page_selection == "Conclusion":
        st.subheader("Overall conclusion")
        st.subheader("What can this do for your Business?")

        
        st.title("Enjoy your movies! ")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    

if __name__ == '__main__':
    main()
