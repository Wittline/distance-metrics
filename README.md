# Understanding Similarity Measures for Text Analysis
The aim of this repository  is analyze how similar two words or terms are to each other, Distance metrics are the most common techniques to use for mesure similarities between words, there is an area called Document similarity that is responsible for searching similarities between sentences or paragraphs of text, this document only focuses on individual words or terms. It is worth mentioning that these techniques could be used for spell-checking, autocomplete sentences or correct words or senteces.

![image](https://user-images.githubusercontent.com/8701464/128754115-e16da511-f567-4fbf-8e9a-076bd852f2bc.png)


# Distance Metric of similarity
There are a lot of Distance metrics that you can use to compute and mesure similarities between entities of text. The measure d is called distance metric of similarity if and only if satisfies the next coditions:

- The distance between any two words say X and Y, must be always non-negative
- The distance between two words should always be zero if and only if they are identical
- The distance measure should always be symmetric, the distance between X and Y muts be equals to the distance between Y and X
- The distance measure should satisfy the triangle inequality property
- Due to the conditions mentioned above, the Kullback-leibler is a distance measure which violates the third condition and it can not be used for measure similarity between words.

> all similarity distance measures of similarity are not distance metrics of similarity.

# Feature engineering
Before start the computation of the distance metrics to check how close two words are, we need to convert the text to numeric values by mapping each letter to a unique numeric value.

Let’s imagine the following group of words:

```python
words = ['Similar', 'similares', 'iguales', 'parecidas', 'similaridad', 'isimral', 'similat', 'somiral']
 ```
> Converting to a vector of numerical values using Character vectorization

```python
    def __vectorize(self):

        vectors = [np.array(list(w.lower())) for w in self.words]
        vectors = [np.array([ord(c) for c in w]) for w in vectors]
        return vectors
```

![image](https://user-images.githubusercontent.com/8701464/128754146-bf65b87f-d61d-4137-b35c-df3acaecd272.png)


> Converting to a vector of numerical values using Bag of character vectorization:


```python
    def __bag_characters_vectorize(self):

        u = np.unique(np.hstack([list(w.lower()) for w in self.words ]))
        w_c = [{ c1: c2 for c1, c2 in np.stack(np.unique(list(w.lower()), return_counts = True), axis= 1)}
               for w in self.words]
        bag = [np.array([int(wt.get(char, 0)) for char in u]) for wt in w_c]

        return list(u), bag
```

![image](https://user-images.githubusercontent.com/8701464/128754164-2af9894b-71ee-4774-9453-be2ffb755246.png)


# Hamming Distance
It is the distance measured between two words assuming both has the same length or it is defined as the number of positions that have symbols between two words of equal length.

![image](https://user-images.githubusercontent.com/8701464/128754190-6617ab28-a203-4153-b0ee-b4a1a40c88dc.png)

```python
    def __hamming_distance(self):

        if self.u.shape != self.v.shape:
            return 'Incorrect lengths'
        elif self.norm:
            return (self.u!=self.v).mean()            
        else:
            return (self.u!=self.v).sum()
```

![image](https://user-images.githubusercontent.com/8701464/128754208-94bc9213-a192-417a-adad-d2c8152bfd40.png)


# Manhattan Distance
Is similar to the Hamming distance, without counting the number of characters not matching and subtracting the difference between each pair of characters at each position of the two words.

![image](https://user-images.githubusercontent.com/8701464/128754227-fece78f8-3306-4d77-bbf8-47e3707d0c3d.png)

```python
    def __manhattan_distance(self):

        if self.u.shape != self.v.shape:
            return 'Incorrect lengths'
        elif self.norm:
            return abs(self.u - self.v).mean()            
        else:
            return abs(self.u - self.v).sum()

```

![image](https://user-images.githubusercontent.com/8701464/128754252-49c8efd7-32f8-4410-815c-a8ea0dfba72a.png)


# Euclidean Distance
It is the shortest straight path distance between two points.

![image](https://user-images.githubusercontent.com/8701464/128754300-10456bab-7593-4875-b4f7-f974be64d94c.png)

```python
    def __euclidean_distance(self):

        if self.u.shape != self.v.shape:
            return 'Incorrect lengths'
        return np.sqrt(np.sum(np.square(self.u - self.v)))

```

![image](https://user-images.githubusercontent.com/8701464/128754307-00b1db64-529a-4b6c-a88e-2a71f6bf7954.png)


# Levenshtein Distance or Wagner-Fischer algorithm
It is somewhat similar to the Hamming distance, is used to measure the distance between two sequence of words based on their differences. In Short, is the minimum number of editions needed (deletions, substitutions or aditions) to convert one word to the other, the length of both words need not be equal.

![image](https://user-images.githubusercontent.com/8701464/
128754319-5976164c-b06b-49a7-8d19-9b020a200bb0.png)

```python
    def __levenshtein_distance(self):

        u = self.u.lower()
        v = self.v.lower()

        if u == v: return 0
        elif len(u) == 0: return len(v)
        elif len(v) == 0: return len(u)

        matrix = []

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
                d_u[j] = d_v[j]
            matrix.append(copy.copy(d_v))
        distance = d_v[len(v)]
        matrix = np.array(matrix)
        matrix = matrix.T
        matrix = matrix[1:,]
        matrix = pd.DataFrame(data = matrix,
                               index= list(v),
                               columns= list(u))

```                               

![image](https://user-images.githubusercontent.com/8701464/128754334-507172c8-281a-4046-8338-0a4a521d738f.png)

![image](https://user-images.githubusercontent.com/8701464/128754348-f350b086-38aa-436f-a9a1-db0d3cf14d72.png)


# Cosine Distance and Cosine similarity
### Remember that:
> The similarity between two words decreases when the distance between its vectors increases
> The similarity between two words increases when the distance between its vectors decreases.

If we have two words represented as a vectors using its numerical representation(Bag of character vectorization), the cosine similarity will give us the measure of the cosine of the angle between the vectors.

- Angle close to 0 means that the cosine similarity is close to 1, both words are very similar.
- Angle close to 90 means that the cosine similarity is close to 0, both words are not similar.
- Angle close to 180 means that cosine similarity is close to -1, both words unrelated.

![image](https://user-images.githubusercontent.com/8701464/128754368-207792c3-397d-44ab-9806-0f8b06c59324.png)

```python

    def __cosine_distance_similarity(self):

        distance = 1.0 - (np.dot(self.u, self.v)/
                          (np.sqrt(sum(np.square(self.u))) * 
                           np.sqrt(sum(np.square(self.v))))
                          )
        return distance
```

![image](https://user-images.githubusercontent.com/8701464/128754380-7baa7023-2e1a-4f25-82f1-722657d045ae.png)

# Summary
- Green is the first option, Yellow is the second option and Orange is the third option
- Hamming, agree with the first option, agree with the second option
- Manhattan, agree with the first option, not agree with the second and third option
- Euclidean, agree with the first option , not agree with the second option
- Levenshtein, agree with the first optionand agree with the second option Cosine, not agree with the first option

![image](https://user-images.githubusercontent.com/8701464/128754404-be063fc4-6468-4c23-828b-3dcb6f3c0ee3.png)

# Contributing and Feedback
Any ideas or feedback about this repository?. Help me to improve it.

# Authors
- Created by <a href="https://www.linkedin.com/in/ramsescoraspe"><strong>Ramses Alexander Coraspe Valdez</strong></a>
- Created on 2021

# License
This project is licensed under the terms of the Apache License.

