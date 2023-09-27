import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main(df,selected_option):
    running_books_df=df[df['status']=='Ongoing']
    percent_chapter_or_page= st.selectbox('How Do you want to track your progress?',["Percentagewise",'Chapterwise','Pagewise'])
    
    if selected_option == "Show Data":
        if percent_chapter_or_page=='Percentagewise':
            st.subheader(f"Raw Data: {percent_chapter_or_page}")
            st.dataframe(calculate_percentile(running_books_df)[['title','format_completed']])
        elif percent_chapter_or_page=='Chapterwise':
            st.empty()
            st.subheader(f"Raw Data: {percent_chapter_or_page}")           
            st.dataframe(running_books_df[['title', 'current_chapter','total_chapters']])
        elif percent_chapter_or_page=='Pagewise':
            st.empty()
            st.subheader(f"Raw Data: {percent_chapter_or_page}")
            st.dataframe(running_books_df[['title','current_page','total_pages']])
    
    elif selected_option=="Show Chart":
        st.subheader("Charts")
        sns.set(rc={'axes.facecolor':'#0e1117','figure.facecolor':'#0e1117'})
        fig=plt.figure(figsize=(15,10))
        if percent_chapter_or_page=='Percentagewise':
            percentage=calculate_percentile(running_books_df)
            y_vals=[i for i in range(0,101,10)]
            sns.barplot(x='title', y='total',color='#262730',edgecolor="1",data=percentage)
            sns.barplot(x='title', y='completed',color='#c42b2b',edgecolor="1",data=percentage)
            plt.ylabel('Pages',color='white',size=20)
            addlabels('title','completed',data=percentage)
            plt.yticks(y_vals)
    
        if percent_chapter_or_page=='Chapterwise':
            st.empty()
            chapterwise=running_books_df[['title', 'current_chapter','total_chapters']]
            y_vals=[i for i in range(1,chapterwise.total_chapters.max()+1,1)]
            sns.barplot(x='title', y='total_chapters',color='#262730',edgecolor="1",data=chapterwise)
            sns.barplot(x='title', y='current_chapter',color='#c42b2b',capsize=.3,edgecolor="1",data=chapterwise)
            plt.ylabel('Chapters',color='white',size=20)
            addlabels('title','current_chapter',data=chapterwise)
            plt.yticks(y_vals)

        if percent_chapter_or_page=='Pagewise':
            st.empty()
            pagewise=running_books_df[['title','current_page','total_pages']]
            y_vals=[i for i in range(0,pagewise.total_pages.max()+50,50)]
            sns.barplot(x='title', y='total_pages',color='#262730',edgecolor="1", dodge=False,data=pagewise)
            sns.barplot(x='title', y='current_page',color='#c42b2b',edgecolor="1",dodge=False, data=pagewise)
            plt.ylabel('Pages',color='white',size=20)
            addlabels('title','current_page',data=pagewise)
            plt.yticks(y_vals)        
            
        plt.title(f"{percent_chapter_or_page} Progress",color='white',size=30)
        plt.xlabel('Books',color='white',size=20)
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
            'format_completed': df['completed'].astype(int).astype(str) + '%',
            'total': 100
        })
        return percentile_df
        
    def addlabels(x,y,data):
        x,y = list(data[x]),list(data[y])
        for i in range(len(x)):
            plt.text(i, y[i]//2, y[i], ha = 'center',fontsize='medium', color='white')
        
    df=pd.read_csv('./data/books.csv')
    selected_option=st.radio("Select",["Show Chart","Show Data"],horizontal=True)
    
    main(df,selected_option)

    import datetime
    # Get the current year
    current_year = datetime.datetime.now().year

    # Include the current year in the footer
    footer = f'© {current_year} Copyright | Made by <a href="https://ziaulkarim.netlify.app" >Md. Ziaul Karim</a>'
    hide_streamlit_style = f"""<div class="myFooter">{footer}</a> </div>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
