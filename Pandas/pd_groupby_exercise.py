import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']
    
    labels=['Young', 'Middle', 'Old']

    df['Age group'] = pd.qcut(df['Age'], 3, labels =labels) 
    groups = df.groupby(['Age group', 'Income'])['Spending'].mean().dropna()

    fig = plt.figure(figsize=(10, 5))
    fig.suptitle("Income vs. Spending")

    for i, label in enumerate(labels):
        group = groups.loc[label]
        ax = fig.add_subplot(1, 3, i+1)
        ax.set_title(label)
        ax.set_xlabel('Income')
        ax.set_ylabel('Spending')
        ax.scatter(group.index, group.values)

    plt.show()

if __name__ == "__main__":
    main()