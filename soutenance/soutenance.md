# Soutenance

## Introduction

### Problèmatique

Comme l'a dit mon collègue, les réseaux de neurones agissent à la façon d'une boite noire. Aucune information n'est fournit sur son raisonnement. L'objectif de notre projet est donc d'esseyer de comprendre ce qui se passe à l'interieur de cette fameuse boite noire. Concrètement, il s’agit de repérer, selon les données d’entrée, des signatures d’activation de neurones. Une signature correspond au pattern (ou chemin) emprunté par un objet au sein du réseau avant d’arriver à une conclusion. On veut donc analyser les différentes signatures obtenues par différents types de données et de modèles.

Autrement dit, ---- changement de diapo ----

Si on entraine un modèle à reconnaitre des images de 1 et des images de 7. On veux répondre aux questions du type:

voir diapo

### Solution
---- changement de diapo ----

Afin d'arriver à répondre à ces questions, nous devons tout d'abord prendre en main les outils de création de réseaux de neurones et se familiariser avec la base de données MNIST. Puis nous passerons à l'extraction des signatures dont nous venons de parler, pour cela nous utiliserons des algorithmes de clustering. Enfin, avant d'analyser les résultat, nous allons réaliser des interfaces de visualtions en utlisant différentes techniques que nous allons détailler un peu plus loin.

---- changement de diapo ----


## Organisation 

??

## Analyse des données

SHAKIB

## Dev de l'architecture

### technologies utilisées 

MIZOU

### Modèles d'apprentissage

Avant toute chose, il nous faut commencer par définir un réseau de neurones. Nous avons eu le choix entre plusieurs types de réseau. Ils diffèrent par plusieurs paramètres :

- . (chouf diapo)
- .
- .

Nous avons choisi de commencer par utiliser un réseau à maillage dense et avec des paramètres de base. Ceci afin de simplifier, dans un premier temps, les expérimentations. Un réseau à maillage dense est un réseau tel que chaque neurone d’une couche est relié à tous les neurones de la couche précédente et de la couche suivante, comme vous le voyer dans cette figure.

---- CHANGEMENE diapi ----

Puis dans un deuxième temps, nous pourrons changer de modèle afin de passer à un réseau de neurones à convolution 1 (ou CNN). Ils consistent en un empilage multicouche de perceptrons, dont le but est de prétraiter de petites quantités d’informations. Les réseaux neuronaux convolutifs ont de larges applications dans la reconnaissance d’image et de vidéo.

---- CHANGEMENE diapi ----

Nous avons vaguement parlé des signatures dans l'introduction de cette présentation. Concrétement, soit un réseau à N couches cachées, La signature S d’une image qui travesent ce réseau, se définit ainsi : S = (H 1 , ..., H N ), avec H i est le vecteur contenant les valeurs de chaque neurone de la couche i.

Si on prend en exemeple cette figure, la signature d'une image sera un vecteur contenant les valeurs des 128 neurones de cette couche cachée.

---- CHANGEMENE diapi ----

Une fois la signature des images extraite, nous passons à l’analyse de ces dernières. Pour cela, nous utilisant un algorithme de clustering, le K-means. Ce dernier prend en paramètres les données et un certain K donnée par l’utilisateur, puis construit K clusters qui regroupent les données qui sont proches, comme illustré sur cette figure.

Par contre, le K doit être 

---- CHANGEMENE diapi ----



## Analyse des résultats

### Conclusion

