import copy
import pandas as pd
import numpy as np 
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
            print('--'*100)
            
        search_word = v_df[v_df.index == self.words[0]].dropna(axis= 1).values[0]
        similar_words =  [v_df[v_df.index == w].dropna(axis= 1).values[0] for w in words[1:]]

        with switch(self.metric) as s:
            if s.case('hamming', True):
                self.__apply_distance_metric(search_word, similar_words, self.words[0], self.words[1:], self.__hamming_distance)
            if s.case('manhattan', True):
                self.__apply_distance_metric(search_word, similar_words, self.words[0], self.words[1:], self.__manhattan_distance)
            if s.case('euclidean', True):
                return self.__euclidean_distance()
            if s.case('levenshtein', True):
                return self.__levenshtein_distance()
            if s.case('cosine', True):
                return self.__cosine_distance()
            if s.default():
                print('Please specify a correct distance metric')


    def __apply_distance_metric(self, search_word, similar_words,word, words, func):

        for t, tv in zip(words, similar_words):
            self.u = search_word
            self.v = tv
            print('{} distance between word: {} and {} is: {}'.format(self.metric, word, t, func()))


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
        edition = pd.Dataframe(data = edition,
                               index= list(v),
                               columns= list(u))
        
        return distance, edition


    def __cosine_distance(self):

        distance = 1.0 - (np.dot(self.u, self.v)/
                          (np.sqrt(sum(np.square(self.u))) * 
                           np.sqrt(sum(np.square(self.v))))
                          )
        return distance
    