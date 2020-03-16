from yahoofinance import HistoricalPrices
import pandas as pd
from pandas import DataFrame
import pprint
import matplotlib.pyplot as plt

#req = HistoricalPrices('AAPL', '2000-01-01', '2020-01-01').to_csv(path="mercado.csv", sep=', ', data_format='raw', csv_dialect='excel')
df = pd.read_csv("mercado.csv", encoding="UTF-8", sep=",")
print(df.head())
df.plot(x='Date', y='Close', kind='line')
plt.show()

