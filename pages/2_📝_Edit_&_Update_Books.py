import datetime
import pandas as pd
import streamlit as st
from Ongoing_Books import df

def save_data(data):
    return data.to_csv('./data/books.csv',index=False)
    
def main(df,df_exp,books_df):
    selected_book=st.selectbox('Which Books you want to update?',list(books_df['title']))
    st.markdown(f'`Edit:` $\\text{ {selected_book} }$')
    data=books_df.loc[books_df['title']==selected_book]
    st.dataframe(data)
    idx=data.index.values[0]
    max_pages=data['total_pages'][idx]
    max_chapters=data['total_chapters'][idx]
    filtered_data={'id':idx,'current_page':data['current_page'][idx],'current_chapter':data['current_chapter'][idx]}
    col1, col2=st.columns(2)
    with col1:
        edited_page=st.number_input(label="Current Page",value=filtered_data['current_page'],max_value=max_pages)
    with col2:
        edited_chapter=st.number_input(label="Current Chapter",value=filtered_data['current_chapter'],max_value=max_chapters)

    subs=[] #subset of columns to be changed and to be hightlighted
    
    # This section is the change sensitiveness of the form fields
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
        elif edited_page>=max_pages:
            subs.extend(["current_page","status"])
            
    elif edited_page==filtered_data['current_page'] and edited_chapter!=filtered_data['current_chapter']:
        filtered_data['current_chapter']=edited_chapter
        subs.append("current_chapter")
        
    # This section updates the DataFrame
    # update=st.button('Check Changes') # This is the update button that regulates the data to be saved on the disk
    exp = st.empty()
    with exp.expander(f'{"Changing: ```"+(", ").join([item for item in subs])+"```" if subs!=[] else "```No Changes yet```"}',expanded=(subs != [])): # if "Update" is pressed
        id=int(filtered_data["id"]) # for disambiguity of the data, we have chosen the index value from the data that is filtered into the dictionary - "filtered_data={}"
        if len(subs)==1: #either current_page or current_chapter edited
            df_exp.loc[[id],subs[0]]=filtered_data[subs[0]]
        elif len(subs)==2: # both current_page and current_chapter edited
            if set(subs) == {"current_chapter", "current_page"}:
                df_exp.loc[[id],["current_chapter","current_page"]]= filtered_data["current_chapter"],filtered_data["current_page"] 
            elif set(subs)=={"current_page","status"}:
                st.write('```Finished```')
                df_exp.loc[[id],["current_chapter","current_page","status"]]=filtered_data["current_chapter"],filtered_data["current_page"],"Finished"
        elif len(subs)==3: # this only occurs when a book from the Upcoming section changes it's current_page, current_chapter and so the status gets changed as well.
            if status=="Upcoming":
                df_exp.loc[[id],["current_chapter","current_page","status"]]=filtered_data["current_chapter"],filtered_data["current_page"],"Ongoing"
        
        if df_exp["current_chapter"][id] != df["current_chapter"][id] or df_exp["current_page"][id] != df["current_page"][id]:
            st.subheader("Previous Data")
            st.dataframe(df.style.apply(lambda x: ['background-color:  #791400' if (i == id) else '' for i in x.index.values],subset=subs,axis=0))
            st.subheader("Updated Data")
            st.dataframe(df_exp.style.apply(lambda x: ['background-color: #445F22' if (i == id) else '' for i in x.index.values],subset=subs,axis=0))
        else:
            st.write("`No Changes Detected`")
    col1,col2= st.columns([0.5,0.5])
    with col1:        
        if st.button("Confirm"):
            save_data(df_exp)
    with col2:
        if st.button("Cancel"):
            save_data(df)

if __name__ == '__main__':

    #config
    st.set_page_config(page_title="Update", page_icon="📝")

    #css styles
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
            .css-17ziqus {background-color: brown; visibility: visible}
            body{text-align:center;}
            </style>
            <title> Book Tracker </title>
            </head>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    st.header("📝Edit and Update")
    st.sidebar.header("📝 Update Books")

    #variables and functions
    # df=pd.read_csv('./data/books.csv')
    df = df
    df_exp=df.copy()
    status=st.radio('Choose:',['Ongoing','Upcoming'],horizontal=True)
    books_df=df[df['status']==status]
    
    main(df,df_exp,books_df)
    hide_streamlit_style = f"""<div class="myFooter">© { datetime.datetime.now().year} Copyright | Made by <a href="https://ziaulkarim.netlify.app" >Md. Ziaul Karim</a></a> </div>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
