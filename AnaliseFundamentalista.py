from yahoofinance import HistoricalPrices
import pandas as pd
import pprint
import matplotlib.pyplot as plt
import csv
import timeit

with open('empresas-dados-ok', newline='') as f:
    reader = csv.reader(f)
    empresas = list(reader)
dfs = []
for empresa in empresas:
    try:
        dfaux = pd.read_csv("csvs/mercado"+empresa[1]+".csv", encoding="UTF-8", sep=",")
        dfaux['Date'] = pd.to_datetime(dfaux['Date'])
        mask = (dfaux['Date'] > '2019-03-21') & (dfaux['Date'] <= '2020-03-21')
        dfaux = dfaux.loc[mask]
        dfaux = dfaux.dropna()
        dfs.append(dfaux);
        pass
    except:
        print("An exception occurred" + empresa[1])
    pass

start = timeit.default_timer()
df = pd.concat(dfs)
dfJoin = df.dropna()
dfJoin = df[['Date', 'Close']].groupby(['Date']).mean().plot()
stop = timeit.default_timer()
print('Time: ', stop - start)

plt.show()
