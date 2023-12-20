import streamlit as st
import pandas as pd
st.set_page_config(page_icon="📑", page_title="Book Tracker - Ziaul Karim")

def check_password():
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"] # if username is included in secrets file
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]] # if password under the username is matching the one given
        ):
            st.session_state["password_correct"] = True # if those conditions are met then our password is correct
            del st.session_state["password"]  # delete the password from session state
            del st.session_state["username"]  # delete the username from session state
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.title("Book Tracker 📔")
        st.header("Login 👤")
        st.text_input("Username 👤", on_change=password_entered, key="username")
        st.text_input(
            "Password 🔑", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.header("Login")
        st.text_input("Username 👤", on_change=password_entered, key="username")
        st.text_input(
            "Password 🔑", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True
    
def main():
    st.title('📑My Book Tracker')
    st.image('./giphy.gif')
    st.sidebar.header('📑 My Book Tracker')
    st.markdown('I track my books here. That\'s it.')
    import datetime
    # Get the current year
    current_year = datetime.datetime.now().year

    # Include the current year in the footer
    footer = f'© {current_year} Copyright | Made by <a href="https://ziaulkarim.netlify.app" >Md. Ziaul Karim</a>'
    hide_streamlit_style = f"""<div class="myFooter">{footer}</a> </div>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
 
if __name__=='__main__':
    if check_password():
        st.success("Logged in!!!")
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
            .css-17ziqus {background-color: brown; display:block}
            p{text-align: center;}
            body{text-align: center;}
            .css-1kyxreq{display:block; display:block;}
            .css-fblp2m {display:block;}
            .css-1rs6os {display:block;}
            </style>
            <title> Book Tracker </title>
            </head>
            """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        if 'df' not in st.session_state:
            st.session_state.df = pd.read_csv('./data/data.csv')
        df = st.session_state.df
        main()
    else:
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
                .css-17ziqus {background-color: brown; display: none!important;}
                .css-fblp2m {display:none;}
                .css-1rs6os {display:none}
                p{text-align: center;}
                body{text-align: center;}
                .css-1kyxreq{display:block;}
                </style>
                <title> Book Tracker </title>
                </head>
                """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    

 
    
