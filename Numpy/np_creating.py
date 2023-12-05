import numpy as np


def main():
    print(np.zeros(5, dtype=int))

    value = np.zeros([2,3,4]) # it's called tensor
    print(value)
    print(value.ndim)
    print()
    print(np.zeros([2,3]))

    
    #ranges
    print(np.arange(2, 8, 0.5))#last number is the_step meaning it_will_be_added_to_numbers
    print()
    #linearly spaced
    print(np.linspace(4, 8, 4)) #last number is how_numbers_will_return
    print()
    #random
    print(np.random.rand(5))
    print()
    #random, normally distrinuted
    print(np.random.randn(5))
    print()
    #reshape
    print(np.random.rand(9).reshape(3, 3))

if __name__ == "__main__":
    main()