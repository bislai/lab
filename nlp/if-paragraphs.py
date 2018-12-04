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
    line_break = r'\s{8,}'
    text_file = re.split(line_break, text_file)
    text_file = list(filter(None, text_file))
    another_list = text_file
    text_file = str(text_file)
    text_file = text_file.replace('\\n', ' ').replace('\\', '')

    # Expresion regular para buscar una palabra
    escuer = re.findall('([^\']*(?=Escuer)[^\']*)', text_file)
    votacion = re.findall("[^']{0,}(?=\\bfavor\\b)[^']{0,}[^']{0,}(?=\\bcontra\\b)[^']{0,}", text_file)

    final_list = [elem for elem in escuer if elem not in votacion]
    print(len(final_list))

    final_list = str(final_list)




    # Generamos el archivo solo con los parrafos donde se nombra a cada concejal
    with open('escuer.txt', 'w') as archivo:
        archivo.write(final_list)
