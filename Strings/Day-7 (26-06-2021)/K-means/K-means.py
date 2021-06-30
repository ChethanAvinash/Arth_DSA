import numpy as n
from sklearn.datasets import make_blobs

class KMeans:
    
    def __init__(self,k=5,n_iter=20):
        self.k=k
        self.n_iter=n_iter
        self.clusters=[[] for i in range(k)]
        self.centers=[]
    
    def predict(self,x):
        self.x=x
        n_samples,n_features=x.shape
        self.centers=[X[n.random.choice(X.shape[0], size=1, replace=False),:][0] for i in range(self.k)]
        for i in range(self.n_iter):
            self.clusters=self.getCluster()
            self.centers=self.getNewCenter()

    def distance(self,x1,x2):
        # Manhattan Distance
        return sum(abs(x1-x2))
    
    def getCluster(self):
        clusters=[[] for _ in range(self.k)]
        for i in range(self.x.shape[0]):
            d=[]
            for j in range(self.k):
                d.append(self.distance(self.x[i],self.centers[j]))
            index=n.argmin(d)
            clusters[index].append(self.x[i])
        return clusters
            
    def getNewCenter(self):
        centers=[]
        for i in range(self.k):
            mean=n.mean(self.clusters[i],axis=0)
            centers.append(mean)
        return centers
    
    
# Generating Data with 4 features
X,_=make_blobs(n_samples=200,n_features=4,centers=5,random_state=10)
k=KMeans()
k.predict(X)
print(k.centers)