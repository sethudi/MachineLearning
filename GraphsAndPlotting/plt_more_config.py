
import matplotlib.pyplot as plt
import numpy as np

def main():

    x = np.linspace(-15, 15, 200)
    y = np.sin(x)

    plt.figure(figsize=(10, 5))
    plt.axis([-16, 16, -2, 2])
    plt.grid(True)
    plt.plot(x, y, '--', color='darkblue')
    plt.rc('axes', titlesize=20)
    plt.title("y = sin(x)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


if __name__ == "__main__":
    main()