import numpy as np
import sys
# our functions
from tools import buildmodel as mtq
import mnist
# Clustering
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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
y_train_origin = y_train
y_test_origin = y_test
x_train , y_train = mnist.normalize_dataset(x_train, y_train)
x_test, y_test = mnist.normalize_dataset(x_test, y_test)

print("size of the train dataset : ", len(x_train))

model_name = "./trained_model_1_16"

model = mtq.MTQModel(model_name)
load = True
model.build_dense((784,), n_neurons=[32,64, len(y_train[0])], load=load, summary=True)
if not load:
    model.fit(x_train,y_train)

hidden_layers = model.get_hidden_layers_outputs(x_test)

# UMAP
import umap.umap_
import umap.plot

umap.plot.output_notebook()
hover_data = pd.DataFrame({'index':np.arange(len(x_test)),
                           'label':y_test_origin})
for hd in hidden_layers:    
    mapper = umap.umap_.UMAP().fit(hd)
    #p = umap.plot.interactive(mapper, labels=y_test_origin, hover_data=hover_data)
    #umap.plot.show(p)

    umap.plot.points(mapper, labels=y_test_origin)