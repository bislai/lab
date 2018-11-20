"""
Este script sirve para generar un CSV con:
    - El número de la moción
    - El partido que lo ha presentado
    - La url con la moción completa
"""

from bs4 import BeautifulSoup
import requests
import html5lib
import csv

# url = input("Introduce la url de los acuerdos a scrapear: ")

url = 'https://www.zaragoza.es/sede/portal/organizacion/plenos/servicio/fehaciente/70554'

dia = input("Introduce el dia del pleno: ")

mes = input("Introduce el mes del pleno: ")

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html5lib')

# Como la estructura de HTML es la mugre hay que hacer piruetas. Buscamos un h3 que contenga MOCIONES
mociones = soup.find('h3', string='MOCIONES')

# Ahora buscamos el ul que esta a continuación del h3, ya que este es el que contiene las mociones
listado = mociones.findNext('ul')

# Buscamos todos los enlaces
mocionesLink = listado.find_all('a')

# Ahora vamos a guardar todo en un CSV, lo primero es crearlo
fileCSV = csv.writer(open('pleno-del-' + dia + '-del-' + mes + '.csv', 'w'))
# Ahora añadimos las columnas del CSV
fileCSV.writerow(['Numero', 'Partido', 'Enlace', 'Texto'])

for elem in mocionesLink:
    # Nos quedamos con el contenido del enlace
    partido = elem.contents[0]
    # Ahora nos quedamos con el enlace
    link = elem.get('href')
    # Y por último nos quedamos con el número de moción, que siempre esta por delante del enlace de la moción
    numeroMocion = elem.previousSibling

    # Nos quedamos con el texto de la moción que siempre esta a continuación del enlace, eliminamos las comas para que no de problemas con el CSV
    textoMocion = elem.nextSibling.replace(',', ' ')

    # Ahora le pasamos todos los parametros al CSV que hemos creado anteriormente
    fileCSV.writerow([numeroMocion, partido, link, textoMocion])

