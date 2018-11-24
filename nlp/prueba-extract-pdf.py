import re
import textract
#read the content of pdf as text
text = textract.process('prueba.pdf')
#use four space as paragraph delimiter to convert the text into list of paragraphs.
print(len(re.split('\s{4,}',str(text))))
