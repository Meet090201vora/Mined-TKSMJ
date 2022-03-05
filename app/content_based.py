import streamlit as st
import search_general
import streamlit.components.v1 as stc

import re
import math
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

    data=search_general.data
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

    # st.write('in cont based')
    with st.form(key='searchform2'):
    # option=["Select one","Artificial Intelligence","Big Data","Computer Vision","Neural Networks"]
    # search_field = st.selectbox("Select one",option)

        search_input = st.text_input("Search")
        date = st.date_input("Published After")#,datetime.date(2019, 7, 6))

        search_abstract = st.form_submit_button(label='Search in Abstract')    
        search_title = st.form_submit_button(label='Search by Title')
        search_author = st.form_submit_button(label='Search by Author')
        search_date = st.form_submit_button(label='Search by Date')


    search_general.import_data()
    search_general.similarity()  
    # st.write("Content based filtering done....")

    if search_abstract:
        # st.write('hello')
        st.success("You searched for {} in Abstract".format(search_input))

        recommended_papers = search_general.matching_score(3, search_input)
        
        if len(recommended_papers)==0:
            st.write("Oops!! No match found ....") # pop up
        else:
            output(recommended_papers)

        
    elif search_author:
        st.success("You searched for Author: {} ".format(search_input))

        l=search_general.data[search_general.data["Authors"].str.contains(search_input.strip(),flags=re.IGNORECASE)==True].index.values

        if len(l)==0:
            st.write("Oops!! No match found ....") # pop up
        else:
            output(l)
            # st.write(search_general.data.iloc[l])

    elif search_title:
        st.success("You searched for {} in Title ".format(search_input))

        l=search_general.data[search_general.data["Title"].str.contains(search_input.strip(),flags=re.IGNORECASE)==True].index.values
        if len(l)==0:
            st.write("Oops!! No match found ....") # pop up
        else:
            output(l)
    elif search_date:
        pass
