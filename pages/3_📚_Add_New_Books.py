import datetime
import pandas as pd
import streamlit as st

def save_data(data):
    return data.to_csv('./data/books.csv',index=False)
    
def cancel_data(data,id):
    data=data.drop(axis=0,index=id)
    
def main(df,df_exp): 
    id=len(df_exp)
    add_current_page=0
    add_current_chapter=0
    add_status='Upcoming'

    form=st.form("Add_Book",clear_on_submit=True)
    with form:
        add_title=st.text_input(label='Book Title',value="")
        add_total_pages=st.number_input(label='Total Pages',value=0)
        add_total_chapters=st.number_input(label='Total Chapters',value=0)
        submitted=st.form_submit_button("Submit")
        cancelled=st.form_submit_button("Cancel")
        if submitted:
            if add_title in list(df.title):
                st.write('```Book Already exists```')
            elif add_title!=None and add_total_pages!=0 and add_total_chapters!=0:
                df_exp.loc[id]=[add_title,add_current_page,add_total_pages,add_current_chapter,add_total_chapters,add_status]
                st.subheader("Data Added!")
                st.write('Added to row:', id)
                preview=df_exp.style.apply(lambda x: ['background-color: green' if (i == id) else '' for i in x.index.values], axis=0)
                st.dataframe(preview,width=4000)
                st.write("```Saved```")
                save_data(df_exp)
            else:
                st.write("```Input Boxes are empty...```")
        elif cancelled:
            st.write("```Cancelled```")
            ### If after submission you want to reset, go to the len(df) and delete that row###

if __name__ == "__main__":
    
    #config
    st.set_page_config(page_title="Add Book", page_icon="📚")

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
            .css-ffhzg2 {text-align: center;}
            </style>
            <title> Book Tracker </title>
            </head>
            <script>document.getElementById("demo").innerHTML = new Date().getFullYear();</script>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.header("📚 Add a new Book")
    st.sidebar.header("📚 Add a new Book")
    st.markdown("Add a new book that you are planning to read")

    if 'df' not in st.session_state:
            st.session_state.df = pd.read_csv('./data/books.csv')
    df = st.session_state.df
    
    #df=pd.read_csv('./data/books.csv')
    df_exp=df.copy()

    main(df,df_exp)

    current_year = datetime.datetime.now().year
    footer = f'© {current_year} Copyright | Made by <a href="https://ziaulkarim.netlify.app" >Md. Ziaul Karim</a>'
    hide_streamlit_style = f"""<div class="myFooter">{footer}</a> </div>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
