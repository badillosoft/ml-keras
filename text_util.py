#-*- coding: utf-8 -*-
import numpy as np
import re

dictionary = []
words = []
sequences = []
length = 0

def text_to_vec(text):
    return re.sub(r"[^a-z\s]", "", text.lower()).split()

def extract_words(texts_vec):
    words = []
    for text_vec in texts_vec:
        words.extend(text_vec)
    print("Se encontraron {} palabras".format(len(words)))
    return words

def word_frequency(words, word):
    return words.count(word)

def word_index(word):
    if not word in dictionary:
        return 0
    return dictionary.index(word) + 1

def extract_dictionary(words, thresh):
    global dictionary
    dictionary = list(set(words))
    f = lambda word: word_frequency(words, word) >= thresh
    dictionary = list(filter(f, dictionary))
    n = len(dictionary)
    print("Se encontraron {} palabras diferentes".format(n))
    return dictionary

def max_sequence(texts_vec):
    global length
    texts_len = list(map(len, texts_vec))
    length = max(texts_len)
    print("La máxima secuencia de palabras es: {}".format(length))
    return length

def text_to_sequence(text_vec):
    seq = [0] * length
    n = len(text_vec)
    seq[-n:] = list(map(word_index, text_vec))
    return np.array(seq)

def encode_texts(texts):
    texts_vec = list(map(text_to_vec, texts))
    return texts_vec

def encode_sequences(texts_vec):
    global sequences
    sequences = list(map(text_to_sequence, texts_vec))
    return sequences

def generate_sequences(texts, size=0, frac=0.8, thresh=5):
    global length, words, dictionary, sequences
    texts_vec = encode_texts(texts)
    length = max(size, max_sequence(texts_vec))
    words = extract_words(texts_vec)
    dictionary = extract_dictionary(words, thresh)
    sequences = encode_sequences(texts_vec)
    n = len(sequences)
    k = int(frac * n)
    x_train = np.array(sequences[:k])
    x_test = np.array(sequences[k:])
    print("Se analizarán {}/{} secuencias".format(len(x_train), n))
    print("Se validarán {}/{} secuencias".format(len(x_test), n))
    return (x_train, x_test)

def encode_label(categories, label):
    y = [0] * len(categories)
    index = categories[label]
    y[index] = 1
    return y

def generate_labels(labels, frac=0.8):
    categories = {}
    i = 0
    for label in labels:
        if not label in categories:
            categories[label] = i
            i += 1
    l = lambda label: encode_label(categories, label)
    labels_enc = list(map(l, labels))
    n = len(labels_enc)
    k = int(frac * n)
    y_train = np.array(labels_enc[:k])
    y_test = np.array(labels_enc[k:])
    print("Se analizarán {}/{} etiquetas".format(len(y_train), n))
    print("Se validarán {}/{} etiquetas".format(len(y_test), n))
    return (y_train, y_test, categories)