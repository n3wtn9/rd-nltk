from nltk.sentiment.util import *
from nltk.tokenize import sent_tokenize
import os

def run():
    root_input = './data/input'
    root_output = './data/output'

    for filename in os.listdir(root_input):
        with open(os.path.join(root_input, filename)) as fin:
            doc = fin.read()
            sent_tokenize_list = sent_tokenize(doc)
            marked = " ".join([" ".join(mark_negation(sent.split())) for sent in sent_tokenize_list])

            with open(os.path.join(root_output, filename), 'w') as fout:
                fout.write(marked)
