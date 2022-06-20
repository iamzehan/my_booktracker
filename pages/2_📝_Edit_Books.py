from cgitb import html
from pyrsistent import m
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Update", page_icon="📝")
df=pd.read_csv('./data/books.csv')
df_exp=df.copy()

st.header("📝Edit and Update")
st.sidebar.header("📝 Update Books")

status=st.radio('Choose:',['Ongoing','Upcoming'],horizontal=True)

books_df=df[df['status']==status]

@st.cache
def save_data(data):
    return data.to_csv('./data/books.csv',index=False)


selected_book=st.selectbox('Which Books you want to update?',list(books_df['title']))
st.markdown(f'Edit: $\\text{ {selected_book} }$')
data=books_df.loc[books_df['title']==selected_book]
st.dataframe(data, width=40000)
idx=data.index.values[0]
max_pages=data['total_pages'][idx]
max_chapters=data['total_chapters'][idx]
filtered_data={'id':idx,'current_page':data['current_page'][idx],'current_chapter':data['current_chapter'][idx]}
edited_page=st.number_input(label="Current Page",value=filtered_data['current_page'],max_value=max_pages)
edited_chapter=st.number_input(label="Current Chapter",value=filtered_data['current_chapter'],max_value=max_chapters)

subs=[] #subset of columns to be hightlighted

# This section is the change sensitiveness of the form fields
#  
if edited_page!=filtered_data['current_page'] and edited_chapter!=filtered_data['current_chapter']: 
    filtered_data['current_page'],filtered_data['current_chapter']=edited_page,edited_chapter 
    if status=='Ongoing':
        if edited_page<data['total_pages'][idx]:
            subs.extend(["current_page","current_chapter"])
    elif status=='Upcoming':
        subs.extend(["current_page","current_chapter","status"])
elif edited_page!=filtered_data['current_page'] and edited_chapter==filtered_data['current_chapter']:
    filtered_data['current_page']=edited_page
    if edited_page<max_pages:
        subs.append("current_page")
    elif edited_page==max_pages:
        subs.extend(["current_page","status"])
elif edited_page==filtered_data['current_page'] and edited_chapter!=filtered_data['current_chapter']:
    filtered_data['current_chapter']=edited_chapter
    subs.append("current_chapter")
if len(subs)!=0:
    st.write('Changing:')
count=1
for item in subs:
    st.write(f'```{item}```')
    count+=1

# This section updates the DataFrame
update=st.button('Update') # This is the update button that regulates the data to be saved on the disk

if update: # if "Update" is pressed
    
    id=int(filtered_data["id"]) # for disambiguity of the data, we have chosen the index value from the data that is filtered into the dictionary - "filtered_data={}"
    
    if len(subs)==1: #either current_page or current_chapter edited
        df_exp.loc[[id],subs[0]]=filtered_data[subs[0]]
    
    elif len(subs)==2: # both current_page and current_chapter edited
        if subs==["current_chapter","current_page"]:
            df_exp.loc[[id],["current_chapter","current_page"]]= filtered_data["current_chapter"],filtered_data["current_page"] 
        elif subs==["current_page","status"]:
            st.write('```Finished```')
            df_exp.loc[[id],["current_chapter","current_page","status"]]=filtered_data["current_chapter"],filtered_data["current_page"],"Finished"

    elif len(subs)==3: # this only occurs when a book from the Upcoming section changes it's current_page, current_chapter and so the status gets changed as well.
        if status=="Upcoming":
            df_exp.loc[[id],["current_chapter","current_page","status"]]=filtered_data["current_chapter"],filtered_data["current_page"],"Ongoing"
    if df_exp["current_chapter"][id] != df["current_chapter"][id] or df_exp["current_page"][id] != df["current_page"][id]:
        st.subheader("Previous Data")
        prev=df.style.apply(lambda x: ['background-color:  #791400' if (i == id) else '' for i in x.index.values],subset=subs,axis=0)
        st.dataframe(prev)
        st.subheader("Updated Data")
        upd=df_exp.style.apply(lambda x: ['background-color: #445F22' if (i == id) else '' for i in x.index.values],subset=subs,axis=0)
        st.dataframe(upd)
        confirm=st.button("Confirm",on_click=save_data(df_exp))

    else:
        st.write("`No Changes Detected`")


hide_streamlit_style = """
            <head>
            <style>
            #MainMenu{visibility: hidden;}
            .css-fk4es0{display:none;}
            .css-1lsmgbg {display: none;}
            .myFooter{color:rgba(250, 250, 250, 0.6); margin-top: 150px; text-align: center;}
            .myFooter a{color: rgb(255, 75, 75); font-weight: bolder;}
            .css-10trblm{color:rgb(255, 75, 75);}
            .css-16huue1 {color:rgb(255, 75, 75); font-size:18px;}
            .css-v37k9u p{color:#edf5e1; font-size: 18px;}
            .css-1q8dd3e{color:rgb(255, 75, 75);}
            .css-1q8dd3e:hover{color:#edf5e1; border-color:rgb(255, 75, 75);}
            .css-17ziqus {background-color: brown;}
            body{text-align:center;}
            </style>
            <title> Book Tracker </title>
            </head>
            <div class="myFooter">© 2022 Copyright | Made by <a href="https://codingwithzk.netlify.app" >Md. Ziaul Karim</a> </div>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
