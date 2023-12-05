
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    word_data = np.loadtxt('wordlengths.csv', delimiter=',', dtype=int)
    
    plt.figure(figsize=(10,5))

    x = [str(number) for number in word_data[:, 0]]
    plt.bar(x, word_data[:, 1])
    plt.grid()
    
    plt.title("Word lengths in Great Expectations")
    plt.xlabel("Word length")
    plt.ylabel("Number of words")
    plt.show()

if __name__ == "__main__":
    main()