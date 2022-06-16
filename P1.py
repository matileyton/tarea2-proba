import pandas as pd
import matplotlib as mpl
import numpy as np
import scipy.stats as st


if __name__ == "__main__":
    df = pd.read_csv("coin_Bitcoin.csv")
    df["Price"] = (df["High"] + df["Low"])/2

    #Para n=25
    df25 = df.sample(25, random_state=1)

    interval1 = st.t.interval(0.95, len(df25["Price"].tolist())-1, loc=np.mean(df25["Price"].tolist()), scale=st.sem(df25["Price"].tolist()))

    print(interval1)

    #Para n=100
    df100 = df.sample(100, random_state=1)

    interval2 = st.t.interval(0.95, len(df100["Price"].tolist())-1, loc=np.mean(df100["Price"].tolist()), scale=st.sem(df100["Price"].tolist()))

    print(interval2)

    #Para n=1000
    df1000 = df.sample(1000, random_state=1)

    interval3 = st.t.interval(0.95, len(df1000["Price"].tolist())-1, loc=np.mean(df1000["Price"].tolist()), scale=st.sem(df1000["Price"].tolist()))

    print(interval3)