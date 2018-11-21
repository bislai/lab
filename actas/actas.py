"""
Un pequeño script para descargar todas las actas de la legislatura 2015-2019
"""

import csv
import requests
from bs4 import BeautifulSoup
import html5lib

# Lista con los enlaces de los plenos de la última legislatura
lista_url = [
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias.htm',
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias_17.htm',
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias_16.htm',
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias_15.htm']

# Creamos un CSV
with open('actas-pdf.csv', 'w') as f:

    # Activamos la escritura
    fileCSV = csv.writer(f)
    # Creamos la columna
    fileCSV.writerow(['Enlace'])

    # Ahora iteramos sobre la lista de URLS
    for link in lista_url:
        res = requests.get(link)
        data = res.text
        soup = BeautifulSoup(data, 'html5lib')

        # Solo queremos los enlaces que contengan la clase PDF
        pdf = soup.find_all('a', {'class': 'pdf'})

        # Volvemos a iterar sobre la lista de enlaces que contienen la clase PDF
        for elem in pdf:
            # Ahora nos quedamos solamente con el enlace ya que no contienen mucha más información
            link = elem.get('href')
            fileCSV.writerow([link])
