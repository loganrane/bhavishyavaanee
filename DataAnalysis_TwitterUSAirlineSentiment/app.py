# Importing the important libraries
import streamlit as st
import pandas as pd
import numpy as np

# Adding exploratory information for the dashboard
st.title('Sentiment Analysis fo Tweets about US Airlines')
st.sidebar.title('Sentiment Analysis fo Tweets about US Airlines')

st.markdown('This application is a Streamlit dashboard to analyze the sentiment of Tweets. 🐦')
st.sidebar.markdown('This application is a Streamlit dashboard to analyze the sentiment of Tweets. 🐦')

# Importing the data
DATA_PATH = ('./Tweets.csv')

# Cache the data returned by this function to save computational costs
@st.cache(persist=True)
def load_data(DATA_URL):
    data = pd.read_csv(DATA_URL)
    data['tweet_created'] = pd.to_datetime(data['tweet_created'])
    return data

data = load_data(DATA_PATH)

# Add display random tweets as sentiment.
st.sidebar.subheader('Show random Tweet')
random_tweet = st.sidebar.radio('Sentiment', ('positive', 'neutral', 'negative'))
st.sidebar.markdown(data.query('airline_sentiment == @random_tweet')[['text']].sample(n=1).iat[0, 0])