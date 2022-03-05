import streamlit as st
import search_general
import streamlit.components.v1 as stc

import new_user
import pandas as pd
import collaborative_filtering
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #053258;
    # color:#ffffff;
    width:60%;
    padding: 5%;
    margin-left:20%;
    font-size:25px;
}
div.stButton > button:hover {
    background-color: #ff0000;
    color:#000000;
}
#the-title {
text-align: center;
}
# div.stTitle > title:first-child{
#     # font-size:10cm
#     text-align: centre;
# }
# div.stTextInput>div>div>input {
#     baackground-color: #000000;
# }
</style>""", unsafe_allow_html=True)


JOB_HTML_TEMPLATE = """
<div style="width:100%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 10px;
box-shadow:0 0 1px 1px #eee; background-color: #31333F;
border-left: 5px solid #6c6c6c;color:white;">
<h4>{}</h4>
<h5>{}</h5>
<h6>{}</h6>
</div>
"""

JOB_DES_HTML_TEMPLATE = """
<div style='color:#ffffff'>
{}
</div>
"""

def output(l):
    # global l
    # st.write("in output...")
    # st.write(l)

    data=pd.read_csv('rp_final.csv')
    # Number of Results
    num_of_results = len(l)
    st.subheader("Showing {} Research Paper".format(num_of_results))
    # st.write(data)
        

# Unnamed: 0
# Title
# Authors
# Keyword
# Abstract

    for i in l:
        title = data.iloc[i]['Title']
        authors = data.iloc[i]['Authors']
        keyword = data.iloc[i]['Keyword']
        date = data.iloc[i]['Date'] #when date
        abstract = data.iloc[i]['Abstract']
        st.markdown(JOB_HTML_TEMPLATE.format(title,authors,date),
            unsafe_allow_html=True)

        # Description
        with st.expander("Abstract"):
            stc.html(JOB_DES_HTML_TEMPLATE.format(abstract),scrolling=True)





def app():
    
    temp=pd.read_csv('Rating.csv')
    opt=[]

    for i in range(temp.shape[1]):
        opt.append('user_'+str(i))

    choice=['New User','Existing User']
    type_of_user=st.selectbox('Type of User',choice)
    if type_of_user==choice[1]:
        # print(opt)
        with st.form(key='searchform'):

            user=st.selectbox('Enter User Id',opt)
            search = st.form_submit_button(label='Search')    

            id=int(user[5:])
            # st.write(id)
            if search:
                output(collaborative_filtering.app(user,id))



        #  NEw  USER      
    elif type_of_user==choice[0]:
        recommend_paper=new_user.app()
        search = st.button(label='Search')    

        # id=int(user[5:])
        # st.write(id)
        if search:
                output(recommend_paper)
    else:
        st.write('Invalid Input')