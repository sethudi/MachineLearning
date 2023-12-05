
#Variance it the measure of how far spread apart the values are
#standard deviation is the better measure of the spread of values than variance

import numpy as np

def variance(data):
    mean = np.mean(data)

    var = 0
    for value in data:
        var += (value - mean)**2

    var /= len(data)
    return var

def main():
    data1 = np.random.randn(3) # Normal distribution

    print(data1)

    print(np.var(data1))
    print(np.std(data1))

    print(variance(data1))
    print(variance(data1)**0.5)
    
if __name__ == "__main__":
    main()