import copy
import pandas as pd
import numpy as np
from scipy.stats import itemfreq
import switch

class DistanceMetric:

    def __init__(self, metric, words, norm = False, show = False):
        self.metric = metric.lower()
        self.words = words
        self.norm = norm
        self.show = show
        self.u = None
        self.v = None
    
    def apply(self):

        vectors = self.__vectorize()
        v_df = pd.DataFrame(vectors, index= self.words)            

        if self.show:
            print("Vectors")
            print(v_df)
            print('--'*45)
                        
        if self.metric == 'cosine':
            colums, bag_vectors = self.__bag_characters_vectorize()
            bag_df = pd.DataFrame(bag_vectors, index = self.words, columns = colums )
            search_word = bag_df[v_df.index == self.words[0]].values[0]
            similar_words =  [bag_df[v_df.index == w].values[0] for w in self.words[1:]]        
        else:
            search_word = v_df[v_df.index == self.words[0]].dropna(axis= 1).values[0]
            similar_words =  [v_df[v_df.index == w].dropna(axis= 1).values[0] for w in self.words[1:]]

        with switch(self.metric) as s:
            if s.case('hamming', True):
                self.__apply_distance_metric(search_word, similar_words, self.words[0], self.words[1:], self.__hamming_distance)
            if s.case('manhattan', True):
                self.__apply_distance_metric(search_word, similar_words, self.words[0], self.words[1:], self.__manhattan_distance)
            if s.case('euclidean', True):
                self.__apply_distance_metric(search_word, similar_words, self.words[0], self.words[1:], self.__euclidean_distance)        
            if s.case('levenshtein', True):
                self.__apply_distance_metric_2(search_word, similar_words, self.words[0], self.words[1:], self.__levenshtein_distance)
            if s.case('cosine', True):
                self.__apply_distance_metric_3(search_word, similar_words, self.words[0], self.words[1:], self.__cosine_distance_similarity)        
            if s.default():
                print('Please specify a correct distance metric')


    def __apply_distance_metric(self, search_word, similar_words,word, words, func):

        for t, tv in zip(words, similar_words):
            self.u = search_word
            self.v = tv
            print('{} distance between word: {} and {} is: {}'.format(self.metric, word, t, func()))


    def __apply_distance_metric_2(self, search_word, similar_words,word, words, func):
        
        for w in words:
            self.v = w
            self.u = word
            d , e = func()
            print('{} distance between word: {} and {} is: {}'.format(self.metric, word, w, d))
            print(e)
            print('-'*45)

    
    def __apply_distance_metric_3(self, search_word, similar_words,word, words, func):
        
        for t, tv in zip(words, similar_words):
            self.u = search_word
            self.v = tv            
            d = round(func(), 2)
            s = round(1 - d, 2)
            print('{} distance between word: {} and {} is: {}'.format(self.metric, word, t, d))
            print('{} similarity between word: {} and {} is: {}'.format(self.metric, word, t, s))
            print('-'*45)
                                  

            

    def __bag_characters_vectorize(self):

        wl = [w.lower() for w in self.words]
        u = np.unique(np.hstack([list(w) for w in wl ]))
        w_c = [{ c1: c2 for c1, c2 in np.stack(np.unique(list(w), return_counts = True), axis= 1)}
               for w in wl]
        bag = [np.array([int(wt.get(char, 0)) for char in u]) for wt in w_c]

        return list(u), bag


    def __vectorize(self):

        vectors = [w.lower() for w in self.words]
        vectors = [np.array(list(w)) for w in self.words]
        vectors = [np.array([ord(c) for c in w]) for w in self.words]
        return vectors

    def __hamming_distance(self):

        if self.u.shape != self.v.shape:
            return 'Incorrect lengths'
        elif self.norm:
            return (self.u!=self.v).mean()            
        else:
            return (self.u!=self.v).sum()
            
   
    def __manhattan_distance(self):

        if self.u.shape != self.v.shape:
            return 'Incorrect lengths'
        elif self.norm:
            return abs(self.u - self.v).mean()            
        else:
            return abs(self.u - self.v).sum()


    def __euclidean_distance(self):

        if self.u.shape != self.v.shape:
            return 'Incorrect lengths'
        return np.sqrt(np.sum(np.square(self.u - self.v)))
        

    def __levenshtein_distance(self):

        u = self.u.lower()
        v = self.v.lower()

        if u == v: return 0
        elif len(u) == 0: return len(v)
        elif len(v) == 0: return len(u)

        edition = []

        d_u = [0] * (len(v) + 1)
        d_v = [0] * (len(v) + 1)

        for i in range(len(d_u)):
            d_u[i] = i
        
        for i in range(len(u)):
            d_v[0] = i + 1
            for j in range(len(v)):
                cost = 0 if u[i] == v[j] else 1
                d_v[j + 1] =  min(d_v[j] + 1, d_u[j + 1] + 1, d_u[j] + cost)
            for j in range(len(d_u)):
                d_u[j] == d_v[j]
            edition.append(copy.copy(d_v))
        distance = d_v[len(v)]
        edition = np.array(edition)
        edition = edition.T
        edition = edition[1:,]
        edition = pd.DataFrame(data = edition,
                               index= list(v),
                               columns= list(u))
        
        return distance, edition


    def __cosine_distance_similarity(self):

        distance = 1.0 - (np.dot(self.u, self.v)/
                          (np.sqrt(sum(np.square(self.u))) * 
                           np.sqrt(sum(np.square(self.v))))
                          )
        return distance
    
    