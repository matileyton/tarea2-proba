from cProfile import label
import pandas as pd
import numpy as np
import scipy.stats as st
from matplotlib import pyplot as plt

monedas = ['Bitcoin', 'Dogecoin', 'Ethereum']
for m in range(len(monedas)):
    csv = 'coin_' + monedas[m] + '.csv'
    
    df = pd.read_csv(csv) 
    df["Prom"] = (df["Open"] + df["Close"])/2

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Year'] = df['Date'].dt.year

    df2017 = df[df['Year'] == 2017]
    promedios_bc_2017 = df2017['Prom'].tolist()

    df2018 = df[df['Year'] == 2018]
    promedios_bc_2018 = df2018['Prom'].tolist()

    '''
    interval_17 = st.norm.interval(0.99, loc=np.mean(promedios_bc_2017), scale=st.sem(promedios_bc_2017))
    print(interval_17[1] - interval_17[0])

    interval_18 = st.norm.interval(0.99, loc=np.mean(promedios_bc_2018), scale=st.sem(promedios_bc_2018))
    print(interval_18[1] - interval_18[0])
    '''

    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septimebre', 'Octubre', 'Noviembre', 'Diciembre']
    dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    prom_meses_2017 = []
    prom_meses_2018 = []

    contador = 0
    for x in dias_meses:
        suma2017 = 0
        suma2018 = 0
        for y in range(1, x + 1):
            suma2017 += promedios_bc_2017[contador]
            suma2018 += promedios_bc_2018[contador]
            contador += 1
            if y == x:
                prom_meses_2017.append(suma2017/x)
                prom_meses_2018.append(suma2018/x)
                break
        
    plt.plot(meses, prom_meses_2017, label= '2017')
    plt.plot(meses, prom_meses_2018, label= '2018')
    plt.title(f'Analisis {monedas[m]} (2017-2018)')
    plt.xticks(rotation=90)
    plt.xlabel('Meses')
    plt.ylabel('Precio Promedio  Moneda')
    plt.legend(loc = "upper center")
    plt.show()