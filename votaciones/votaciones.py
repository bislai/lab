"""
Este script sirve pa capturar todo el texto de las mociones presentadas
 en el Ayuntamiento de Zaragoza. A partir de lo obtenido nos quedamos con
 los resultados de las votaciones
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import html5lib
from nltk import tokenize

url = input("Introduce la url de votaciones a scrapear: ")

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

"""
Ahora vamos a guardar todo lo extraído en un archivo
Lo primero abrimos el archivo y le damos un nombre
Lo segundo, escribimos todo lo extraído en el archivo
Y lo último, cerramos el archivo.
"""
textoMociones = open('texto-mociones.md', 'w')

textoMociones.write(texto)

textoMociones.close()

"""
Vamos a extraer solamente las votaciones de las mociones
Vamos a usar nltk
"""
texto = listado.text
# Lo partimos en parrafos con nltk
votaciones = tokenize.sent_tokenize(texto)

palabrasR = 'Total votaciones'

# Creamos una nueva lista solo con el elemento que contiene el resultado de las votaciones
resultado = [i for i in votaciones if palabrasR in i]

# Ahora vamos a guardar el resultado de las votaciones
votacionesMociones = open('votaciones-mociones.md', 'w')

votacionesMociones.write(resultado)

votacionesMociones.close()
