# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 03:21:53 2018

Building a data set for QA contextual DNN

@author: Mauricio Martinez
@author: Jonathan Perry
@author: Chris Snyder
"""
# nltk for NLP processing (using tokenize)
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
# import json to parse a json file format
import json
import random
import numpy as np


ERROR_THRESHOLD = 0.25
words = []
sections = []
documents = []
with open('java_data3.json') as json_data:
    topics = json.load(json_data)
    ignore_these = ['(', ')', '\'','.',',', ';']      
    # loop through each sentence in our intents patterns
    for topic in topics['data']:
        for question in topic['questions']:
            w = nltk.word_tokenize(question)
            words.extend(w)
            documents.append((w, topic['topic']))
            if topic['topic'] not in sections:
                sections.append(topic['topic'])
    words = [stemmer.stem(w.lower()) for w in words if w not in ignore_these]
    words = sorted(list(set(words)))
    sections = sorted(list(set(sections)))
       
    print (len(documents), "documents")
    print (len(sections), "sections", sections)
    print (len(words), "unique words", words)



def set_training_data():
    # create our training data
    training = []
    output = []
    # create an empty array for our output
    output_empty = [0] * len(sections)
    
    # training set, bag of words for each sentence
    for doc in documents:
        # initialize our bag of words
        bag = []
        # list of tokenized words for the pattern
        pattern_words = doc[0]
        # stem each word
        pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
        # create our bag of words array
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)
    
        # output is a '0' for each tag and '1' for current tag
        output_row = list(output_empty)
        output_row[sections.index(doc[1])] = 1
    
        training.append([bag, output_row])
    
    # shuffle our features and turn into np.array
    random.shuffle(training)
    training = np.array(training)
    return list(training[:,0]), list(training[:,1])

def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

def classify(sentence, model):
    # generate probabilities from the model
    results = model.predict([bow(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((sections[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list


def response(sentence, model, userID='123', show_details=False):
    results = classify(sentence, model)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in topics['data']:
                # find a tag matching the first result
                if i['topic'] == results[0][0]:
                    # a random response from the intent
                    return print(results)
