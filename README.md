# Understanding Similarity Measures for Text Analysis
The aim of this repository  is analyze how similar two words or terms are to each other, Distance metrics are the most common techniques to use for mesure similarities between words, there is an area called Document similarity that is responsible for searching similarities between sentences or paragraphs of text, this document only focuses on individual words or terms. It is worth mentioning that these techniques could be used for spell-checking, autocomplete sentences or correct words or senteces.

# Distance Metric of similarity
There are a lot of Distance metrics that you can use to compute and mesure similarities between entities of text. The measure d is called distance metric of similarity if and only if satisfies the next coditions:

- The distance between any two words say X and Y, must be always non-negative
- The distance between two words should always be zero if and only if they are identical
- The distance measure should always be symmetric, the distance between X and Y muts be equals to the distance between Y and X
- The distance measure should satisfy the triangle inequality property
- Due to the conditions mentioned above, the Kullback-leibler is a distance measure which violates the third condition and it can not be used for measure similarity between words.
- all similarity distance measures of similarity are not distance metrics of similarity.


