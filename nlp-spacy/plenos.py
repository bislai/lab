'''
Casi todo el código esta sacado de este ejemplo:
https://github.com/Jcharis/Natural-Language-Processing-Tutorials/blob/master/Training%20the%20Named%20Entity%20Recognizer%20in%20SpaCy.ipynb
'''
# Load Packages
from __future__ import unicode_literals, print_function
import random
from pathlib import Path
import spacy
from tqdm import tqdm

nlp1 = spacy.load('es')
docx1 = nlp1(u"¿Quién es Sandra Escuer?")

for token in docx1.ents:
    print(token.text, token.start_char, token.end_char, token.label_)

docx2 = nlp1(u"¿Quién es Azcón?")

for token in docx2.ents:
    print(token.text, token.start_char, token.end_char, token.label_)

docx3 = nlp1(u"¿Quién es Rivarés?")

for token in docx3.ents:
    print(token.text, token.start_char, token.end_char, token.label_)

# training data
TRAIN_DATA = [
    ('¿Quién es Sandra Escuer?', {
        'entities': [(10, 23, 'PER')]
    }),
     ('¿Quién es Azcón?', {
        'entities': [(10, 15, 'PER')]
    }),
    ('Estamos en Zaragoza que es la capital de Aragón.', {
        'entities': [(11, 19, 'LOC'), (41, 47, 'LOC')]
    }),
    ('El pleno del Ayuntamiento de Zaragoza.', {
        'entities': [(13, 37, 'ORG')]
    }),
    ('El concejal Azcón ha votado en contra del Ayuntamiento.', {
        'entities': [(12, 17, 'PER'), (42, 54, 'ORG')]
    }),
    ('¿Quién es quién en el pleno', {
        'entities': []
     })
]


# Define our variables
modelo = None
output_dir = Path("/Users/jorgeatgu/github/scraping/nlp-spacy/model")
n_iter = 100

if modelo is not None:
    nlp = spacy.load(modelo)  # load existing spaCy modelo
    print("Cargando el modelo '%s'" % modelo)
else:
    nlp = spacy.blank('es')  # create blank Language class
    print("Created blank 'es' modelo")

# #### Set Up the Pipeline
if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner, last=True)

# otherwise, get it so we can add labels
else:
    ner = nlp.get_pipe('ner')

# add labels
for _, annotations in TRAIN_DATA:
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])

# get names of other pipes to disable them during training
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):  # only train NER
    optimizer = nlp.begin_training()
    for itn in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in tqdm(TRAIN_DATA):
            nlp.update(
                [text],  # batch of texts
                [annotations],  # batch of annotations
                drop=0.5,  # dropout - make it harder to memorise data
                sgd=optimizer,  # callable to update weights
                losses=losses)
        print(losses)

# test the trained modelo
for text, _ in TRAIN_DATA:
    doc = nlp(text)
    print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
    print('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])

# #### Save the modelo
# save modelo to output directory
if output_dir is not None:
    output_dir = Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir()
    nlp.to_disk(output_dir)
    print("Guardando el modelo", output_dir)

    # test the saved modelo
    print("Cargando el modelo guardado", output_dir)
    nlp2 = spacy.load(output_dir)
    for text, _ in TRAIN_DATA:
        doc = nlp2(text)
        print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
        print('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])
