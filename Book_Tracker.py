import streamlit as st

st.set_page_config(page_icon="📑", page_title="Book Tracker - Ziaul Karim")

def check_password():
    """Returns `True` if the user had the correct password."""
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
                .css-17ziqus {background-color: brown; visibility: hidden;}
                .css-fblp2m {visibility:hidden;}
                .css-1rs6os {visibility:hidden;}
                p{text-align: center;}
                body{text-align: center;}
                .css-1kyxreq{display:block;}
                </style>
                <title> Book Tracker </title>
                </head>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.header("Login")
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.header("Login")
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.success("Logged in!!!")
    def main():
        st.title('📑My Book Tracker')
        st.image('./giphy.gif')
        st.sidebar.header('📑 My Book Tracker')
        st.markdown('I track my books here. That\'s it.')
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
                    p{text-align: center;}
                    body{text-align: center;}
                    .css-1kyxreq{display:block; display:block;}
                    .css-fblp2m {visibility:visible;}
                    .css-1rs6os {visibility:visible;}
                    </style>
                    <title> Book Tracker </title>
                    </head>
                    <div class="myFooter">© <a>2022</a> Copyright | Made by <a href="https://codingwithzk.netlify.app" >Md. Ziaul Karim</a> with <a href="https://streamlit.io/"> Streamlit </a> </div>
                    """
        return st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    if __name__=='__main__':
        main()

 
    
