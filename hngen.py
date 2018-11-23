# Code from https://gist.github.com/grantslatton/7694811,
# saw at https://news.ycombinator.com/item?id=6815282.

from collections import defaultdict
from random import random
from gzip import open

with open("archive.txt.gz") as archive:
    titles = archive.read().split("\n")
markov_map = defaultdict(lambda: defaultdict(int))

lookback = 2

# Generate map in the form word1 -> word2 -> occurences of word2 after word1
for title in titles[:-1]:
    title = title.split()
    if len(title) > lookback:
        for i in xrange(len(title) + 1):
            markov_map[" ".join(title[max(0, i - lookback) : i])][" ".join(title[i : i + 1])] += 1

# Convert map to the word1 -> word2 -> probability of word2 after word1
for word, following in markov_map.items():
    total = float(sum(following.values()))
    for key in following:
        following[key] /= total


# Typical sampling from a categorical distribution
def sample(items):
    next_word = None
    t = 0.0
    for k, v in items:
        t += v
        if t and random() < v / t:
            next_word = k
    return next_word


def get_sentence(length_max=140):
    while True:
        sentence = []
        next_word = sample(markov_map[""].items())
        while next_word != "":
            sentence.append(next_word)
            next_word = sample(markov_map[" ".join(sentence[-lookback:])].items())
        sentence = " ".join(sentence)
        if any(sentence in title for title in titles):
            continue  # Prune titles that are substrings of actual titles
        if len(sentence) > length_max:
            continue
        return sentence
