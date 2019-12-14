# Unsupervised Machine Learning *using* Cloudmesh Cloud AI Services

 
Mohamed Elfateh Abdelgader, [fa19-516-140](https://github.com/cloudmesh-community/fa19-516-140)


## Introduction  

The main objective of this project is to provide AI capabilities on cloud. mainly I am trying to produce an cloud based method that achieves customer segmentation, which is the practice of grouping customers based on features like age, gender, interests, and spending habits. The developed functionalities will be implemented using cloud platforms mainly two nnodes on chameleon. The scope of work for this deployemnt is to build cababilities on the cloud allows recieving feeds in a data form end users and the service shouls interpret these feeds an responds back results as a segmentation representation of the recieved data, this reponse could be a visualization of the clustered data or tabular representation of the data. 

## Clutering & K-means
In todays world everything we practice as human being in our daily activities is tied to a personalized factor, which has been discovered by our services providers, marketing analyzers or data scientists, customer segmentation is the output of this segregation and binding.

In this project demonstration we will see how segmentation of a product line could be done on a pizza product line simple to segments pieces according to their thickness, width, length and weight in order to be mapped as customers desiring. 

K-means

Kmeans clustering is one of the powerful Machine learning algorithm practices that defines and discover segmentation according to their patterns by converging in a finite number of iterations with a computational cost considered the most cost effective and efficient one compare to other clustering practices which is representing as:

`0(k*n*d)` 

Where:

* k represents  the umber of clusters.
* n represents  the umber of data points (cutomers, products ..etc).
* d represents  the umber of attributes (length, width, thikness …etc.).

as our practice will be in python lets explore the needed libraries for that, as we can see all of them can be found on the requirements.txt file:

* numpy
* flask
* connexion[swagger-ui]
* scikit-learn


## Technologies Used 

* Python 3.7
* OpenAPI.
* Connexion
* Development manchine is in MacOS 

## Design

[x] Database design completed.
[x] ML design completed.
[x] API design and coding completed.

## Implementation 

###Architecture Design

## Challenges   

1. Slowlyness when using chameleon VM.

## Conclusion

TBD

## References

1.Applied Unsupervised Learning with Python by Benjamin Johnston, Aaron Jones, Christopher Kruger
2.OpenAPI 3.0 Tutorial. https://app.swaggerhub.com/help/tutorials/openapi-3-tutorial
3.Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems
Book by Geron Aurelien

## Progress

- [x] learned how to create a cloudmesh command
- [x] leraned how to use cloudmesh Config()
- [x] learned how to start a vm on openstack with cloudmesh
- [x] drafted report

* Week Sep 29 - Oct 5
  
  - [x] Collecting info about how to build prober APIs using OpenAPI.
  - [x] learning about different DBs Mongodbg and SQLlite in order to decide which is the most prober fit. 
  
* Week Oct 6 - Oct 12

  - [x] Installing MongoDB and start drafting DB design.
  - [x] loading datafiles in Dev environment.

* Week Oct 6 - Oct 12
- [x] Developing API prototype
- [x] Moving data (xls) to VM (local development env)

* Week Oct 13 - Oct 19
- [x] Developing API finalizations and tunning
- [x] injecting data in Mongodb.
- [x] devloping python Mongodb readers.

* Week Oct 20 - Oct 26
- [x] Developing Python K-means clustering functionalities
- [x] Set up new chameleon instance

* Week Oct 27 - Nov 2
- [x] installing connexion[swagger-ui] 
- [x] testing connexions on chameleon
- [x] testing first API reading in chameleon

* Week Nov 3 - Nov 9
- [x] Download and install Ubuntu on local machine (*had to do it due to the slowlyness on chameleon)
- [x] Moving production enviroment (cloudmesh, swagger-ui ..etc) to the local ubuntu machine
- [x] statrt on prototyping Machine learning scripts


* Week Nov 10 - Nov 16
- [x] testing Codes for unsuprvised ML using K-means 
- [x] Enhancing codes to read data directly from mongodb
- [x] Enhance loaders to load data in Mongodb

* Week Nov 17 - Nov 23
- [x] unifying codes and planning to move everything to chameleon.
- [?] trying to figure out why plotting is not showing results *stucked for a while here

* Week Nov 24 - Nov 30
- [x] drafting the updated report





  
