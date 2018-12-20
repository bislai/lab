'''
Script que parsea el texto de un pdf a un string
Se convierte cada parrafo en un elemento de una lista
Se busca el nombre de un/una concejal/concejala en cada parrafo,
si se encuentra se guarda en un fichero TXT
'''
import re
import pdftotext

clean_list = []
dp_list = []

list_pln = [
    'plenos/acta-pleno-280915.pdf',
    'plenos/acta-pleno-010618.pdf'
]

for pln in list_pln:

    with open(pln, 'rb') as f:
        # Convertimos el PDF en un bloque de texto respetando saltos de parrafo
        pdf = pdftotext.PDF(f)

        # Lo pasamos a un string
        text_file = ' '.join(pdf)

        # Ahora convertimos ese string en una lista, la condición para partir el parrafo es que haya ocho o más espacios en blanco
        line_break = r'\s{8,}'
        text_file = re.split(line_break, text_file)
        # Filtramos los elementos de la lista vacios
        text_file = list(filter(None, text_file))
        text_file = str(text_file)
        text_file = text_file.replace('\\n', ' ').replace('\\', '')

        # Expresion regular para buscar palabras y discriminar por ellas
        escuer = re.findall('([^\']*(?=Escuer)[^\']*)', text_file)
        votacion = re.findall("[^']{0,}(?=\\bfavor\\b)[^']{0,}[^']{0,}(?=\\bcontra\\b)[^']{0,}", text_file)
        abstencion = re.findall("[^']{0,}(?=\\bfavor\\b)[^']{0,}[^']{0,}(?=\\babstenciones\\b)[^']{0,}", text_file)

        '''
        Recorremos la lista que contiene Escuer con un for. Si los elementos de la lista votacion no están en la lista de votación los almacenamos en final_list
        '''
        final_list = [elem for elem in escuer if elem not in votacion]

        # Hacemos el mismo proceso con abstencion
        clean_list = [elem for elem in final_list if elem not in abstencion]

        # Convertimos la lista en un string
        clean_list = str(clean_list)

        dp_list.append(clean_list)

dp_list = str(dp_list)

# Generamos el archivo solo con los parrafos donde se nombra a cada concejal
with open('escuer.txt', 'w') as archivo:
    archivo.write(dp_list)
