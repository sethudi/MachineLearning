import pandas as pd
import matplotlib.pylab as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def main():
    df = pd.read_csv("grapes.csv")
    print(df.corr())

    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot()
    ax.set_xlabel("Diameter")
    ax.set_ylabel("Weight")

    x = df["diameter"]
    y = df["weight"]

    (x_train, x_test, y_train, y_test) = train_test_split(x, y, shuffle=False, train_size=0.7)
    X_train = [[n] for n in x_train]
    X_test = [[n] for n in x_test]

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_predicted = model.predict(X_test)

    ax.scatter(X_train, y_train, color='green')
    ax.scatter(X_test, y_predicted, color='red')
    ax.scatter(X_test, y_test, color='blue')

    r2 = r2_score(y_test, y_predicted)
    print(r2)

    plt.show()

if __name__ == "__main__":
    main()