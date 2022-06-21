import pandas as pd
import numpy as np
import scipy.stats as st


dfB = pd.read_csv("coin_Bitcoin.csv")
dfE = pd.read_csv("coin_Ethereum.csv") 
dfD = pd.read_csv("coin_Dogecoin.csv")
dfU = pd.read_csv("coin_USDCoin.csv")
   

bit = dfB.sample(n=350, random_state=1)
eth = dfE.sample(n=350, random_state=1)
dog = dfD.sample(n=350, random_state=1)
usd = dfU.sample(n=350, random_state=1)

bit = bit.sort_values(by=['Date'])

print(bit)

#'Date':str(i[3])[0:10]

