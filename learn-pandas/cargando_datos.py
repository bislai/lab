import pandas as pd
import numpy as np

dataset = pd.read_csv('datos/Data.csv', encoding = "ISO-8859-1")
print(dataset.info())
print(dataset.head())

nuevo = pd.DataFrame(dataset)

print(nuevo)


nuevo = nuevo.replace(np.nan, '0')

print('Impresión del dataset sin NaN')
print(nuevo.info())

print(nuevo.describe())

print('····Estadísticas solamente de números')
print(nuevo.describe(include=[np.number]))




nuevo=nuevo.replace('N/A', '0')
nuevo=nuevo.replace('NR', '0')

print('Estadísticas sin N/A o NR')

print(nuevo.describe())

print(list(nuevo))
nuevo['Wsets'] = nuevo.Wsets.astype(int)
nuevo['WRank'] = nuevo.WRank.astype(int)

print(nuevo.describe())

nuevo.dropna(how='any', inplace=True)
print(nuevo.head())
