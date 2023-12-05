import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

def main():
    df = pd.read_csv("weights.csv", index_col=0, sep='\s+')
    print(df)
    major_ticks = range(0, len(df.index), 7)
    labels = [df.index[x] for x in major_ticks]

    fig = plt.figure(figsize=(16, 9))
    ax = fig.add_subplot()
    ax.set_xticks(ticks=major_ticks, labels=labels, rotation='vertical', minor=False)
    ax.set_xticks(ticks=range(len(df.index)), minor=True)
    ax.tick_params(axis='x', which='major', labelsize=10)
    ax.tick_params(axis='x', which='minor')
    fig.suptitle("Weight Vs Time")
    ax.grid()
    ax.set_xlabel("Data")
    ax.set_ylabel("Weight(kg)")


    x = np.arange(len(df.index))
    y = df['weight']

    (x_train, x_test, y_train, y_test) = train_test_split(x, y, shuffle=False, train_size=0.7)

    ax.plot(x, y)
    plt.show()

    
if __name__ == "__main__":
    main()