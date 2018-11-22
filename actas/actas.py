"""
Un pequeño script para descargar todas las actas de la legislatura 2015-2019
"""

from pathlib import Path
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import html5lib

# Creamos la lista que contendra todos los enlaces a los PDFS
list_pdf = []

# Lista con los enlaces de los plenos de la última legislatura
list_url = [
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias.htm',
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias_17.htm',
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias_16.htm',
    'http://www.zaragoza.es/ciudad/organizacion/plenos/activ_plenarias_15.htm']

# Ahora iteramos sobre la lista de URLS
for link in list_url:
    res = requests.get(link)
    data = res.text
    soup = BeautifulSoup(data, 'html5lib')

    '''
    Solo queremos los enlaces que contengan la clase PDF
    y los vamos a guardar en la lista que ya hemos creado
    '''
    for link_pdf in soup.find_all('a', {'class': 'pdf'}):
        list_pdf.append(link_pdf.get('href'))

# Iteramos sobre la lista de enlaces
for file_pdf in list_pdf:
    response = requests.get(file_pdf)
    if file_pdf.find('/'):
        # Nos quedamos solamente con el nombre del archivo y lo guardamos en la variable path
        path = Path(file_pdf.rsplit('/', 1)[1])
        # Ahora guardamos cada PDF con su nombre correspondiente :)
        path.write_bytes(response.content)
