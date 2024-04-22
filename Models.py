import numpy as np
import pandas as pd
import os
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random
import nltk
from Story_dataset import *

class Markov():
    def __init__(self,markov_model=dict()):
        self.markov_model = markov_model

    def processText(path = 'internet_archive_scifi_v3.txt'): 
        txt = []
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line!='':
                    txt.append(line)


        nltk.download('punkt')

        bag_of_words = []
        for line in txt:
            line = line.lower()
            line = re.sub(r"[,.\"\'!@#$%^&*(){}?/;`~:<>+=-\\]", "", line)
            tokens = word_tokenize(line)
            words = [word for word in tokens if word.isalpha()]
            bag_of_words+=words
        
        return bag_of_words

    def train(bag_of_words, n_gram=2):
        markov_model = {}
        for i in range(len(bag_of_words)-n_gram-1):
            curr_state, next_state = "", ""
            for j in range(n_gram):
                curr_state += bag_of_words[i+j] + " "
                next_state += bag_of_words[i+j+n_gram] + " "
            curr_state = curr_state[:-1]
            next_state = next_state[:-1]
            if curr_state not in markov_model:
                markov_model[curr_state] = {}
                markov_model[curr_state][next_state] = 1
            else:
                if next_state in markov_model[curr_state]:
                    markov_model[curr_state][next_state] += 1
                else:
                    markov_model[curr_state][next_state] = 1

        # calculating transition probabilities
        for curr_state, transition in markov_model.items():
            total = sum(transition.values())
            for state, count in transition.items():
                markov_model[curr_state][state] = count/total
        
        markov_model = Markov(markov_model)
        return markov_model


    def generate_story(self, limit=100, start="starship"):
        possibles = []
        markov_model = dict(self.markov_model)
        keys = list(markov_model.keys())
        for i in keys:
            if start in i:
                possibles.append(i)

        start = random.sample(possibles,1)[0]

        n = 0
        curr_state = start
        next_state = None
        story = ""
        story+=curr_state+" "
        while n<limit:
            next_state = random.choices(list(markov_model[curr_state].keys()),
                                        list(markov_model[curr_state].values()))

            curr_state = next_state[0]
            story+=curr_state+" "
            n+=1
        return story
    
    def save(self):
        import pickle
        markov_model = self.markov_model
        keys = []
        values = []

        for i in list(markov_model.keys()):
            keys.append(i)
        
        for i in list(markov_model.values()):
            values.append(i)


        with open("markovModel_scifi.pkl", "wb") as file:
            pickle.dump((keys,values), file)
    
    def load_model(self,path='markovModel_scifi.pkl'):
        import pickle
        with open(path,'rb') as f:
            data = pickle.load(f)
        markov_model = dict()
        keys,values = data
        for i in range(len(keys)):
            markov_model[keys[i]] = values[i]
        return Markov(markov_model)
    



