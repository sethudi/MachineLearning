
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(0, 20, 1000)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # plt.figure(figsize=(10,5))
    # plt.grid()
    # plt.plot(x, y1, x, y2)
    # plt.show()

    #fig, axes = plt.subplots(2, 2)
    fig = plt.figure()

    fig.set_figwidth(16)
    fig.set_figheight(9)
    fig.suptitle("Trig Functions")

    #ax = axes[0][0]
    ax = fig.add_subplot(3, 2, 1)
    ax.set_title("sin(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.plot(x, y1)

    #ax = axes[1][1]
    ax = fig.add_subplot(3, 2, 6)
    ax.set_title("cos(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.plot(x, y2)

    plt.show()

if __name__ == "__main__":
    main()