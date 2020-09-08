import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import *
from nltk.tokenize import PunktSentenceTokenizer
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import tree2conlltags
from nltk.corpus import treebank
from tkinter import Tk, Text, BOTH, W, N, E, S
import numpy as np
from IPython.display import Image

#import spacy
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
#create nlp
#NLP packages
from textblob import TextBlob
window = Tk()
window.title("NLP Tool V0.0.2")
window.resizable(height = None, width = None)

#window.attributes("-fullscreen", TRUE)
#create a general menu
# create a toplevel menu


menubar = Menu(window)
file = Menu(menubar, tearoff=0)#create file menu
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")
file.add_separator()
file.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=file)#add menu file with label
#********** edit menu
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select All")
menubar.add_cascade(label="Edit", menu=edit)
config = Menu(menubar, tearoff=0)
config.add_checkbutton(label="nltk")
config.add_checkbutton(label="spacy")
config.add_checkbutton(label="elastic search")


menubar.add_cascade(label="Config", menu=config)
# display the menu
window.config(menu=menubar)
#tab layout

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

#add tab to botebook
tab_control.add(tab1,text="NLP Tool")
tab_control.add(tab2,text="File Processer")
tab_control.add(tab3,text="About")
tab_control.pack(expand=1, fill='both')

#tab for nlp tool
label1 = Label(tab1, text="NLP Made Simple", padx=5,pady=5)
label1.grid(row=0,column=0)
label2 = Label(tab2, text="File Processing", padx=5,pady=5)
label2.grid(row=0,column=0)
label3 = Label(tab3, text="About", padx=5,pady=5)
label3.grid(row=0,column=0)

#functions for nlptool


#get tokens
def get_tokens(aText, aTabDisplay, use_ner):
    #messagebox.showinfo("Button label", text.get());
    raw_text = str(aText.get())
    new_text = TextBlob(raw_text)
    final_text = new_text.words
    result = format(final_text)#'\nTokens: {}'.format(final_text)
    if use_ner:
        return result
    else:
        aTabDisplay.insert(tk.END, result)


def get_pos_tags(aText, aTabDisplay, use_ner):
    raw_text = str(aText.get())
    new_text = TextBlob(raw_text)
    final_text = new_text.tags
    result = format(final_text)
    # Inserting into display   *****not recommended
    if use_ner:
        return result
    else:
        aTabDisplay.insert(tk.END, result)


#get sentiments
def get_sentiments(aText, aTabDisplay, use_ner):
    raw_text = str(aText.get())
    new_text = TextBlob(raw_text)
    final_text = new_text.sentiment
    result = '\nSubjectivity: {}, Polarity{}'.format(new_text.sentiment.subjectivity, new_text.sentiment.polarity)
    # Inserting into display   *****not recommended
    if use_ner:
        return result
    else:
        aTabDisplay.insert(tk.END, result)


#get entities, needs previous

def get_entities(aText, aTabDisplay, aList):
    aVar = aList.__getitem__(0)
    if aVar.get():#getting a token
        sentence = aText.get()
        word = nltk.word_tokenize(sentence)
        print(word)
        aTabDisplay.insert(tk.END, word)
    aVar = aList.__getitem__(1)
    if aVar.get():  # getting pos
        pos_tag = nltk.pos_tag(word)
        print(pos_tag)
        aTabDisplay.insert(tk.END, pos_tag)
    aVar = aList.__getitem__(3)
    if aVar.get():  # getting pos
        chunk = nltk.ne_chunk(pos_tag)
        print(chunk)
        aTabDisplay.insert(tk.END, chunk)
    aVar = aList.__getitem__(4)
    if aVar.get():
        chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
        chunkParser = nltk.RegexpParser(chunkGram)
        chunked = chunkParser.parse(pos_tag)
        chunked.draw()
        #nltk.draw.tree.TreeView(chunk)._cframe.print_to_file('output.ps')
        #os.system('convert output.ps output.png')
        #Image(filename='output.png')

        # Inserting into display   *****not recommended
    #tab1_display.insert(tk.END, result)

#cleaning text screen in tab1

def reset_entry_text():
    entry1.delete(0, END)

def clear_display_result():
    tab1_display.delete('1.0',END)


#main nlp tab 1
l1 = Label(tab1,text="Enter Text to Analysis")
l1.grid(row=1,column=0)


raw_entry = StringVar()#reading text
entry1 = Entry(tab1,textvariable=raw_entry,width=50)
entry1.grid(row=1,column=1)#get width of main, and adjust according to size, that would be more interesting


#display screen for results

tab1_display = ScrolledText(tab1, height=10)
tab1_display.grid(row=7, column=0, columnspan = 3, padx = 5, pady=5)

#buttons
#button1 = Button(tab1, text='Tokenize',width=12,bg='#03A9F4', fg='#FFF', command=get_tokens)
button1 = Button(tab1, text="Tokenizer", width=12, bg='#03A9F4',fg='#FFF',
                 command=lambda: get_tokens(entry1, tab1_display, False))
button1.grid(row=2,column=0, padx=10, pady=10)

button2 = Button(tab1, text='POS Tagger',width=12,bg='#03A9F4', fg='#FFF',
                 command=lambda: get_pos_tags(entry1, tab1_display, False))
button2.grid(row=2,column=1, padx=10, pady=10)

button3 = Button(tab1, text='Sentiment',width=12,bg='#03A9F4', fg='#FFF',
                 command = lambda : get_sentiments(entry1, tab1_display, False))
button3.grid(row=2,column=2, padx=10, pady=10)

button4 = Button(tab1, text='Entities',width=12,bg='#03A9F4', fg='#FFF', command = lambda :get_entities(entry1, tab1_display, True))
button4.grid(row=3,column=0, padx=10, pady=10)

button5 = Button(tab1, text='Reset',width=12,bg='#03A9F4', fg='#FFF', command=reset_entry_text)
button5.grid(row=3,column=1, padx=10, pady=10)

button6 = Button(tab1, text='Clear Result',width=12,bg='#03A9F4', fg='#FFF', command=clear_display_result)
button6.grid(row=3,column=2, padx=10, pady=10)

#frame for checkbutton
#iframe1 = Frame(tab1, width=100, height=110)

#iframe1.grid(row=8,column=0, padx=10, pady=10)
#frame for the buttons
# Tab 1
Pipeline = ttk.LabelFrame(tab1, text=' Pipeline ')
Pipeline.grid(column=4, row=0, columnspan=4, rowspan=6, padx=8, pady=4, sticky='nsew')
tk.Grid.rowconfigure(Pipeline, 0, weight=1)
tk.Grid.columnconfigure(Pipeline, 0, weight=1)
ttk.Label(Pipeline).grid(column=4, row=0)

#check button for pipeline

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()


checkbutton1 =Checkbutton(Pipeline, text = "Tokenizer                         ", variable = CheckVar1,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 20)
checkbutton1.grid(row=0,column=4, sticky= W)

checkbutton2 =Checkbutton(Pipeline, text = "Part of Speech (POS) Tagger", variable = CheckVar2,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 20)
checkbutton2.grid(row=1,column=4, padx=10, pady=10)

checkbutton3 =Checkbutton(Pipeline, text = "Sentiment Analisys               ", variable = CheckVar3,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 20)
checkbutton3.grid(row=2,column=4, padx=10, pady=10)

checkbutton4 =Checkbutton(Pipeline, text = "Name Entity Recognition    ", variable = CheckVar4,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 20)
checkbutton4.grid(row=3,column=4, padx=10, pady=10)

checkbutton5 =Checkbutton(Pipeline, text = "Treebank Graph                    ", variable = CheckVar5,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 20)
checkbutton5.grid(row=4,column=4, padx=10, pady=10)


checkbuttons_list = [CheckVar1, CheckVar2,CheckVar3, CheckVar4, CheckVar5]

button7 = Button(Pipeline, text="Process Pipeline", width=12, bg='#03A9F4',fg='#FFF',
                 command=lambda: get_entities(entry1, tab1_display, checkbuttons_list))
button7.grid(row=5,column=4, padx=10, pady=10)



#file reading and processing in tab 2
#function for opening files
def openfiles():
    file1 = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("text files", "*.jpg"), ("all files", "*")))
    read_text = open(file1).read()
    displayed_file.insert(tk.END, read_text)

#function for tokenizer

def get_file_tokens():
    raw_text = displayed_file.get('1.0',tk.END)
    new_text = TextBlob(raw_text)
    final_text = new_text.words
    result = '\nTokens: {}'.format(final_text)
    # Inserting into display   *****not recommended
    tab2_display_text.insert(tk.END, result)

#function for pos tagging

def get_file_pos_tags():
    raw_text = displayed_file.get('1.0',tk.END)
    new_text = TextBlob(raw_text)
    final_text = new_text.tags
    result = '\nPOS of Speech : {}'.format(final_text)
    # Inserting into display   *****not recommended
    tab2_display_text.insert(tk.END, result)

#function get_file_sentiments()
def get_file_sentiments():
    raw_text = displayed_file.get('1.0',tk.END)
    new_text = TextBlob(raw_text)
    final_text = new_text.sentiment
    result = '\nSubjectivity: {}, Polarity{}'.format(new_text.sentiment.subjectivity, new_text.sentiment.polarity)
    # Inserting into display   *****not recommended
    tab2_display_text.insert(tk.END, result)

# function for getting file entities

def get_file_entities():
    raw_text = displayed_file.get('1.0',tk.END)
    pass

# function for nlp processing

def nlp_file():
    raw_text = displayed_file.get('1.0',tk.END)
    pass

#cleaning text screen in tab1

def clear_text_file():
    displayed_file.delete('1.0', END)

def clear_result():
    tab2_display_text.delete('1.0',END)


l1 = Label(tab2, text = 'Open File to Process', padx=5, pady=5)
l1.grid(column=1, row=1)

displayed_file = ScrolledText(tab2, height= 7)
displayed_file.grid(row=2,column=0,columnspan=3,padx=5, pady=5)

#buttons for second tab

b0 = Button(tab2, text='Open File', width=12, bg='#03A9F4', fg = '#FFF', command=openfiles)
b0.grid(row=3, column=0, padx=10, pady = 10)

b1 = Button(tab2, text='Reset', width=12, bg='#b9f6ca', fg = '#FFF', command=clear_text_file)
b1.grid(row=3, column=1, padx=10, pady = 10)

b1a = Button(tab2, text='NLP', width=12, bg='#03A9F4', fg = '#FFF', command=nlp_file)
b1a.grid(row=3, column=2, padx=10, pady = 10)

b2 = Button(tab2, text='Tokenize', width=12, bg='#03A9F4', fg = '#FFF', command=get_file_tokens)
b2.grid(row=4, column=0, padx=10, pady = 10)

b3 = Button(tab2, text='POS Tags', width=12, bg='#bb86fc', fg = '#FFF', command=get_file_pos_tags)
b3.grid(row=4, column=1, padx=10, pady = 10)

b4 = Button(tab2, text='Sentiments', width=12, bg='#f44336', fg = '#FFF', command=get_file_sentiments)
b4.grid(row=4, column=2, padx=10, pady = 10)

b5 = Button(tab2, text='Entities', width=12, bg='#80d8ff', fg = '#FFF', command=get_file_entities)
b5.grid(row=5, column=0, padx=10, pady = 10)

b6 = Button(tab2, text='Clear Result', width=12, bg='#bb86fc', fg = '#FFF', command=clear_result)
b6.grid(row=5, column=1, padx=10, pady = 10)

b7 = Button(tab2, text='Close', width=12, command=window.destroy)
b7.grid(row=5, column=2, padx=10, pady = 10)

#setup display screen

tab2_display_text = ScrolledText(tab2, height = 7)
tab2_display_text.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

#about tab

about_label = Label(tab3, text="NLPText, V0.0.2 \n Luis Ramos @luisramos1977", padx=5, pady=5)
about_label.grid(column=0, row=1)

#creating the class with all parameter, a class button wit nltk specific functions



#test
#**********END***********
window.mainloop()



