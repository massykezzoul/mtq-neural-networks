import sys

import numpy as np
from numpy import save
from numpy import load


from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam

import os.path

# Prend les images et ne garder que les images ne contenant que des 0, 1 et des 2
# Afin de simplifier l'étude.
def cut_data(x, y, keep=[0,1,2]):
    mask = np.isin(y, keep)
    return x[mask], y[mask]


if os.path.isfile("mnist_x_train_012.npy") and \
    os.path.isfile("mnist_y_train_012.npy") and \
    os.path.isfile("mnist_x_test_012.npy") and \
    os.path.isfile("mnist_y_test_012.npy"):
    print("loading local files")
    x_train = load("mnist_x_train_012.npy")
    y_train = load("mnist_y_train_012.npy")
    x_test = load("mnist_x_test_012.npy")
    y_test = load("mnist_y_test_012.npy")
else:
    print("loading from mnist")
    # Télechargement des données
    (x_train , y_train) , (x_test, y_test) = keras.datasets.mnist.load_data(path='all_mnist.npz')

    (x_train , y_train) = cut_data(x_train , y_train)
    (x_test, y_test) = cut_data(x_test, y_test)

    save("mnist_x_train_012.npy", x_train)
    save("mnist_y_train_012.npy", y_train)
    save("mnist_x_test_012.npy", x_test)
    save("mnist_y_test_012.npy", y_test)

print("x_train len : ", len(x_train))
print("y_train len : ", len(y_train))
print("x_test len : ", len(x_test))
print("y_test len : ", len(y_test))


# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255


# Flatten the images.
x_train = x_train.reshape((-1, 784))
x_test = x_test.reshape((-1, 784))


# convert class vectors to binary class matrices
# Ex: 2 will become [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# Creating the model
model = Sequential([
    Dense(16, input_shape=(784,), activation='relu'),
    Dense(10, activation='softmax')
])
#model.summary()
model.compile(optimizer=Adam(learning_rate=0.0001), loss='mean_squared_error', metrics=['accuracy'])
model.fit(x=x_train, y=y_train,batch_size=12, epochs=15, verbose=2)

model.evaluate(
    x_test,
    y_test
)