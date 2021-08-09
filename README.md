# Understanding Similarity Measures for Text Analysis
The aim of this repository  is analyze how similar two words or terms are to each other, Distance metrics are the most common techniques to use for mesure similarities between words, there is an area called Document similarity that is responsible for searching similarities between sentences or paragraphs of text, this document only focuses on individual words or terms. It is worth mentioning that these techniques could be used for spell-checking, autocomplete sentences or correct words or senteces.

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
> Converting to a vector of numerical values using Bag of character vectorization:


```python
    def __bag_characters_vectorize(self):

        u = np.unique(np.hstack([list(w.lower()) for w in self.words ]))
        w_c = [{ c1: c2 for c1, c2 in np.stack(np.unique(list(w.lower()), return_counts = True), axis= 1)}
               for w in self.words]
        bag = [np.array([int(wt.get(char, 0)) for char in u]) for wt in w_c]

        return list(u), bag
```

# Hamming Distance
It is the distance measured between two words assuming both has the same length or it is defined as the number of positions that have symbols between two words of equal length.

# Manhattan Distance
Is similar to the Hamming distance, without counting the number of characters not matching and subtracting the difference between each pair of characters at each position of the two words.

# Euclidean Distance
It is the shortest straight path distance between two points.


# Levenshtein Distance or Wagner-Fischer algorithm
It is somewhat similar to the Hamming distance, is used to measure the distance between two sequence of words based on their differences. In Short, is the minimum number of editions needed (deletions, substitutions or aditions) to convert one word to the other, the length of both words need not be equal.

# Cosine Distance and Cosine similarity
### Remember that:
> The similarity between two words decreases when the distance between its vectors increases
> The similarity between two words increases when the distance between its vectors decreases.

If we have two words represented as a vectors using its numerical representation(Bag of character vectorization), the cosine similarity will give us the measure of the cosine of the angle between the vectors.

- Angle close to 0 means that the cosine similarity is close to 1, both words are very similar.
- Angle close to 90 means that the cosine similarity is close to 0, both words are not similar.
- Angle close to 180 means that cosine similarity is close to -1, both words unrelated.

# Summary
- Green is the first option, Yellow is the second option and Orange is the third option
- Hamming, agree with the first option, agree with the second option
- Manhattan, agree with the first option, not agree with the second and third option
- Euclidean, agree with the first option , not agree with the second option
- Levenshtein, agree with the first optionand agree with the second option Cosine, not agree with the first option