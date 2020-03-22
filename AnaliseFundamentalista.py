from yahoofinance import HistoricalPrices
import pandas as pd
from pandas import DataFrame
import pprint
import matplotlib.pyplot as plt
import csv
import timeit




with open('empresas', newline='') as f:
    reader = csv.reader(f)
    empresas = list(reader)

dfs = []
for empresa in empresas:
    print(empresa[1])
    req = HistoricalPrices(empresa[1], '1990-03-20','2020-03-21').to_csv(path="mercado"+empresa[1]+".csv", sep=', ', data_format='raw', csv_dialect='excel')
    dfs.append(pd.read_csv("mercado"+empresa[1]+".csv", encoding="UTF-8", sep=","))
    pass

start = timeit.default_timer()
df = pd.concat(dfs)
dfJoin = df[['Date','Close']].groupby(['Date']).sum().plot()
print(df.shape)
stop = timeit.default_timer()
print('Time: ', stop - start)  
plt.show()