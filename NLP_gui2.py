from tkinter import Tk, BOTH, messagebox
from tkinter.ttk import Frame, Button
from tkinter import ttk
from tkinter import *
from textblob import TextBlob
import tkinter as tk
from tkinter.scrolledtext import *





class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent
        self.parent.title("Buttons")

        tab_control = ttk.Notebook(self.parent)
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab3 = ttk.Frame(tab_control)

        # add tab to botebook
        tab_control.add(tab1, text="NLP Tool")
        tab_control.add(tab2, text="File Processer")
        tab_control.add(tab3, text="About")
        tab_control.pack(expand=1, fill='both')

        # tab for nlp tool
        label1 = Label(tab1, text="NLP Made Simple", padx=5, pady=5)
        label1.grid(row=0, column=0)
        label2 = Label(tab2, text="File Processing", padx=5, pady=5)
        label2.grid(row=0, column=0)
        label3 = Label(tab3, text="About", padx=5, pady=5)
        label3.grid(row=0, column=0)

        raw_entry = StringVar()  # reading text
        entry1 = Entry(tab1, textvariable=raw_entry, width=50)
        entry1.grid(row=1, column=1)  # get width of main, and adjust according to size, that would be more interesting

        tab1_display = ScrolledText(tab1, height=10)
        tab1_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

        # main nlp tab 1
        l1 = Label(tab1, text="Enter Text to Analysis")
        l1.grid(row=1, column=0)

        #self.pack(fill=BOTH, expand=1)

        btn1 = Button(tab1, text="Button 1",
                      command=lambda: self.get_tokens(entry1, tab1_display))
        btn1.grid(row=4, column=0, padx=10, pady=10)

        btn2 = Button(self, text="Button 2",
                      command=lambda: self.onClick("Button 2"))
        #btn2.pack(padx=5, pady=5)

        btn2 = Button(self, text="Button 3",
                      command=lambda: self.onClick("Button 3"))
        #btn2.pack(padx=5, pady=5)


    def get_tokens(self, aText, aTabDisplay):
        #messagebox.showinfo("Button label", text.get());
        raw_text = str(aText.get())
        new_text = TextBlob(raw_text)
        final_text = new_text.words
        result = '\nTokens: {}'.format(final_text)
        aTabDisplay.insert(tk.END, result)



def main():
    window = Tk()
    window.title("NLP Tool V0.0.2")
    window.geometry("700x400")
    # tab layout
    app = Example(window)
    window.mainloop()


if __name__ == '__main__':
    main()