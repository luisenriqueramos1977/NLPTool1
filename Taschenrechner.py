from tkinter import *

import nltk
sentence = [("the", "DT"),("book",
"NN"),("has","VBZ"),("many","JJ"),("chapters","NNS")]
chunker=nltk.RegexpParser(r'''
NP:{<DT><NN.*><.*>*<NN.*>}
}<VB.*>{
''')
chunker.parse(sentence)
Output=chunker.parse(sentence)
Output.draw()
