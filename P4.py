from cProfile import label
import pandas as pd
import numpy as np
import scipy.stats as st
from matplotlib import pyplot as plt

#INTERVALOS DE CONFIANZA
monedas = ['Bitcoin', 'Dogecoin', 'Ethereum']
for m in range(len(monedas)):
    csv = 'coin_' + monedas[m] + '.csv'
    
    df = pd.read_csv(csv) 
    df["Prom"] = (df["Open"] + df["Close"])/2 - df["Open"]

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Year'] = df['Date'].dt.year

    df2017 = df[df['Year'] == 2017]
    promedios_bc_2017 = df2017['Prom'].tolist()

    df2018 = df[df['Year'] == 2018]
    promedios_bc_2018 = df2018['Prom'].tolist()
    
    print('')
    print(f'Intervalo de confianza {monedas[m]} (2017-2018)')
    interval_17 = st.norm.interval(0.95, loc=np.mean(promedios_bc_2017), scale=st.sem(promedios_bc_2017))
    print(f'2017: {interval_17}')

    interval_18 = st.norm.interval(0.95, loc=np.mean(promedios_bc_2018), scale=st.sem(promedios_bc_2018))
    print(f'2018: {interval_18}')
    print('')
    
#GRAFICOS PROMEDIOS MENSUALES
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