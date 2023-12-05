import pandas as pd
import numpy as np

def main():
    df = pd.read_csv("mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']
    
    gp = df.groupby(by="Gender")

    print(type(gp))

    male_dataframe = gp.get_group('Male')
    print(type(male_dataframe))

    male_income_series = male_dataframe['Income']
    print(type(male_income_series))

if __name__ == "__main__":
    main()