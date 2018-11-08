import pandas as pd

f = open("corpus.txt")

texts = []
labels = []

for line in f:
    [label, text] = line.split("\t")
    texts.append(text.strip())
    labels.append(int(label))

f.close()

print(texts[0])
print(labels[0])

df = pd.DataFrame({
    "text": texts,
    "label": labels
})

print(df.info())

print(df.head())

df.to_csv(open("corpus.csv", "w"))