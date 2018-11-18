from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import html5lib

# La url de la moción que vamos a scrapear
url = 'http://www.zaragoza.es/sede/portal/agenda-institucional/servicio/fehaciente/70422'

# Simulamos ser un navegador
header = {'User-Agent': 'Mozilla/5.0'}

# Pasamos la url y el header a la petición
req = Request(url,headers=header)

# Abrimos la url
page = urlopen(req)

# Ahora lo scrapeamos con beautiful soup usando el parser html5lib
soup = BeautifulSoup(page, 'html5lib')

# Como la estructura de HTML es la mugre hay que hacer piruetas. Buscamos un h3 que contenga MOCIONES
mociones = soup.find('h3', string='MOCIONES')

# Ahora le decimos que se quede solo con el <ul> a continuación del <h3>MOCIONES</h3>, el cual contiene las mociones

listado = mociones.findNext('ul')

# PELIGRO: esto de arriba es posible que no funciones con todas: http://www.zaragoza.es/sede/portal/agenda-institucional/servicio/fehaciente/70863 aquí deciden meter un <p> por en medio 🤷🏻‍♂️ y las siguientes votaciones continuan en otro <ul>.

# Solo queremos el texto
texto = listado.text

votaciones = 'votaciones'
tags = soup.find_all('li', text=lambda t: t and votaciones in t)
print(tags)


# print(unanimidad)

# for i in listado():
#     votaciones = listado.find('li')
#     print(i)


# print(texto)
