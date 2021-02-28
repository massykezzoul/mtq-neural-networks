import numpy as np

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam

import os.path
import sys

# Clustering
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# our functions
import mnist

# MacOS support
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


save_dir="./mnist-dataset/"
(x_train , y_train) , (x_test, y_test) = mnist.load_mnist(save_dir)
x_train , y_train = mnist.normalize_dataset(x_train, y_train)
x_test, y_test = mnist.normalize_dataset(x_test, y_test)

print("Len of train dataset : ", len(x_train))
print("Len of test dataset : ", len(x_test))

model_name = "./trained_model_1_16"

if (os.path.isdir(model_name)):
    model = keras.models.load_model(model_name)
else:
    # Creating the model
    model = Sequential([
        Dense(16, input_shape=(784,), activation='relu'),
        Dense(2, activation='softmax')
    ])

    model.compile(optimizer=Adam(learning_rate=0.0001), loss='mean_squared_error', metrics=['accuracy'])
    model.fit(x=x_train, y=y_train,batch_size=12, epochs=15, verbose=2)
    #model.summary()

    model.save(model_name)

    model.evaluate(
        x_test,
        y_test
    )

first_hidden_layer = model.layers[0]
extractor = keras.Model(inputs=model.inputs,
                            outputs=[first_hidden_layer.output])
first_hidden_output = extractor(x_train) # sorties du premiers hidden layers 
print(first_hidden_output)


# Clustering
cluster = KMeans(3).fit(first_hidden_output)
y_kmeans = cluster.predict(first_hidden_output)

plt.scatter(first_hidden_output[:, 0], first_hidden_output[:, 1], c=y_kmeans, s=50, cmap='viridis')

centers = cluster.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

plt.show()