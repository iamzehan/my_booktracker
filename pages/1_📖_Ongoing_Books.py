import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Running Books", page_icon="📖")
df=pd.read_csv('./data/books.csv')
st.header("📖 Ongoing Books")
st.markdown("Track books that are currently being read...")
st.sidebar.header(" 📖 Ongoing Books")

selected_option=st.radio("Select",["Show Data","Show Chart"],horizontal=True)

running_books_df=df[df['status']=='Ongoing']
chapter_or_page= st.selectbox('How Do you want to track your progress?',['Chapterwise','Pagewise'])
if selected_option == "Show Data":
    st.subheader("Raw Data")
    if chapter_or_page=='Chapterwise':
        chapterwise=pd.DataFrame(columns=['title', 'current_chapter','total_chapters'],data=running_books_df)
        st.dataframe(chapterwise)
    elif chapter_or_page=='Pagewise':
        pagewise=pd.DataFrame(columns=['title','current_page','total_pages'],data=running_books_df)
        st.dataframe(pagewise)
elif selected_option=="Show Chart":
    st.subheader("Charts")
    if chapter_or_page=='Chapterwise':
        chapterwise=pd.DataFrame(columns=['title', 'current_chapter','total_chapters'],data=running_books_df)
        fig=fig=plt.figure(figsize=(15,10))
        plt.title("Chapterwise Progress",color='white',size=30)
        sns.barplot(x='title', y='total_chapters',color='#262730',edgecolor="1",data=chapterwise)
        sns.barplot(x='title', y='current_chapter',color='#c42b2b',capsize=.3,edgecolor="1",data=chapterwise)
        plt.xlabel('Books',color='white',size=20)
        plt.ylabel('Chapters',color='white',size=20)
        plt.tick_params(axis='both', colors='white',size=20)
        sns.set(rc={'axes.facecolor':'#0e1117', 'figure.facecolor':'#0e1117'})
        st.pyplot(fig)
    elif chapter_or_page=='Pagewise':
        pagewise=pd.DataFrame(columns=['title','current_page','total_pages'],data=running_books_df)
        fig=plt.figure(figsize=(15,10))
        plt.title("Pagewise Progress",color='white',size=30)
        sns.barplot(x='title', y='total_pages',color='#262730',edgecolor="1", dodge=False,data=pagewise)
        sns.barplot(x='title', y='current_page',color='#c42b2b',edgecolor="1",dodge=False, data=pagewise)
        plt.xlabel('Books',color='white',size=20)
        plt.ylabel('Pages',color='white',size=20)
        plt.tick_params(axis='both', colors='white',size=20)
        sns.set(rc={'axes.facecolor':'#0e1117','figure.facecolor':'#0e1117'})
        st.pyplot(fig)


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
            .css-17ziqus {background-color: brown;}
            body {text-align:center;}
            p{text-align: center;}
            </style>
            <title> Book Tracker </title>
            </head>
            <div class="myFooter">© 2022 Copyright | Made by <a href="https://codingwithzk.netlify.app" >Md. Ziaul Karim</a></div>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
