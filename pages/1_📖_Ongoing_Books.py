import datetime
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

@st.cache(allow_output_mutation=True)
def calculate_percentile(df):
    percentile_df = pd.DataFrame({
        'title': df['title'],
        'completed': (df['current_page'] / df['total_pages']).round(2) * 100
    })
    return percentile_df
        
def addlabels(x,y,data,format=False):
    x,y = list(data[x]),list(data[y])
    for i in range(len(x)):
        if format:
            plt.text(i, round(y[i]//2), str(round(y[i]))+"%", ha = 'center',fontsize='large', color='white')
        else:
            plt.text(i, round(y[i]//2), round(y[i]), ha = 'center',fontsize='medium', color='white')
            
def main(running_books_df,selected_option):
    percent_chapter_or_page= st.selectbox('How Do you want to track your progress?',["Percentagewise",'Chapterwise','Pagewise'])
    data = None
    if selected_option == "Show Data":
        if percent_chapter_or_page=='Percentagewise':
            data = calculate_percentile(running_books_df)
            st.subheader(f"Raw Data: {percent_chapter_or_page}")
            st.dataframe(data)
        elif percent_chapter_or_page=='Chapterwise':
            st.empty()
            data = running_books_df[['title', 'current_chapter','total_chapters']]
            st.subheader(f"Raw Data: {percent_chapter_or_page}")           
            st.dataframe(data)
        elif percent_chapter_or_page=='Pagewise':
            st.empty()
            data = running_books_df[['title','current_page','total_pages']]
            st.subheader(f"Raw Data: {percent_chapter_or_page}")
            st.dataframe(data)
    
    elif selected_option=="Show Chart":
        st.subheader("Charts")
        sns.set(rc={'axes.facecolor':'#0e1117','figure.facecolor':'#0e1117'})
        fig=plt.figure(figsize=(15,10))
        if percent_chapter_or_page=='Percentagewise':
            data = calculate_percentile(running_books_df)
            y_vals=[i for i in range(0,101,10)]
            sns.barplot(x='title', y=[100 for i in data['title']],color='#262730',edgecolor="1",data=data)
            sns.barplot(x='title', y='completed',color='#c42b2b',edgecolor="1",data=data)
            plt.ylabel('Completed(%)',color='white',size=20)
            addlabels('title','completed',data=data,format=True)
            plt.yticks(y_vals)
    
        if percent_chapter_or_page=='Chapterwise':
            st.empty()
            data=running_books_df[['title', 'current_chapter','total_chapters']]
            y_vals=[i for i in range(1,data.total_chapters.max()+1,1)]
            sns.barplot(x='title', y='total_chapters',color='#262730',edgecolor="1",data=data)
            sns.barplot(x='title', y='current_chapter',color='#c42b2b',capsize=.3,edgecolor="1",data=data)
            plt.ylabel('Chapters',color='white',size=20)
            addlabels('title','current_chapter',data=data)
            plt.yticks(y_vals)

        if percent_chapter_or_page=='Pagewise':
            st.empty()
            data=running_books_df[['title','current_page','total_pages']]
            y_vals=[i for i in range(0,data.total_pages.max()+50,50)]
            sns.barplot(x='title', y='total_pages',color='#262730',edgecolor="1", dodge=False,data=data)
            sns.barplot(x='title', y='current_page',color='#c42b2b',edgecolor="1",dodge=False, data=data)
            plt.ylabel('Pages',color='white',size=20)
            addlabels('title','current_page',data=data)
            plt.yticks(y_vals)        
            
        plt.title(f"{percent_chapter_or_page} Progress",color='white',size=30)
        plt.xlabel('Books',color='white',size=20)
        plt.xticks(rotation=45)
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
    if 'df' not in st.session_state:
            st.session_state.df = pd.read_csv('./data/books.csv')
    df = st.session_state.df
    #df=pd.read_csv('./data/books.csv')
    df = df[df['status']=='Ongoing']
    
    try:
        main(df,st.radio("Select",["Show Chart","Show Data"],horizontal=True))
    except:
        st.error('We have encountered some error!')
        
    # Include the current year in the footer
    hide_streamlit_style = f"""<div class="myFooter">© {datetime.datetime.now().year} Copyright | Made by <a href="https://ziaulkarim.netlify.app" >Md. Ziaul Karim</a></a> </div>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
