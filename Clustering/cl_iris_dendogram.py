import sklearn.datasets as ds
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

class Iris:
    def __init__(self):
        data = ds.load_iris(as_frame=True)

        self.target = data['target']
        self.target_names = data['target_names']

        self._df = data['data']

    def dendrogram(self):
        X = self._df.iloc[:, 0:4]
        X = StandardScaler().fit_transform(X)
        dendrogram(linkage(X))
        plt.show()

def main():
    iris = Iris()
    iris.dendrogram()

main()

