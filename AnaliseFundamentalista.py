from yahoofinance import HistoricalPrices
import pandas as pd
from pandas import DataFrame
import pprint
import matplotlib.pyplot as plt
empresa = 'AAPL'
#req = HistoricalPrices(empresa, '2007-01-01', '2020-01-01').to_csv(path="mercado"+empresa+".csv", sep=', ', data_format='raw', csv_dialect='excel')
df = pd.read_csv("mercado"+empresa+".csv", encoding="UTF-8", sep=",")
print(df.head())
print(df.tail())

df.plot(x='Date', y='Close', kind='line')
plt.show()

