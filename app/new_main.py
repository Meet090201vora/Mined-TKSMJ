import numpy as np
import copy
import pandas as pd
import streamlit.components.v1 as stc
import streamlit as st
import search_general
import paper_based
import content_based
import backup_main
import collabrative_based

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



st.title("Netflix for Researcher")
#  content collabrative
option=["Query Based","Trending Fields","Trending Papers"]
c=st.sidebar.selectbox('select',option)
 


if c==option[0]:
    content_based.app()
  
elif c==option[1]:
    collabrative_based.app()
    # pass

elif c==option[2]:
    paper_based.app()