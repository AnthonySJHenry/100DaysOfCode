from functools import partial
from tkinter import *
import os

#Just changes the header to whatever is in the textbox

def change(num):
    if (num == 1):
        header.config(text=header_textbox.get())
    else:
        win.title(header_textbox.get())

win = Tk()
win.title("First GUI(Demo)")
win.minsize(height=100,width=300)
win.config(padx=15)

header = Label(text="header", font=("Arial", 20, "bold"))
header.grid(row=0,column=1, sticky='')

header_textbox = Entry()
header_textbox.grid(row=1,column=1)

#Change header using partial
change_header_button = Button(text="Change Header", command=partial(change, 1))
change_header_button.grid(row=4,column=0, rowspan=2)

#Change title using lambda
change_title_button = Button(text='Change Title', command=lambda: change(2))
change_title_button.grid(row=4,column=2, rowspan=2)
win.mainloop()