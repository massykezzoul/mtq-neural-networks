import numpy as np 
from random import randint
from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy

# Data creation
def createData() :
    train_labels = []
    train_samples = []
    for i in range(500):
        # The ~5% of younger individuals who did experience side effects
        random_younger = randint(13,64)
        train_samples.append(random_younger)
        train_labels.append(1)

        # The ~5% of older individuals who did not experience side effects
        random_older = randint(65,100)
        train_samples.append(random_older)
        train_labels.append(0)

    for i in range(10000):
        # The ~95% of younger individuals who did not experience side effects
        random_younger = randint(13,64)
        train_samples.append(random_younger)
        train_labels.append(0)

        # The ~95% of older individuals who did experience side effects
        random_older = randint(65,100)
        train_samples.append(random_older)
        train_labels.append(1)

    train_labels = np.array(train_labels)
    train_samples = np.array(train_samples)

    return shuffle(train_labels, train_samples)

train_labels , train_samples = createData()

scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_samples = scaler.fit_transform(train_samples.reshape(-1,1))

model = Sequential([
    Dense(units=16, input_shape=(1,), activation='relu'),
    Dense(units=32, activation='relu'),
    Dense(units=2, activation='softmax')
])

model.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x=scaled_train_samples, y=train_labels, validation_split=0.1, batch_size=10, epochs=30, verbose=2)