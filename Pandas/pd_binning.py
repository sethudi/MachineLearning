import pandas as pd
import numpy as np

# qcut - separate values into quantiles, where each quantile tries to have the same number of rows in it.
# cut - separate values into ranges, where you either specify the range boundaries, or create equal-sized ranges
def main():
    df = pd.DataFrame(np.random.randn(20), columns=['Price'])

    # qcut will try to create bins. in such a way that  you have the same number of rows.
    df['Category'] = pd.qcut(df['Price'], 4) 

    print(df.groupby('Category').count())

if __name__ == "__main__":
    main()