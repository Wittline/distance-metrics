# Compute Similarity with Distance Metrics
Distance metrics are one the most importan parts of some machine learning algorithms, supervised and unsupervised learning, It will help us to calculate and measure similarities between numerical values expressed as a data points, below I will expliain five of them:


Understanding Similarity Measures for Text Analysis
Distance Metric of similarity
The aim of this article is analyze how similar two words or terms are to each other, Distance metrics are the most common techniques to use for mesure similarities between words, there is an area called Document similarity that is responsible for searching similarities between sentences or paragraphs of text, this article only focuses on individual words or terms. It is worth mentioning that these techniques could be used for spell-checking, autocomplete sentences or correct words or senteces.
Distance Metric of similarity
There are a lot of Distance metrics that you can use to compute and mesure similarities between entities of text. The measure d is called distance metric of similarity if and only if satisfies the next coditions:
The distance between any two words say X and Y, must be always non-negative
The distance between two words should always be zero if and only if they are identical
The distance measure should always be symmetric, the distance between X and Y muts be equals to the distance between Y and X
The distance measure should satisfy the triangle inequality property

Due to the conditions mentioned above, the Kullback-leibler is a distance measure which violates the third condition and it can not be used for measure similarity between words. 
all similarity distance measures of similarity are not distance metrics of similarity.
Feature engineering
Before start the computation of the distance metrics to check how close two words are, we need to convert the text to numeric values by mapping each letter to a unique numeric value.
Let's imagine the following group of words:
words = ['Similar', 'similares', 'iguales', 'parecidas', 'similaridad', 'isimral', 'similat', 'somiral']
Converting to a vector of numerical values using Character vectorization
Converting to a vector of numerical values using Bag of character vectorization:
Hamming Distance
It is the distance measured between two words assuming both has the same length or it is defined as the number of positions that have symbols between two words of equal length.
Hamming DistanceManhattan Distance
Is similar to the Hamming distance, without counting the number of characters not matching and subtracting the difference between each pair of characters at each position of the two words.
Manhattan DistanceEuclidean Distance
It is the shortest straight path distance between two points.
Euclidean DistanceLevenshtein Distance or Wagner-Fischer algorithm

Levenshtein Distance or Wagner-Fischer algorithmCosine Distance and similarity

Cosine Distance and similarity



