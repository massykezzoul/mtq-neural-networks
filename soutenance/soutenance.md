# Soutenance


## Introduction

Bonjour Messieurs. Tous d'abord nous vous remercions pour votre présence et toute l'attention que vous allez accorder à notre présentation. Notre groupe se nomme **MTQ** et composé de Bouzidi Belkassim, Elhouiti Chakib et moi même Kezzoul Massili. Pour une partie du projet, il y avais aussi deux autres membres (Dadi Mélissa et Zeroual Ramzi). Mais ils n'ont malheuresement pas pu terminer le projet avec nous et qui n'ont pas pu être présent ajourd'hui avec nous. Ils enverront un e-mail aux responsables du TER expliquant leur situation. Parenthèse faite, Notre sujet s'intitule "Chemins spécifiques pour la classification dans
les réseaux de neurones profonds". Je laisse maintenant M. Bouzidi prendre la parole.

-- MIZOU --
### Les réseaux de neurones


Les réseaux de neurones sont une des méthodes d’apprentissage automatique utilisées en machine learning. Ils sont inspirés du fonctionnement d’un cerveau humain.


### Boite noire

Bien que les réseaux de neurones donnent de bons résultats généralement, leur structure leur donne un effet de boite noire. C'est-à-dire qu'ils permettent de donner des prédictions, mais sans pouvoir expliquer le raisonnement qui les a menés à ces dernières.

-- MASSY --

### Problèmatique

Comme viens de le dire mon collègue, les réseaux de neurones agissent à la façon d'une boite noire. L'objectif de notre projet est d'esseyer de comprendre ce qui se passe à l'interieur de cette fameuse boite noire. Concrètement, il s’agit de repérer, selon les données d’entrée, des signatures d’activation de neurones. Une signature correspond au pattern (ou le chemin) emprunté par un objet au sein du réseau. On veut donc analyser les différentes signatures obtenues par différents types de données et de modèles.

Autrement dit, si on entraine un modèle à reconnaitre des images de 1 et des images de 7. On veux répondre aux questions du type:

voir diapo

---- changement de diapo ----
### Solution

Afin d'arriver à répondre à ces questions, nous devons tout d'abord prendre en main les outils de création de réseaux de neurones. Une fois le réseau créer et entraîner, nous allons récuperer les sortie des couches cachées. Puis nous passerons à l'extraction des signatures dont nous venons de parler. Pour cela, nous utiliserons des algorithmes de clustering. Enfin, avant d'analyser les résultat, nous allons réaliser des interfaces de visualtions en utlisant différentes techniques que nous allons détailler un peu plus loin.

---- changement de diapo ----
CHAKIB

## Organisation 

Maintenant, on va parler de l'organisation du projet. nous avons commencé par essayer de prendre en mains les outils nécéssaires  la réalisation du projet, on essayé aussi de savoir comment fonctionne les réseaux de neurones, d'ailleurs le thème de notre prmière réunions avec monsieur Pascal POncelet était sur le fonctionnement des réseaux de neurones. 

Nous avons également choisi les outils de travail collaboratifs et les principales
technologies utilisées.

après cela, on a decoupé la réalisation de notre projet en 3 grandes parties. 

Premièrement, l'analyse des données, Durant cette étape, nous nous sommes concentrés sur l’analyse des données que nous allions
utiliser. Notamment l’étude de leur structure ainsi que la définition des différents outils utiles pour
leur manipulation.

Ensuite on est passée à la phase de developpement de l'architecture, ça a consisté en l'implementation de plusieurs modèles d’apprentissage
automatique, les outils d’extraction des informations internes aux modèles ainsi que les interfaces
de visualisation des résultats.

Et en dernier on a commencé à annlyser les résultats et c'était un petit peu en parallele avec le developpement de l'architecture. durant cette étape on a effectuer plusieurs expérimentations pour pouvoir en tirer de conclusions et essayer de répondre au question posées lors de la problématique.

Et au final nous avons consacré notre temps à la rédaction du rapport.

Commencons maintenant par l'analyse des données, 

MNIST est un ensemble de données étiqueté qui associe des images de chiffres écrits à la main
avec la valeur du chiffre respectif. Elle contient 70 000 images en noir et blanc de 28 x 28 pixels
représentant des chiffres de zéro à neuf. Chaque pixel de l’image est un entier de valeur comprise
entre 0 et 255 représentant le niveau de gris.

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


-- MASSY --
### Modèles d'apprentissage

Avant toute chose, il nous faut commencer par programmer un réseau de neurones. En utilisant Keras, nous avons définit un réseau à 4 couches. Donc on a la couche d'entré suivit de la première couche chaché avec 32 neurones, puis la deuxième couche cachée avec 64 neurones et enfin la couche de sortie. On a utilisé une structure de couche qu'on appelle 'Dense'. C'est une structure ou tout les neurones sont connectés avec tout les neurones autour d'eux. Il y'en a d'autres possibles mais on a utilisé la plus simple.

Une fois le modèle créer et entraîner. On a extrait les output de chaque couche cachées. 

-- DIAPO --

Pour mieux les comprendre, nous utilisant un algorithme de clustring, le K-means. Ce dernier  (LIT SUR LA DIAPO )  (prend paramètres les données et un certain K donnée par l’utilisateur, puis construit K clusters qui regroupent les données qui sont proches,) comme illustré sur cette figure.

-- DIAPO --

Par contre, et vu le fonctionnement de K-means, le K ne peut être choisi automatiquement par l'algorithme. Nous passons donc par une méthode qui permet d'évaluer (une façon de donner une note) a un clustering. C'est la méthode Silhouette qui attribut à un clustering un score .Plus le score est elevé plus les clusters sont denses. Comme on peut le voir dans cette figure, on voit que le score silhouette est maximal pour la valuer k = 3. Donc il sera plus optimal de choisir cette valeur.

-- CHAKIB --

## Analyse des résultats

### Changement de compertement

En plus, notre solution montre que l'architecture choisi n'est pas optimal et que la deuxième couche ne sert à rien. On pourra donc l'otimiser afin d'utiliser qu'une seule couche.

### Anomalies

Pour répondre à la dernière question, nous faisons passer des images de chiffres que le réseau n'a jamais vu. Par exemple, ici nous insèrons des images de 4.

Nous observant, gràce au diagramme de Sankey, que, dès la première couche cachée, le modèle rapproche les images de 4 plus des 7 que des 1. On peut supposer que le modèle detecte des patterns communs aux 7 et aux 4. Ceci est possiblement dû au faite que les images de 4 sont plus ressemblante aux 7 qu'aux 1.

Nous avons insèrer un autre intru pour voir si il y a une variation avec nos résultats précèdents. 

-- DIAPO --

Nous avons insèrer des images de 3 et on obtient différents résultats. On voit ici, que le modèle trouvais les 3 légérement plus proche des 1. Mais à la fin, ses prédictions étais complètement hasardeuse. On suppose que le modèle n'a pas su detecter, sur les images de 3, des patterns resemblant à ceux des 1 ou des 7.

## Conclusion

- outils de visualisation
- 