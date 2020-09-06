import tkinter as tk
from tkinter import *
#from tkinter.ttk import *

def set_Img_size(e, aTextValue):
    e.delete(0, tk.END)  # cleaning the entry to use it
    e.insert(0, aTextValue)
    return e

# creating main tkinter window/toplevel
master = tk.Tk()


# this wil create two labels widget
l1 = tk.Label(master, text = "Height:")
l2 = tk.Label(master, text = "Width:")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row=0, column=0, sticky=tk.W, pady=2)
l2.grid(row=1, column=0, sticky=tk.W, pady=2)


#variables for text entry

entryText1 = tk.StringVar()#what is StringVar?
entryText2 = tk.StringVar()

e1 = tk.Entry( master, textvariable=entryText1 )#assign the entry text to entry
e2 = tk.Entry( master, textvariable=entryText2 )#assign the entry text to entry


# this will arrange entry widgets

e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)

# checkbutton widget
c1 = tk.Checkbutton(master, text = "Preserve")
c1.grid(row = 2, column = 0, sticky = tk.W, columnspan = 2)

# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file = r"C:\Users\255G74\Desktop\docramos\mifoto2.png")
img1 = img.subsample(2, 2)

#get height and width of image

img_high = img1.height()
img_width = img1.width()

#setting height and witdh in entry


## settup function
e1 = set_Img_size(e1,img_high)
e2 = set_Img_size(e2,img_high)

#


# setting image with the help of label
tk.Label(master, image = img1).grid(row = 0, column = 2,
       columnspan = 2, rowspan = 2, padx = 5, pady = 5)

# button widget
b1 = tk.Button(master, text = "Zoom in")
b2 = tk.Button(master, text = "Zoom out")

# arranging button widgets
b1.grid(row = 2, column = 2, sticky = E)
b2.grid(row = 2, column = 3, sticky = E)



master.mainloop()
