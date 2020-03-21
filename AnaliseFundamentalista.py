from yahoofinance import HistoricalPrices
import pandas as pd
from pandas import DataFrame
import pprint
import matplotlib.pyplot as plt
empresas = ['AMZN','TSLA','FB']
dfs = []
for empresa in empresas:
    req = HistoricalPrices(empresa, '2019-03-20','2020-03-20').to_csv(path="mercado"+empresa+".csv", sep=', ', data_format='raw', csv_dialect='excel')
    dfs.append(pd.read_csv("mercado"+empresa+".csv", encoding="UTF-8", sep=","))
    pass
df = pd.concat(dfs)
print(df.shape)
dfJoin = df[['Date','Close']].groupby(['Date']).mean().plot()
plt.show()
    
