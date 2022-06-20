import streamlit as st
import pandas as pd
st.set_page_config(page_title="Upcoming",page_icon="🆕")
df=pd.read_csv('./data/books.csv')
st.header("Books that you're planning to read ahead.")
data=df[df['status']=='Upcoming']

data=data.sort_values(by=['total_pages'],ascending=True)
st.dataframe(data)

st.sidebar.header("🆕 Upcoming books")

hide_streamlit_style = """
            <head>
            <style>
            #MainMenu{visibility: hidden;}
            .css-fk4es0{display:none;}
            .css-1lsmgbg {display: none;}
            .myFooter{color:rgba(250, 250, 250, 0.6); margin-top: 150px; text-align: center;}
            .myFooter a{color: rgb(255, 75, 75); font-weight: bolder;}
            .css-10trblm{color:rgb(255, 75, 75); text-align:center;}
            .css-16huue1 {color:rgb(255, 75, 75); font-size:18px;}
            .css-v37k9u p{color:#edf5e1; font-size: 18px;}
            .css-1q8dd3e{color:rgb(255, 75, 75);}
            .css-1q8dd3e:hover{color:#edf5e1; border-color:rgb(255, 75, 75);}
            .css-ffhzg2 {text-align: center;}
            .css-17ziqus {background-color: brown;}
            </style>
            <title> Book Tracker </title>
            </head>
            <div class="myFooter">© 2022 Copyright | Made by <a href="https://codingwithzk.netlify.app" >Md. Ziaul Karim</a></div>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
