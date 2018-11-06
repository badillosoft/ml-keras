import pandas as pd

df = pd.read_csv("data.csv")

print(df.dtypes)
print(df)

x = pd.DataFrame(df, columns=("a", "b"))
y = df["c"]

print(x.shape)
print(x)
print(y.shape)
print(y)