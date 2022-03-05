
import pandas as pd
import random
import sklearn
from sklearn.neighbors import NearestNeighbors
import operator


import streamlit.components.v1 as stc
import streamlit as st
def app(user,id):
    dataf = pd.read_csv("rp_final.csv")
    df= pd.read_csv('Paper_Rating.csv',index_col=0)
    
    # print(df)
    n = len(df)
    # id  = input("Enter yo id : ")
    # st.write('started to fit')
    number_neighbors = 4
    knn = NearestNeighbors(metric='cosine', algorithm='brute')
    knn.fit(df.values)
    distances, indices = knn.kneighbors(df.values, n_neighbors=number_neighbors)

    # st.write('done fitting')

    x = list(zip(distances[int(id)],indices[int(id)]))


    x.sort(key = lambda y: y[0])

    arr = []
    for i in range(len(x)):
        #print(str((x[i][1])))
        t=df.loc["user_"+str((x[i][1]))]
        #display(t)
        if len(arr)==0:
            arr.append(t.values)
        else:
            arr+=t.values
    arr = arr/len(x)
    # arr
    # st.write('found average')

    enumerate_object = enumerate(arr[0][:])
    sorted_pairs = sorted(enumerate_object, key=operator.itemgetter(1))

    sorted_indices = []
    for index, element in sorted_pairs:
        sorted_indices.append(index)
        sorted_indices.reverse()
    # st.write(sorted_indices)

    top_5 = sorted_indices[0:5] #top 5 users with which our field aligns
    print(top_5)


    return top_5
