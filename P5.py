import pandas as pd
import numpy as np
import scipy.stats as st
from matplotlib import pyplot as plt


dfB = pd.read_csv("coin_Bitcoin.csv")
dfE = pd.read_csv("coin_Ethereum.csv") 
dfD = pd.read_csv("coin_Dogecoin.csv")
dfU = pd.read_csv("coin_USDCoin.csv")

dfB["Price"] = (dfB["High"] + dfB["Low"])/2
dfE["Price"] = (dfE["High"] + dfE["Low"])/2
dfD["Price"] = (dfD["High"] + dfD["Low"])/2
dfU["Price"] = (dfU["High"] + dfU["Low"])/2

bit = dfB.sample(n=350, random_state=1)
eth = dfE.sample(n=350, random_state=1)
dog = dfD.sample(n=350, random_state=1)
usd = dfU.sample(n=350, random_state=1)



##################Bitcoin###########################
bit['yyyy'] = pd.to_datetime(bit['Date']).dt.year

bit = bit.sort_values(by=['yyyy'])

medias = bit.groupby('yyyy')['Price'].mean()
vari = bit.groupby('yyyy')['Price'].var()


medias.plot()
plt.title('Media de precio de Bitcoin a lo largo de los años')
plt.xlabel('Años')
plt.show()


vari.plot()
plt.title('varianza de precio de Bitcoin a lo largo de los años')
plt.xlabel('Años')
plt.show()



###################Ethereum#######################
eth['yyyy'] = pd.to_datetime(eth['Date']).dt.year

eth = eth.sort_values(by=['yyyy'])

medias = eth.groupby('yyyy')['Price'].mean()
vari = eth.groupby('yyyy')['Price'].var()


medias.plot()
plt.title('Media de precio de Ethereum a lo largo de los años')
plt.xlabel('Años')
plt.show()


vari.plot()
plt.title('Varianza de precio de Ethereum a lo largo de los años')
plt.xlabel('Años')
plt.show()





##################Dogecoin######################
dog['yyyy'] = pd.to_datetime(dog['Date']).dt.year

dog = dog.sort_values(by=['yyyy'])

medias = dog.groupby('yyyy')['Price'].mean()
vari = dog.groupby('yyyy')['Price'].var()

medias.plot()
plt.title('Media de precio de Dogecoin a lo largo de los años')
plt.xlabel('Años')
plt.show()


vari.plot()
plt.title('Varianza de precio de Dogecoin a lo largo de los años')
plt.xlabel('Años')
plt.show()




##################USDcoin#########################
usd['yyyy'] = pd.to_datetime(usd['Date']).dt.year

usd = usd.sort_values(by=['yyyy'])

medias = usd.groupby('yyyy')['Price'].mean()
vari = usd.groupby('yyyy')['Price'].var()

medias.plot()
plt.title('Media de precio de USDCoin a lo largo de los años')
plt.xlabel('Años')
plt.show()


vari.plot()
plt.title('Varianza de precio de USDCoin a lo largo de los años')
plt.xlabel('Años')
plt.show()
plt.close()
########################################################