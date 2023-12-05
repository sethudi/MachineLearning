
import matplotlib.pyplot as plt
import numpy as np

def main():

    x = np.linspace(0, 30, 1000)
    y = x**2

    plt.figure(figsize=(10, 5))
    plt.grid(True)
    plt.title("$y=x^2$")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(x, y, color='red')
    plt.show()


if __name__ == "__main__":
    main()