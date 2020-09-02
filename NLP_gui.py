import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import *



#import spacy
import nltk


#create nlp

#nlp =spacy.load('en')#second option ----   import spacy nlp = spacy.load('en')

#NLP packages
from textblob import TextBlob


window = Tk()
window.title("NLP Tool V0.0.2")
window.geometry("700x400")

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
def get_tokens():
    raw_text = str(raw_entry.get())
    new_text = TextBlob(raw_text)
    final_text = new_text.words
    result = '\nTokens: {}'.format(final_text)
    #Inserting into display   *****not recommended
    tab1_display.insert(tk.END,result)

def get_pos_tags():
    raw_text = str(raw_entry.get())
    new_text = TextBlob(raw_text)
    final_text = new_text.tags
    result = '\nPOS of Speech : {}'.format(final_text)
    # Inserting into display   *****not recommended
    tab1_display.insert(tk.END, result)


#get sentiments
def get_sentiments():
    raw_text = str(raw_entry.get())
    new_text = TextBlob(raw_text)
    final_text = new_text.sentiment
    result = '\nSubjectivity: {}, Polarity{}'.format(new_text.sentiment.subjectivity, new_text.sentiment.polarity)
    # Inserting into display   *****not recommended
    tab1_display.insert(tk.END, result)


#get entities

#def get_entities():
 #   raw_text = str(raw_entry.get())
  #  docx = nlp(raw_text)
   # final_text = [(entity.text, entity.label) for entity in docx.ents ]
    #result = '\nEntities: {}'.format(final_text)
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



#buttons
button1 = Button(tab1, text='Tokenize',width=12,bg='#03A9F4', fg='#FFF', command=get_tokens(tab1_display))
button1.grid(row=4,column=0, padx=10, pady=10)

button2 = Button(tab1, text='POS Tagger',width=12,bg='#03A9F4', fg='#FFF', command=get_pos_tags)
button2.grid(row=4,column=1, padx=10, pady=10)

button3 = Button(tab1, text='Sentiment',width=12,bg='#03A9F4', fg='#FFF', command=get_sentiments)
button3.grid(row=4,column=2, padx=10, pady=10)

button4 = Button(tab1, text='Entities',width=12,bg='#03A9F4', fg='#FFF', command=get_tokens)
button4.grid(row=5,column=0, padx=10, pady=10)

button5 = Button(tab1, text='Reset',width=12,bg='#03A9F4', fg='#FFF', command=reset_entry_text)
button5.grid(row=5,column=1, padx=10, pady=10)

button6 = Button(tab1, text='Clear Result',width=12,bg='#03A9F4', fg='#FFF', command=clear_display_result)
button6.grid(row=5,column=2, padx=10, pady=10)

#display screen for results

tab1_display = ScrolledText(tab1, height=10)
tab1_display.grid(row=7, column=0, columnspan = 3, padx = 5, pady=5)

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



