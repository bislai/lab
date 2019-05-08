import pandas as pd
import numpy as np

datos = {
    'Nombre':
    ['Chalio', 'Marisol', 'Yolanda', 'Tina'],
    'Calificaciones':
    ['100', '90', '100', '80'],
    'Deportes':
    ['Futbol', 'Natacion', 'Basket', 'Beisbol'],
    'Materias':
    ['Calculo', 'Metodos Numericos', 'Cocina', 'Quimica']
}

df = pd.DataFrame(datos)
print(df)
print('\n' *2)

datos2 = {
    'Nombre':
    ['Chalio', 'Marisol', 'Yolanda', 'N/A'],
    'Calificaciones':
    ['100', '90', np.nan, '80'],
    'Deportes':
    ['Futbol', 'Natacion', 'Basket', 'N/A'],
    'Materias':
    ['Calculo', 'Metodos Numericos', 'N/A', 'Quimica']
}

df2 = pd.DataFrame(datos2)
print(df2)
print('\n' *2)
print(df2.info())
print('\n' *2)

print(df2.describe())
print('\n' *4)

nuevo = pd.DataFrame(df2)

nuevo = nuevo.replace(np.nan, '0')
print(nuevo)


