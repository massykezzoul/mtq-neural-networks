# Soutenance

## Introduction

### Les réseaux de neurones

Les réseaux de neurones sont une des méthodes d’apprentissage automatique utilisées en machine learning. Ils sont inspirés du fonctionnement d’un cerveau humain.

### Boite noire

Bien que les réseaux de neurones donnent de bons résultats généralement, leur structure leur donne un effet de boite noire. C'est-à-dire qu'ils permettent de donner des prédictions, mais sans pouvoir expliquer le raisonnement qui les a menés à ces dernières.


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

SHAKIB
## Analyse des données

### Jeu de donnée

### Seléction

### Prétraitement

#### Scaling

#### Flattening

#### one hot encoding

L'encodage one-hot ou encodage 1 parmi n consiste à encoder une variable à n états sur n bits dont un seul prend la valeur 1, le numéro du bit valant 1 étant le numéro de l'état pris par la variable. 

## Dev de l'architecture

### technologies utilisées 

MIZOU

#### Jupyter

Les notebooks Jupyter offrent un excellent moyen d’écrire et d’itérer sur du code Python.
C’est un outil incroyablement puissant pour développer et présenter de manière interactive des projets de science de données.

Jupyter notebook intègre le code et sa sortie dans un document unique qui combine des visualisations, du texte, des équations mathématiques et d’autres médias riches.

#### TensorFlow & Keras

Initialement créé par l’équipe Google Brain à des fins internes, telles que le filtrage du spam sur Gmail, il est devenu open-source en 2015.

Tensorflow est souvent utilisé pour résoudre des problèmes d’apprentissage profond et pour la formation et l’évaluation des processus jusqu’au déploiement du modèle.

Keras est une API de réseau neuronal open source écrite en Python. Il peut fonctionner sur plusieurs frameworks d’apprentissage en profondeur et d’apprentissage automatique.

#### Voilà



### Modèles d'apprentissage

Avant toute chose, il nous faut commencer par définir un réseau de neurones. Nous avons eu le choix entre plusieurs types de réseau. Ils diffèrent par plusieurs paramètres :

- . (chouf diapo)
- .
- .

Nous avons choisi de commencer par utiliser un réseau à maillage dense et avec des paramètres de base. Ceci afin de simplifier, dans un premier temps, les expérimentations. Un réseau à maillage dense est un réseau tel que chaque neurone d’une couche est relié à tous les neurones de la couche précédente et de la couche suivante, comme vous le voyer dans cette figure.

Pour savoir ce qui se passe au milieu on a extrait les output de chaque couche cachées afin de voir à quoi ils ressemblent. Pour ça nous utilisant un algoritheme de clustring, le K-means. Ce dernier prend en paramètres les données et un certain K donnée par l’utilisateur, puis construit K clusters qui regroupent les données qui sont proches, comme illustré sur cette figure.

Par contre, et vu le fonctionnement de K-means, le K ne peut être choisi automatiquement par l'algorithme. Nous passons donc par une méthode qui permet d'évaluer (une façon de donner une note) un clustering. C'est la méthode Silhouette. Comme on peut voir dans ce figure, on voit que le score silhouette est maximal pour la valuer k = 3. Donc il sera optimal de choisir cette valeur.

## Analyse des résultats

### Changement de compertement

En plus, notre solution montre que l'architecture choisi n'est pas optimal et que la deuxième couche ne sert à rien. On pourra donc l'otimiser afin d'utiliser qu'une seule couche.

### Conclusion

