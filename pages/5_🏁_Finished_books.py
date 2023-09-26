import streamlit as st
import pandas as pd

def main(data):
    finished_books=data['title'].to_list()
    if len(finished_books)>0:
        count=1
        for book in finished_books:
            st.write(count, book)
            count+=1
    else:
        st.image('./pages/nope.gif')
        st.write('```None```')
    # st.dataframe(data)

if __name__ == '__main__':

    st.set_page_config(page_title="Finished",page_icon="🏁")
    st.header("🏁 Books that you've Finished")
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
            .css-17ziqus {background-color: brown; visibility: visible}
            .css-1kyxreq{display:block;}
            code{color:red; font-size:20px;}
            </style>
            <title> Book Tracker </title>
            </head>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    df=pd.read_csv('./data/books.csv')
    data=df[df['status']=='Finished']
    main(data)

    hide_streamlit_style = """
                <div class="myFooter">© 2022 Copyright | Made by <a href="https://ziaulkarim.netlify.app" >Md. Ziaul Karim</a></div>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 