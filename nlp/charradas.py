from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def convert_pdf_to_txt(path, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(path, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    return text


data = convert_pdf_to_txt('acta-pleno-010618.pdf')

paragraphs = data.split("\n\n")

paragraphs[:] = (value for value in paragraphs if value != '\t')

data = ' '.join(paragraphs)

searchString = '([^\']*(?=hooligan)[^\']*)'

match = re.findall(searchString, str(paragraphs))


print(match)

# print(match.groups())

# tokens = word_tokenize(textFile)

# stop_words = stopwords.words('spanish')

# punctuations = ['(', ')', ';', ':', '[', ']', ',', '.']

# keywords = [word for word in tokens if not word.isnumeric()]

# keywords = [word.lower() for word in keywords]

# keywords = [word for word in keywords if not word in stop_words and not word in punctuations]

# fdist = FreqDist(keywords)

# for word, frequency in fdist.most_common(100):
#     print(u'{};{}'.format(word, frequency))
