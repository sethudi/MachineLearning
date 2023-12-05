
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

    fig, ax = plt.subplots()

    fig.set_figwidth(10)
    fig.set_figheight(5)
    fig.set_gid(True)

    ax.set_title("Trig Functions")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    
    ax.plot(x, y1, 'blue', label="sin(x)")
    ax.plot(x, y2, 'red', label="cos(x)")

    ax.legend()

    plt.show()

if __name__ == "__main__":
    main()