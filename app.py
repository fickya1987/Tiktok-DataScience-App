#Import streamlit dependancy
import streamlit as st
#Import pandas to load the analytics data
import pandas as pd
#Import subprocess to run tiktok script from command line
from subprocess import call
#Import plotly for visualization
import plotly.express as px
from PIL import Image

#Set page width
st.set_page_config(layout='wide')

#Importing logo image
image = Image.open('logo.png')

#Create a sidebar
st.sidebar.image(image, caption='Tiktok Analytics' ,use_column_width=True)

st.sidebar.markdown("This dashboard allows you to analyze tiktok data by hashtag")
st.sidebar.markdown("Get started by <ol><li>Enter the <i>hashtag</i> you wish to analyse</li> <li>Hit <i>Get Data</i>.</li> <li>Get analyzing</li></ol>",
                    unsafe_allow_html=True)
st.sidebar.markdown("The Tiktok Unofficial API has no search by hashtag api call available. The app is currently showing hardcoded data")


#Getting user input for hashtag
hashtag = st.text_input('Search for a hashtag ', value="")

#Search button
if st.button('Get Data'):
    st.write('Recieved tiktok data on #'+hashtag)
    call(['python', 'tiktok.py', hashtag])   
    #Load in existing data to test it out
    df = pd.read_csv('tiktokdata.csv') 
    
    #Plotly visualization 
    fig = px.histogram(df, x='desc', hover_data=['desc'], y='stats_diggCount', height=300)
    st.plotly_chart(fig, use_container_width=True)
    
    #Split columns
    left_col, right_col = st.columns(2)
    
    #First chart - video stats
    scatter1 = px.scatter(df, x='stats_shareCount', y='stats_commentCount', hover_data=['desc'], size='stats_playCount', color='stats_playCount')
    left_col.plotly_chart(scatter1, use_container_width=True)
    
    #Second chart - video stats
    scatter2 = px.scatter(df, x='author_nickname', y='authorStats_videoCount', hover_data=['author_signature'], size='authorStats_followerCount', color='authorStats_followerCount')
    right_col.plotly_chart(scatter2, use_container_width=True)
    
    #Area graph
    fig2 = px.area(df, x="video_duration", y="stats_shareCount", color="author_nickname", line_group="author_nickname")
    st.plotly_chart(fig2, use_container_width=True)
    
    
    
    #Show tabular dataframe in streamlit(Raw format)
    df 

