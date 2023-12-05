
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    fig.set_figwidth(16)
    fig.set_figheight(9)

    x = np.random.randn(1000)
    y = np.random.randn(1000)
    z = np.random.randn(1000)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.scatter(x, y, z)

    plt.show()

if __name__ == "__main__":
    main()