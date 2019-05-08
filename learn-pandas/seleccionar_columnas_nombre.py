import pandas as pd
import numpy as np

dataset = pd.read_csv('datos/Data.csv', encoding= "ISO-8859-1")
print(dataset.head())
dataset.set_index("Location", inplace= True)
print("Melbourne")
print(dataset.loc['Melbourne'])
print("Atlanta y superficie")

print(dataset.loc['Atlanta', 'Surface'])
