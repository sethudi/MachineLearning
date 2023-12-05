import pandas as pd
import numpy as np


def main():
    df = pd.read_csv("mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']
    
    corr = df.corr()

    print(corr)

if __name__ == "__main__":
    main()