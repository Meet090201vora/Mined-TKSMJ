from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
from num2words import num2words


import nltk
import os
import string
import numpy as np
import copy
import pandas as pd
import pickle
import re
import math
nltk.download('stopwords')
nltk.download('punkt')


# data prepocessinf funcitons

def convert_lower_case(data):
    return np.char.lower(data)

def remove_stop_words(data):
    stop_words = stopwords.words('english')
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text

def remove_punctuation(data):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
        data = np.char.replace(data, "  ", " ")
    data = np.char.replace(data, ',', '')
    return data

def remove_apostrophe(data):
    return np.char.replace(data, "'", "")

def stemming(data):
    stemmer= PorterStemmer()
    
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return new_text


def convert_numbers(data):
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        try:
            w = num2words(int(w))
        except:
            a = 0
        new_text = new_text + " " + w
    new_text = np.char.replace(new_text, "-", " ")
    return new_text

def preprocess(data):
    data = convert_lower_case(data)
    data = remove_punctuation(data) #remove comma seperately
    data = remove_apostrophe(data)
    data = remove_stop_words(data)
    data = convert_numbers(data)
    data = stemming(data)
    data = remove_punctuation(data)
    data = convert_numbers(data)
    data = stemming(data) #needed again as we need to stem the words
    data = remove_punctuation(data) #needed again as num2word is giving few hypens and commas fourty-one
    data = remove_stop_words(data) #needed again as num2word is giving stop words 101 - one hundred and one
    return data

def import_data():
    global text,processed_title,processed_text,data
    data = pd.read_csv("rp.csv")
    titles=data.Title.values
    text=data.Abstract.values


    processed_title = []
    processed_text = []

    for i in range(len(text)):
        processed_text.append(word_tokenize(str(preprocess(text[i]))))
        processed_title.append(word_tokenize(str(preprocess(titles[i]))))

    DF = {}

    for i in range(len(processed_title)):
        tokens = processed_text[i]
        for w in tokens:
            try:
                DF[w].add(i)
            except:
                DF[w] = {i}

        tokens = processed_title[i]
        for w in tokens:
            try:
                DF[w].add(i)
            except:
                DF[w] = {i}
    for i in DF:
        DF[i] = len(DF[i])
    
    total_vocab_size = len(DF)
    total_vocab = [x for x in DF]


def doc_freq(word):
    c = 0
    try:
        c = DF[word]
    except:
        pass
    return c


def similarity():
    global tf_idf,tf_idf_title, text,processed_title,processed_text 
    
    N = len(text)
    doc = 0

    tf_idf = {}

    for i in range(N):
        
        tokens = processed_text[i]
        
        counter = Counter(tokens + processed_title[i])
        words_count = len(tokens + processed_title[i])
        
        for token in np.unique(tokens):
            
            tf = counter[token]/words_count
            df = doc_freq(token)
            idf = np.log((N+1)/(df+1))
            
            tf_idf[doc, token] = tf*idf

        doc += 1
        doc = 0

    tf_idf_title = {}

    for i in range(N):
        
        tokens = processed_title[i]
        counter = Counter(tokens + processed_text[i])
        words_count = len(tokens + processed_text[i])

        for token in np.unique(tokens):
            
            tf = counter[token]/words_count
            df = doc_freq(token)
            idf = np.log((N+1)/(df+1)) #numerator is added 1 to avoid negative values
            
            tf_idf_title[doc, token] = tf*idf

        doc += 1


    for i in tf_idf:
        tf_idf[i] *= 0.3

    for i in tf_idf_title:
        tf_idf[i] = tf_idf_title[i]



def matching_score(k, query):
    global tf_idf,tf_idf_title
    preprocessed_query = preprocess(query)
    tokens = word_tokenize(str(preprocessed_query))

    print("Matching Score")
    print("\nQuery:", query)
    print("")
    print(tokens)
    
    query_weights = {}

    for key in tf_idf:
        
        if key[1] in tokens:
            try:
                query_weights[key[0]] += tf_idf[key]
            except:
                query_weights[key[0]] = tf_idf[key]
    
    query_weights = sorted(query_weights.items(), key=lambda x: x[1], reverse=True)

    print("")
    
    l = []
    
    for i in query_weights[:5]:
        l.append(i[0])
    
    print(l)
    return l
    

# l = matching_score(3, "Supervised learning is modern era, autonoums")