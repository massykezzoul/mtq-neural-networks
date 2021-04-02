import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score,adjusted_rand_score,adjusted_mutual_info_score

# our functions
from tools import buildmodel as mtq
from tools import mnist

# Clustering
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# plot
import umap.umap_
import umap.plot
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def pretraitement(x_train_origin, y_train_origin, x_test_origin, y_test_origin, keep=[0,1], n=None, verbose=False):
    x_train, y_train = mnist.cut_data(x_train_origin, y_train_origin, keep=keep,n=n)
    x_test, y_test = mnist.cut_data(x_test_origin, y_test_origin, keep=keep, n=None)

    x_train, y_train = mnist.normalize_dataset(x_train, y_train)
    x_test, y_test = mnist.normalize_dataset(x_test, y_test)

    if verbose:
        print("size of the train dataset : ", len(x_train))
        print("size of the test dataset : ", len(x_test))
    
    return (x_train, y_train), (x_test, y_test)

def trained_model(x, y, hidden_layers=[32, 64], model_name="./models/trained_model_2_16",verbose=False):
    model = mtq.MTQModel(model_name)

    input_shape = x[0].shape
    n_neurons= hidden_layers + [len(y[0])]
    load=False # Construit le modèle
    
    if verbose:
        print('- input_shape: ', input_shape)
        print('- n_neurons: ', n_neurons)

    model.build_dense(input_shape=input_shape, n_neurons=n_neurons, load=load, summary=False)

    if not load:
        model.fit(x,y, verbose=2 if verbose else 0)

    return model

def get_preditions(model, x, keep, verbose=False):
    result = model.predict(x)
    predictions = []

    for r in result:
        predictions.append(keep[np.argmax(r)])

    predictions = np.array(predictions)
    if verbose:
        print("predictions range: ", np.unique(predictions))

    return predictions

def get_best_k(hidden_layers, kmax=7, verbose=False):
    best_k = []

    if verbose:
        fig, axes = plt.subplots(nrows=len(hidden_layers), ncols=2, sharex=True)
        fig.set_size_inches(15, 9)

    for x, ax in zip(hidden_layers,axes):
        sil = []
        sse = []

        for k in range(1, kmax+1):
            kmeans = KMeans(n_clusters = k, random_state=24).fit(x)
            labels = kmeans.labels_
            if k == 1:
                sil.append(0)
            else:
                sil.append(silhouette_score(x, labels, metric = 'euclidean'))

            centroids = kmeans.cluster_centers_
            pred_clusters = kmeans.predict(x)
            curr_sse = 0
            # calculate square of Euclidean distance of each point from its cluster center and add to current WSS
            for i in range(len(x)):
                curr_center = centroids[pred_clusters[i]]
                curr_sse += np.sqrt(np.sum((x[i] - curr_center) ** 2, axis=0))
            sse.append(curr_sse)
        
        best_k.append(np.array(sil).argmax()+1)
        
        if verbose:
            # ploting
            ax[0].plot(range(1,kmax+1),sil,color='r')
            ax[0].set_xlabel('K values')
            ax[0].set_ylabel('Silhouette score')
            ax[1].plot(range(1,kmax+1),sse, color='g')
            ax[1].set_xlabel('K values')
            ax[1].set_ylabel('Elbow')
            
            ax[0].grid(True)
            ax[1].grid(True)
        
    if verbose: #Verbose
        print("Best K values: ", best_k)
        plt.show()
    
    return best_k

def clustering(hidden_layers, best_k):
    # Clustering with KMeans
    y_kmeans = []
    for hd, k in zip(hidden_layers,best_k):
        y_kmeans.append(KMeans(k,n_init=100,random_state=25).fit_predict(hd))

    return y_kmeans

def umap_plot(x, labels, predictions, hidden_layers, clusters):
    umap.plot.output_notebook()
    hover_data = pd.DataFrame({'index': np.arange(len(x)),
                                'label': labels,
                                'prediction': predictions
                                })

    for hd, cluster in zip(hidden_layers,clusters):    
        plt.figure(figsize=(15, 5))
        mapper = umap.umap_.UMAP().fit(hd)
        hover_data['kmeans'] = cluster
        p = umap.plot.interactive(mapper, labels=cluster, hover_data=hover_data,width=800,height=300)
        umap.plot.show(p)

def sankey(labels, keep, best_k, clustering, predictions):
    # sankey data conversion
    clusters = []
    list_dict_c = [{value:i for i, value in enumerate(keep)}]
    index = len(keep)

    for k in best_k:
        clusters += ["C"+str(j) for j in range(k)]
        list_dict_c.append({value:value+index for value in range(k)})
        index += k
        
    list_dict_c.append({value:i+index for i, value in enumerate(keep)})

    label = keep + clusters + keep 
    list_y = [labels] + [y for y in clustering] + [predictions]

    source, target, value = [], [], []
    for i in range(len(list_y)-1):
        for s, t, v in zip(list_y[i], list_y[i+1], list_y[0]):
            source.append(list_dict_c[i][s])
            target.append(list_dict_c[i+1][t])
            value.append(v)

    node = dict(
        pad = 15,
        thickness = 15,
        line = dict(color = "black", width = 0.25),
        label = label,
        color = "blue"
        )
    link = dict(
        source = source, # indices correspond to labels
        target = target,
        value = [1 for t in target],
        label = value
    )

    data=[go.Sankey(node=node, link=link)]
    fig = go.Figure(data=data)

    fig.update_layout(title_text="Sankey Diagram", font_size=15)
    fig.show()