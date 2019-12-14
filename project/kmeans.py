#Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans

def kplot(x,y):
    plt.scatter(x[:,0],x[:,1], c=y, cmap='brg')
    plt.title('Kmeans Clustering')
    plt.xlabel('Clusters based on features')
    plt.ylabel('Corresponding error values')
    plt.savefig('kmeans.png')
    return(plt.show())

def clac_kmeans():  
    #import the dataset
    df = pd.read_csv('sample.csv')
    df.head(10)
    x = df.iloc[:, [0,1,2,3]].values
    matplotlib.use('Agg')
    kmeans = KMeans(n_clusters=3)
    y_kmeans = kmeans.fit_predict(x)
    cluster_centres = kmeans.cluster_centers_
    for centroid in cluster_centres:
        plt.scatter(centroid[0],  centroid[1], s=300,  c='black', alpha=0.5)
        kplot(x,y_kmeans)  
