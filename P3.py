import pandas as pd
import numpy as np
import scipy.stats as st


if __name__ == "__main__":
    dfB = pd.read_csv("coin_Bitcoin.csv")
    dfB["Price"] = (dfB["High"] + dfB["Low"])/2

    dfA = pd.read_csv("coin_Ethereum.csv")
    dfA["Price"] = (dfA["High"] + dfA["Low"])/2

    dfS = pd.read_csv("coin_Dogecoin.csv")
    dfS["Price"] = (dfS["High"] + dfS["Low"])/2

    dfSt = pd.read_csv("coin_USDCoin.csv")
    dfSt["Price"] = (dfSt["High"] + dfSt["Low"])/2

    intervalB = st.norm.interval(0.99, loc=np.mean(dfB["Price"].tolist()), scale=st.sem(dfB["Price"].tolist()))

    intervalA = st.norm.interval(0.99, loc=np.mean(dfA["Price"].tolist()), scale=st.sem(dfA["Price"].tolist()))

    intervalS = st.norm.interval(0.99, loc=np.mean(dfS["Price"].tolist()), scale=st.sem(dfS["Price"].tolist()))

    intervalSt = st.norm.interval(0.99, loc=np.mean(dfSt["Price"].tolist()), scale=st.sem(dfSt["Price"].tolist()))

    print("IDC Bitcoin: ", intervalB, " Variabilidad: ", intervalB[1]-intervalB[0])
    print("IDC Ethereum: " , intervalA, " Variabilidad: ", intervalA[1]-intervalA[0])
    print("IDC Dogecoin: ", intervalS, " Variabilidad: ", intervalS[1]-intervalS[0])
    print("IDC USDCoin: ", intervalSt, " Variabilidad: ", intervalSt[1]-intervalSt[0])