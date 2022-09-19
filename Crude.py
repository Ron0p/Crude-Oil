import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np
import requests 
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(page_title="Crude Oil Analysis", page_icon=":chart_with_upwards_trend:", layout="wide",initial_sidebar_state="expanded")

#dataset 
df = pd.read_csv('CrudeOil.csv')

# Use for lottie animation

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



#Assets

lottie_url = "https://assets5.lottiefiles.com/packages/lf20_2gpl6gdk.json"
lottie_anime = load_lottieurl(lottie_url)

lottie_url = "https://assets5.lottiefiles.com/packages/lf20_PuCnC9.json"
lottie_conclusion = load_lottieurl(lottie_url)


with st.container():
                
    st.title("Crude Oil Analysis")
    st_lottie(lottie_anime,height=300)


            
                
        
with st.container():
            st.write('---')
            left_column,right_column=st.columns(2)
            with left_column:
                st.header("Welcome !")
                st.write("""

                -   In this analysis, I used the CrudeOil.csv file from the kaggle Dataset
                -   In this data Analysis,We will be using various Libraries such as pandas, Numpy, Seaborn & Matplotlib""")
            with right_column:
                st_lottie(lottie_conclusion,height=300)

with st.container():
        st.write('---')
        st.header(" Crude Oil Dataframe")
        df = pd.read_csv("CrudeOil.csv")
        st.dataframe(df.head())
with st.container():
        st.write('---')
        st.header(" last five data value")
        st.dataframe(df.tail())
        st.header(" Shape")
        st.dataframe(df.shape)
        st.header(" Columns")
        st.dataframe(df.columns)
        st.header("statiscal information")
        st.dataframe(df.describe())

        st.header("distribution of data")
        
        plot= df['Open'].plot(kind="hist")
        st.write(plot)
        st.pyplot()



        st.header("missing values")
        st.dataframe(df.isnull().sum())
        st.header("drop useless columns")
        df.drop('Adj Close**' , axis = 1, inplace= True)
        df=df.rename(columns={'Close*':'Close'})
        st.dataframe(df.head())
        st.header("outliear detection")
        plot1= df['Open'].plot(kind='box')
        st.write(plot1)
        st.pyplot()

        sns.boxplot(df['Open'])


        # IQR
        st.subheader('IQR')
        Q1 = df['Open'].quantile(0.25)
        Q3 = df['Open'].quantile(0.75)
        IQR = Q3 - Q1
        IQR

        st.write("---")

        st.subheader('MAX')
        max = Q3 + 1.5*IQR
        max
        st.subheader('MIN')
        min = Q1 - 1.5* IQR
        min

        df1 = df[(min < df['Open']) & (df['Open'] < max)]
        st.subheader("Shape after data cleaning")
        st.dataframe(df1.shape)

        sns.regplot(df1['Open'], df1['Close'])
        plt.show()
        st.pyplot()

        st.header("pearson correlation")
        st.dataframe(df1.corr())
        st.write(sns.heatmap(df1.corr(),annot=True))
        st.pyplot()
        
        st.write("---")