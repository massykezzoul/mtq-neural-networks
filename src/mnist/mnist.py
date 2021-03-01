import numpy as np
from numpy import save
from numpy import load

from tensorflow import keras
import os.path


# Prend les images et ne garder que les images ne contenant que des 0 et des 1
# Afin de simplifier l'étude.
def cut_data(x, y, keep=[0,1], n=50):
    #mask = np.isin(y, keep)
    #x, y = x[mask], y[mask]
    new_x = x[np.where(y == keep[0])][:n]
    new_y = y[np.where(y == keep[0])][:n]
    for i in keep[1:]:
        new_x = np.concatenate((new_x , x[np.where(y == i)][:n]))
        new_y = np.concatenate((new_y , y[np.where(y == i)][:n]))

    return new_x, new_y


def load_mnist(save_dir="./mnist-dataset/"):
    if False and os.path.isfile(save_dir + "mnist_x_train_01.npy") and \
        os.path.isfile(save_dir + "mnist_y_train_01.npy") and \
        os.path.isfile(save_dir + "mnist_x_test_01.npy") and \
        os.path.isfile(save_dir + "mnist_y_test_01.npy"):
        print("loading local files")
        x_train = load(save_dir + "mnist_x_train_01.npy")
        y_train = load(save_dir + "mnist_y_train_01.npy")
        x_test = load(save_dir + "mnist_x_test_01.npy")
        y_test = load(save_dir + "mnist_y_test_01.npy")
    else:
        print("remote loading")
        # Télechargement des données
        (x_train , y_train) , (x_test, y_test) = keras.datasets.mnist.load_data(path='all_mnist.npz')

        (x_train , y_train) = cut_data(x_train , y_train)
        (x_test, y_test) = cut_data(x_test, y_test)
        if False:
            save(save_dir + "mnist_x_train_01.npy", x_train)
            save(save_dir + "mnist_y_train_01.npy", y_train)
            save(save_dir + "mnist_x_test_01.npy", x_test)
            save(save_dir + "mnist_y_test_01.npy", y_test)
    
    return (x_train , y_train) , (x_test, y_test)

def normalize_dataset(x_train, y_train):
    # Scale images to the [0, 1] range
    x_train = x_train.astype("float32") / np.amax(x_train)
    # Flatten the images.
    x_train = x_train.reshape((-1, len(x_train[0]) * len(x_train[0][0])))

    # convert class vectors to binary class matrices
    # Ex: 1 will become [0, 1]
    y_train = keras.utils.to_categorical(y_train, len(np.unique(y_train)))

    return x_train , y_train