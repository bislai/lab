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

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html5lib')

# Como la estructura de HTML es la mugre hay que hacer piruetas. Buscamos un h3 que contenga MOCIONES
mociones = soup.find('h3', string='MOCIONES')

# Ahora buscamos el ul que esta a continuación del h3, ya que este es el que contiene las mociones
listado = mociones.findNext('ul')

# Buscamos todos los enlaces
tags = listado.find_all('a')

# Ahora vamos a guardar todo en un CSV, lo primero es crearlo
fileCSV = csv.writer(open('pleno-del.csv', 'w'))
# Ahora añadimos las columnas del CSV
fileCSV.writerow(['Numero', 'Partido', 'Enlace'])

for tag in tags:
    # Nos quedamos con el contenido del enlace
    partido = tag.contents[0]
    # Ahora nos quedamos con el enlace
    link = tag.get('href')
    # Y por último nos quedamos con el número de moción, que siempre esta por delante del enlace de la moción
    numeroMocion = tag.previousSibling

    # Ahora le pasamos todos los parametros al CSV que hemos creado anteriormente
    fileCSV.writerow([numeroMocion, partido, link])
