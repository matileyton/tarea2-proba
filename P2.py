import pandas as pd
import numpy as np
import scipy.stats as st


if __name__ == "__main__":
    df = pd.read_csv("coin_Bitcoin.csv")
    df["Price"] = (df["High"] + df["Low"])/2

    df100 = df.sample(100, random_state=1)

    #Confianza=0.9
    interval1 = st.norm.interval(0.9, loc=np.mean(df100["Price"].tolist()), scale=st.sem(df100["Price"].tolist()))

    print("Con confianza de 90% = ", interval1)

    #Confianza=0.95
    interval2 = st.norm.interval(0.95, loc=np.mean(df100["Price"].tolist()), scale=st.sem(df100["Price"].tolist()))

    print("Con confianza de 95% = ", interval2)

    #Confianza=1
    interval3 = st.norm.interval(1, loc=np.mean(df100["Price"].tolist()), scale=st.sem(df100["Price"].tolist()))

    print("Con confianza de 100% = ", interval3)