
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    print(plt.style.available)
    plt.style.use('classic')

    x = np.linspace(0, 30, 1000)
    y = x**2

    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()