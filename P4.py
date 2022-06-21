import pandas as pd
import numpy as np
import scipy.stats as st

df = pd.read_csv("coin_Bitcoin.csv") 
df["Prom"] = (df["Open"] + df["Close"])/2

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Year'] = df['Date'].dt.year

df2017 = df[df['Year'] == 2017]
promedios_bc_2017 = df2017['Prom'].tolist()

df2018 = df[df['Year'] == 2018]
promedios_bc_2018 = df2018['Prom'].tolist()

interval_17 = st.norm.interval(0.99, loc=np.mean(promedios_bc_2017), scale=st.sem(promedios_bc_2017))
print(interval_17[1] - interval_17[0])

interval_18 = st.norm.interval(0.99, loc=np.mean(promedios_bc_2018), scale=st.sem(promedios_bc_2018))
print(interval_18[1] - interval_18[0])