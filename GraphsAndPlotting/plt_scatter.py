
import matplotlib.pyplot as plt
import numpy as np

def main():
    NVALUES = 1000

    x = np.random.randn(NVALUES)
    y = np.random.randn(NVALUES)

    plt.figure(figsize=(10, 10))
    plt.axis([-5, 5, -5, 5])
    plt.scatter(x, y, s=100)
    plt.show()


if __name__ == "__main__":
    main()