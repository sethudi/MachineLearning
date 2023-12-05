import numpy as np


def main():
    num = np.arange(16).reshape(4,4)

    print(num)
    print()
    print(num[[1,2],[0,3]]) #advanced indexing creates a copy from the original list
    print(num[num % 2 == 0])

if __name__ == "__main__":
    main()