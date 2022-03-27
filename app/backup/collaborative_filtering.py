import pandas as pd
import random
import sklearn
from sklearn.neighbors import NearestNeighbors
import operator


import streamlit.components.v1 as stc
import streamlit as st

def app(user,id):
    
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
    #field = ['Artificial Intelligence','Cloud Computing','Software Engineering','App Development','Physics']

    dataf = pd.read_csv("rp_final.csv")

    df=pd.read_csv('Rating.csv')

    n = len(df)
    # id  = input("Enter your user id : ")



    #old user
    number_neighbors = 4
    knn = NearestNeighbors(metric='cosine', algorithm='brute')
    knn.fit(df.values)
    distances, indices = knn.kneighbors(df.values, n_neighbors=number_neighbors)
    distances

    x = list(zip(distances[int(id)],indices[int(id)]))
    # x

    x.sort(key = lambda y: y[0])

    arr = []
    for i in range(len(x)):
        #print(str((x[i][1])))
        # t=df["user_"+str((x[i][1]))]
        t=df[user]
        #display(t)
        if len(arr)==0:
            arr.append(t.values)
        else:
            arr+=t.values
    arr = arr/len(x)
    # arr

    enumerate_object = enumerate(arr[0][:])
    sorted_pairs = sorted(enumerate_object, key=operator.itemgetter(1))

    sorted_indices = []
    for index, element in sorted_pairs:
        sorted_indices.append(index)
        sorted_indices.reverse()
    # print(sorted_indices)

    top_3 = sorted_indices[0:3] #top 3 users with which our field aligns

    recommend_paper = []
    for i in top_3:
        field_name = field_dict[i]
        st.write(field_name)
        print(field_name)

        temp = dataf[dataf['Field']==field_name].sort_values(by='Citations',ascending = False)
        for i in temp.index.values[0:2]:
            recommend_paper.append(i)

    print(recommend_paper)
    return recommend_paper
# app()




