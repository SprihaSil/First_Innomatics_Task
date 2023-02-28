import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

#absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
#absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR,os.pardir)
#absolute path of directory_of_interest
dir_of_interest= os.path.join(PARENT_DIR,"Resources")

IMAGE_PATH = os.path.join(dir_of_interest,"Images","ipl_pic.jpg")
DATA_PATH = os.path.join(dir_of_interest,"data","ipl.csv")

st.title("Dashboard - IPL Data")
st.header("My first dashboard")
st.subheader("First :red[Innomatics] internship task :heart_eyes: :heart_eyes:")

img = image.imread(IMAGE_PATH)
st.image(img)

df=pd.read_csv(DATA_PATH)
dt1=df.drop(columns=['Unnamed: 18','Unnamed: 19','Unnamed: 20','Unnamed: 21'])
st.subheader('The IPL dataset is shown below:')
st.dataframe(dt1)

toss_won=dt1.iloc[:,3].value_counts()
count=list(toss_won.values)
teams=list(toss_won.index)
d1={"teams":teams,"count_of_tosses_won":count}
d2=pd.DataFrame(d1)

match_won=dt1.iloc[:,7].value_counts()
count1=list(match_won.values)
teams1=list(match_won.index)
d3={"teams":teams1,"count_of_matches_won":count1}
d4=pd.DataFrame(d3)

st.subheader("No. of tosses won by different teams")
fig_1=px.bar(d2,x="teams",y="count_of_tosses_won")
col1 = st.columns(1)
col1[0].plotly_chart(fig_1,use_container_width=True)

st.subheader("No. of matches won by different teams")
fig_2=px.bar(d4,x="teams",y="count_of_matches_won")
col2 = st.columns(1)
col2[0].plotly_chart(fig_2,use_container_width=True)


bat_ball=st.selectbox ("Select the mode whose frequency is required: ",df['First Batting/Bowling'].unique())
st.write("### The number of times the teams selected",bat_ball)
n=dt1[dt1['First Batting/Bowling']==bat_ball].iloc[:,4].value_counts()[0]
st.write("## ",n)


st.write('#### The box plot of ages of the man of the match while their corresponding team selected',bat_ball)
col3 = st.columns(1)
fig_3=px.box(df[df['First Batting/Bowling']==bat_ball],x="Age")

col3[0].plotly_chart(fig_3,use_container_width=True)

