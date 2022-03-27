
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import seaborn as sns
import operator
import streamlit.components.v1 as stc
import streamlit as st
"""new user => generate id (append user table)  -->
user_last_used_id+1

=> trending (popularity based)

  => rating table => avg rating => sort 
  
  => top 5 paper of each field
"""


def app():
    df=pd.read_csv("Rating.csv",index_col=0)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    # st.write(df)
    with st.form(key='userForm'):
    
        if st.form_submit_button(label='Create User'):
            id=df.shape[1]
            user='user_'+str(id)
            
            st.error('Your UserId is '+user)
           


    field_dict = {0:'Artificial Intelligence',
              1:'Machine Learning', 
              2:'Software Engineering',
              3:'Math',
              4:'Social and Information Networks',
              5:'Information Theory',
              6:'Data Structures',
              7:'Cryptography and Security',
              8:'Computer Vision',
              9:'Information Retrieval System'}
    # see later- 0- not read

    arr=df.sum(axis=1)
    arr=arr/df.shape[1]

    enumerate_object = enumerate(arr)
    sorted_pairs = sorted(enumerate_object, key=operator.itemgetter(1))

    sorted_indices = []
    for index, element in sorted_pairs:
        sorted_indices.append(index)
    sorted_indices.reverse()
    print(sorted_indices)

    dataf = pd.read_csv("rp_final.csv")

    # top 5 papers in  each field
    top_5=[]
    for i in sorted_indices:
        field_name = field_dict[i]
        temp = dataf[dataf['Field']==field_name].sort_values(by='Citations',ascending = False)
        l=temp.index.values
        # print(temp)
        print(l)
        for j in l[0:min(1,len(l))]:
            top_5.append(j)
    print(top_5)

    df['user_'+str(df.shape[1])] = [0 for i in range((df.shape[0]))]
    # df.to_csv('Rating.csv')
    st.write(df)
    return  top_5

# app()
