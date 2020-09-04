# Importing the important libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

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

st.sidebar.markdown('### Number of tweets by sentiment')
select = st.sidebar.selectbox('Visualization Type', ['Histogram', 'Pie Chart'], key='1')

# Create dataframe to plot the graphs
sentiment_count = data['airline_sentiment'].value_counts()
sentiment_count = pd.DataFrame({'Sentiment':sentiment_count.index, 'Tweets':sentiment_count.values})

# Show the charts of sentiment count in the main section
if not st.sidebar.checkbox('Hide', True):
    st.markdown('### Number of tweets by sentiment')
    if select == 'Histogram':
        fig = px.bar(sentiment_count, x='Sentiment', y='Tweets', color='Tweets', height=500)
        st.plotly_chart(fig)
    elif select == 'Pie Chart':
        fig = px.pie(sentiment_count, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)


# -------------------------------------------------------------- #
# ----------- Missing Columns (Latitude and Longitude) --------- #
# -------------------------------------------------------------- #

# Add map to visualize the when and where of the tweets
# Create the data
# st.sidebar.subheader('When and Where are users tweeting from?')
# hour = st.sidebar.slider('Hour of day', 0, 23)
# modified_data = data[data['tweet_created'].dt.hour == hour]
# # Add the plot
# if not st.sidebar.checkbox('Close', True, key='1'):
#     st.markdown('### Tweets locations based on the time of day')
#     st.markdown('%i tweets between %i:00 and %i:00'%(len(modified_data), hour, ((hour+1) % 24)))
#     st.map(modified_data)
#     if st.sidebar.checkbox('Show raw data', False):
#         st.write(modified_data)

# -------------------------------------------------------------- #


# Add graphs for breakdown of airline tweets by sentiment. 
st.sidebar.subheader('Breakdown airline tweets by sentiment')
choice = st.sidebar.multiselect('Pick Airlines', ('US Airways', 'United', 'American', 'Southwest', 'Delta', 'Virgin America'), key='0')

if len(choice) > 0:
    choice_data = data[data.airline.isin(choice)]
    fig_choice = px.histogram(choice_data, x='airline', y='airline_sentiment', histfunc='count', color='airline_sentiment',
                              facet_col='airline_sentiment', labels={'airline_sentiment': 'tweets'}, height=600, width=800)
    st.plotly_chart(fig_choice)



