#-*- coding: utf-8 -*-
import pandas as pd
import re

df = pd.read_csv("corpus.csv")

print(df.info())
print("-" * 20)

df["text"] = df["text"].map(lambda text: text.lower())

print(df.head())
print("-" * 20)

total_words = []
texts_words = []
max_words = 0

for text in df["text"]:
    words = re.sub(r'[^a-zA-Z0-9\s]', '', text).split()
    texts_words.append(words)
    total_words.extend(words)
    if len(words) > max_words:
        max_words = len(words)

print("Últimas 5 palabras: {}".format(total_words[-5:]))
print("Primer texto: {}".format(texts_words[0]))

word_index = {}

for word in total_words:
    if not word in word_index:
        word_index[word] = 1
        continue
    word_index[word] += 1

THRESH = 5

word_index_thresh = {}

for word in word_index:
    if word_index[word] >= THRESH:
        word_index_thresh[word] = word_index[word]

print("Total de palabras: {}".format(len(word_index)))
print("Mayores al umbral: {}".format(len(word_index_thresh)))

def word_to_vec(words):
    vec = [0] * max_words
    i = 0
    for word in words:
        if word in word_index_thresh:
            vec[i] = word_index_thresh[word]
        i += 1
    return vec

print("Vector primer texto: {}".format(word_to_vec(texts_words[0])))