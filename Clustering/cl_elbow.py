import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def plot(df):
    fig = plt.figure(figsize=(16, 9))
    ax = fig.add_subplot()
    ax.scatter(df['income'], df['spending'], c=df['cluster'], cmap='plasma')
    ax.set_xlabel('Income')
    ax.set_ylabel('Spending')
    plt.show()

def plot_elbow(df, max):
    plot ={}

    for n in range(2, max +1):
        inertia = cluster(df, n)
        plot[n] = inertia

    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot()
    ax.set_xlabel('Numer of clusters')
    ax.set_ylabel('Inertia')
    ax.plot(plot.keys(), plot.values())
    plt.show()

def cluster(df, n):
    X = df[['income', 'spending']]
    model = KMeans(n_clusters= n)
    model.fit(X)
    df['cluster'] = model.labels_
    print(model.inertia_)
    print(df['cluster'] )
    return model.inertia_

def main():
    df = pd.read_csv('mall_customers.csv')
    df.columns = ['id', 'gender', 'age', 'income', 'spending']

    cluster(df, 5)
    plot_elbow(df, 10)
    #plot(df)

main()