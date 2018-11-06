from keras.models import Sequential
from keras.layers import Dense
import numpy as np

model = Sequential()
model.add(Dense(16, activation="tanh", input_dim=2))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer="adam", loss="mse")

x = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])

model.fit(x, y, batch_size=32, epochs=2000)

predicts = model.predict(x)

print(predicts)