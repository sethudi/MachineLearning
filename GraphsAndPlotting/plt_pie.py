
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    plt.pie([1, 2, 3, 4], labels=[1, 2, 3, 4], autopct='%.1f %%')
    plt.show()


if __name__ == "__main__":
    main()