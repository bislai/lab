import pandas as pd
import numpy as np

dataset = pd.read_csv('datos/Data.csv', encoding = "ISO-8859-1")
print(dataset.info())
print(dataset.head())
print(dataset.iloc[0:5])
# seleccionar filas salteadas
print(dataset.iloc[[0,3,6,24],])

#seleccionar columnas
print(dataset.iloc[:, 0:2])

#seleccionar filas y columnas
print(dataset.iloc[[0,3,6,24], [0,5,6]])
print(dataset.iloc[0:5,5:8])
