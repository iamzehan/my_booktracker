import datetime
import pandas as pd
import streamlit as st

def main(data):
    st.header("Books that you plan to read")
    st.dataframe(data)

if __name__ == '__main__':
                                                    #config
    st.set_page_config(page_title="Upcoming",page_icon="🆕")
    st.sidebar.header("🆕 Upcoming books")

                                                    #styles
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
            </style>
            <title> Book Tracker </title>
            </head>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

                                                    #main
    if 'df' not in st.session_state:
            st.session_state.df = pd.read_csv('./data/books.csv')
    df = st.session_state.df
    #df=pd.read_csv('./data/books.csv')
    data=df[df['status']=='Upcoming']
    data = pd.DataFrame({'Name':data['title'], 'Chapters':data['total_chapters'],'Pages':data['total_pages']})
    data=data.sort_values(by=['Pages'],ascending=True)

    main(data)
                                                    #footer
    current_year = datetime.datetime.now().year
    footer = f'© {current_year} Copyright | Made by <a href="https://ziaulkarim.netlify.app" >Md. Ziaul Karim</a>'
    hide_streamlit_style = f"""<div class="myFooter">{footer}</a> </div>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
