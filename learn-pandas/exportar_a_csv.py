import pandas as pd

dataset = pd.read_csv('datos/Data.csv', encoding="ISO-8859-1")
df = pd.DataFrame(dataset)


dataset.set_index("Location", inplace=True)

df = dataset.loc['Melbourne']

df.reset_index().to_csv('datos_melbourne.csv', header=True, index=False)

df2 = dataset.loc[dataset['Series'].str.endswith('Slam')]
df2.reset_index().to_csv('grand_slam.csv', header=True, index=False)
