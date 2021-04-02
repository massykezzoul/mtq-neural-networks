import numpy as np
from numpy import save, load
from tensorflow import keras
import os.path

# Prend les images et ne garder que les images ne contenant que des 0 et des 1
# Afin de simplifier l'étude.
def cut_data(x, y, keep=[0,1], n=None):
    new_x = x[np.where(y == keep[0])][:n]
    new_y = y[np.where(y == keep[0])][:n]
    for i in keep[1:]:
        new_x = np.concatenate((new_x , x[np.where(y == i)][:n]))
        new_y = np.concatenate((new_y , y[np.where(y == i)][:n]))

    return new_x, new_y

def normalize_dataset(x_train, y_train):
    # Scale images to the [0, 1] range
    x_train = x_train.astype("float32") / np.amax(x_train)
    # Flatten the images.
    x_train = x_train.reshape((-1, len(x_train[0]) * len(x_train[0][0])))
    # convert class vectors to binary class matrices
    # Ex: 1 will become [0, 1] if len(np.unique(y_train))==2
    y_train = np.array(list(map(lambda x:  [1 if x == k else 0 for k in np.sort(np.unique(y_train))], y_train)))

    return x_train , y_train