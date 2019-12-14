#Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans

def kplot(x,y):
    plt.scatter(x[:,0],x[:,1], c=y, cmap='brg')
    plt.title('Kmeans Clustering')
    plt.xlabel('No of clusters')
    plt.ylabel('Error')
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
    kmeans.cluster_centers_
    kplot(x,y_kmeans)    

clac_kmeans()
