# Chemins spécifiques pour la classification dans les réseaux de neurones profonds

## Contexte

Projet dans le cadre d'un TER de Master 1, faculté des sciences de l'Université de Montpellier.
L'objectif est ici de mieux comprendre comment s'exécute un réseau de neurones profonds. Il s'agit de repérer des signatures d'activation au sein des couches cachés du réseau en fonction des données d'entrée pour répondre aux questions du type :

- Si le jeu d'apprentissage ne contient que des 1 et des 3 quels sont les neurones qui sont activés
et comment ? que se passe-t-il si le modèle est appliqué sur un 2 ?
- Existe-t-il des signatures caractéristiques de certaines données ?
- A partir de quand (quelle couche ?) le modèle change de comportement pour reconnaître une
valeur ?

## Structure du projet

* doc: Bibliographie
* src: code sources des différents réseaux 

## Outils utilisés

L'implémentation des divers modèles s'est faite principalement en [Python3](https://www.python.org/download/releases/3.0/).
Afin de faciliter l'implémentation et la visualisation des résultats, plusieurs modules python et autres projets sont utiliser au sein de ce projet.

- [scikit-learn](https://scikit-learn.org/stable/) inclus dans [TensorFlow](https://www.tensorflow.org/)
- [Pandas](https://pandas.pydata.org/) et [Matplotlib](https://matplotlib.org/stable/index.html)
- [Jupyter](https://jupyter.org/install)

## Prise en main


## Membres

- Bouzidi Belkassem
- Dadi Mélissa
- Elhouiti Chakib
- Kezzoul Massili 
- Zeroual Ramzi

Encadrant: Pascal poncelet <Pascal.Poncelet@lirmm.fr>

## Bibliographie

* [Plotting UMAP](https://umap-learn.readthedocs.io/en/latest/plotting.html)
* [Clustering](https://umap-learn.readthedocs.io/en/latest/clustering.html)
* [Faire du Clustering avec l'algorithme K-means](https://ledatascientist.com/faire-du-clustering-avec-lalgorithme-k-means/)
* [Pattern Signatures](https://www.lirmm.fr/~poncelet/RN/)