import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main(df,selected_option):
    running_books_df=df[df['status']=='Ongoing']
    percent_chapter_or_page= st.selectbox('How Do you want to track your progress?',["Percentagewise",'Chapterwise','Pagewise'])
    
    if selected_option == "Show Data":
        st.subheader("Raw Data")
        if percent_chapter_or_page=='Percentagewise':
            percentile=pd.DataFrame(columns=['title','completed'],data=calculate_percentile(running_books_df))
            st.dataframe(percentile)
        elif percent_chapter_or_page=='Chapterwise':
            chapterwise=pd.DataFrame(columns=['title', 'current_chapter','total_chapters'],data=running_books_df)
            st.dataframe(chapterwise)
        elif percent_chapter_or_page=='Pagewise':
            pagewise=pd.DataFrame(columns=['title','current_page','total_pages'],data=running_books_df)
            st.dataframe(pagewise)
    
    elif selected_option=="Show Chart":
        st.subheader("Charts")
        sns.set(rc={'axes.facecolor':'#0e1117','figure.facecolor':'#0e1117'})

        if percent_chapter_or_page=='Percentagewise':
            st.spinner('Loading...')
            fig=plt.figure(figsize=(15,10))
            plt.title("Percentage of Progress",color='white',size=30)
            sns.barplot(x='title', y='total',color='#262730',edgecolor="1",data=calculate_percentile(running_books_df))
            sns.barplot(x='title', y='completed',color='#c42b2b',edgecolor="1",data=calculate_percentile(running_books_df))
            plt.xlabel('Books',color='white',size=20)
            plt.ylabel('Pages',color='white',size=20)
            plt.tick_params(axis='both', colors='white',size=20)
    
        if percent_chapter_or_page=='Chapterwise':
            st.empty()
            chapterwise=pd.DataFrame(columns=['title', 'current_chapter','total_chapters'],data=running_books_df)
            fig=fig=plt.figure(figsize=(15,10))
            plt.title("Chapterwise Progress",color='white',size=30)
            sns.barplot(x='title', y='total_chapters',color='#262730',edgecolor="1",data=chapterwise)
            sns.barplot(x='title', y='current_chapter',color='#c42b2b',capsize=.3,edgecolor="1",data=chapterwise)
            plt.xlabel('Books',color='white',size=20)
            plt.ylabel('Chapters',color='white',size=20)
            plt.tick_params(axis='both', colors='white',size=20)

        if percent_chapter_or_page=='Pagewise':
            st.empty()
            pagewise=pd.DataFrame(columns=['title','current_page','total_pages'],data=running_books_df)
            fig=plt.figure(figsize=(15,10))
            plt.title("Pagewise Progress",color='white',size=30)
            sns.barplot(x='title', y='total_pages',color='#262730',edgecolor="1", dodge=False,data=pagewise)
            sns.barplot(x='title', y='current_page',color='#c42b2b',edgecolor="1",dodge=False, data=pagewise)
            plt.xlabel('Books',color='white',size=20)
            plt.ylabel('Pages',color='white',size=20)
            plt.tick_params(axis='both', colors='white',size=20)
                
        st.pyplot(fig)    
     
if __name__ == '__main__':
    st.set_page_config(page_title="Running Books", page_icon="📖")
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
                .css-17ziqus {background-color: brown; visibility: visible}
                body {text-align:center;}
                p{text-align: center;}
                </style>
                <title> Book Tracker </title>
                </head>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    st.header("📖 Ongoing Books")
    st.markdown("Track books that are currently being read...")
    st.sidebar.header(" 📖 Ongoing Books")
    
    @st.cache
    def calculate_percentile(df):
        percentile_df = pd.DataFrame({
            'title': df['title'],
            'completed': (df['current_page'] / df['total_pages']).round(2) * 100,
            'total': 100
        })
        return percentile_df
    
    df=pd.read_csv('./data/books.csv')
    selected_option=st.radio("Select",["Show Chart","Show Data"],horizontal=True)
    main(df,selected_option)

    hide_streamlit_style="""<div class="myFooter">© 2022 Copyright | Made by <a href="https://ziaulkarim.netlify.app" >Md. Ziaul Karim</a></div>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)   