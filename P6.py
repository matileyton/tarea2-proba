import pandas as pd
import numpy as np
import scipy.stats as st
from matplotlib import pyplot as plt


if __name__ == "__main__":
    df = pd.read_csv('coin_Tether.csv')
    df["Price"] = (df["High"] + df["Low"])/2

    df100 = df.sample(100, random_state=1)

    #Confianza=0.9
    interval1 = st.norm.interval(0.9, loc=np.mean(df100["Price"].tolist()), scale=st.sem(df100["Price"].tolist()))

    print("Con confianza de 90% =", interval1)

    #Confianza=0.95
    interval2 = st.norm.interval(0.95, loc=np.mean(df100["Price"].tolist()), scale=st.sem(df100["Price"].tolist()))

    print("Con confianza de 95% =", interval2)

    #Confianza=0.99
    interval3 = st.norm.interval(0.99, loc=np.mean(df100["Price"].tolist()), scale=st.sem(df100["Price"].tolist()))

    print("Con confianza de 99% =", interval3)

    tet = df.sample(n=350, random_state=1)
    tet['yyyy'] = pd.to_datetime(tet['Date']).dt.year
    

    tet = tet.sort_values(by=['yyyy'])

    medias = tet.groupby('yyyy')['Price'].mean()
    vari = tet.groupby('yyyy')['Price'].var()


    medias.plot()
    plt.title('Media de precio de Tether a lo largo de los años')
    plt.xlabel('Años')
    plt.show()


    vari.plot()
    plt.title('varianza de precio de Tether a lo largo de los años')
    plt.xlabel('Años')
    plt.show()



