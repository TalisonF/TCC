from yahoofinance import HistoricalPrices
import pandas as pd
import matplotlib.pyplot as plt
import csv

def getDadosEmpresas(nomeArquivo):
    with open(nomeArquivo, newline='') as f:
        reader = csv.reader(f)
        empresas = list(reader)
    for empresa in empresas:
        try:
            req = HistoricalPrices(empresa[1], '2000-01-01','2020-03-21').to_csv(path="csvs/mercado"+empresa[1]+".csv", sep=', ', data_format='raw', csv_dialect='excel')
            pass
        except:
            print("An exception occurred" + empresa[1])
        pass
    pass


