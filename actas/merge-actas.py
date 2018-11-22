'''
Este script para mergear PDFS esta sacado de aquí: https://www.blog.pythonlibrary.org/2018/04/11/splitting-and-merging-pdfs-with-python/
'''
import glob
from PyPDF2 import PdfFileMerger

def merger(output_path, input_paths):
    pdf_merger = PdfFileMerger()
    file_handles = []

    for path in input_paths:
        pdf_merger.append(path)

    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)

if __name__ == '__main__':
    paths = glob.glob('*.pdf')
    paths.sort()
    merger('todas-las-actas-desde-2015-2019.pdf', paths)
