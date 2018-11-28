'''
Script que parsea el texto de un pdf a un string
Se convierte cada parrafo en un elemento de una lista
Se busca el nombre de un/una concejal/concejala en cada parrafo,
si se encuentra se guarda en un fichero TXT
'''

import re
import pdftotext

clean_list = []

with open('acta-pleno-010618.pdf', 'rb') as f:
    # Convertimos el PDF en un bloque de texto respetando saltos de parrafo
    pdf = pdftotext.PDF(f)

    # Lo pasamos a un string
    text_file = ' '.join(pdf)

    # Ahora convertimos ese string en una lista, la condición para partir el parrafo es que haya ocho o más espacios en blanco
    line_break = '\s{8,}'
    text_file = re.split(line_break, text_file)

    # Ahora lo volvemos a convertir en string
    text_file = str(text_file)


    # Expresion regular para buscar una palabra
    searchString = re.compile("[^']{0,}(?=\\bfavor\\b)[^']{0,}[^']{0,}(?=\\bcontra\\b)[^']{0,}")

    # Buscamos en la lista la palabra
    matching = searchString.findall(text_file)

    # Lo convertimos en string
    matching = str(matching)

    # En algún proceso se añaden saltos de línea como caracteres \n 🤷🏻‍♂️, lo reemplazamos
    matching = matching.replace('\\n', ' ').replace('\\', '')

    # # Generamos el archivo solo con los parrafos donde se nombra a cada concejal
    with open('prueba.txt', 'w') as archivo:
        archivo.write(matching)
