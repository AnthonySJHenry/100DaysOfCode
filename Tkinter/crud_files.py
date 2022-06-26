from tkinter import *
import os

#The plan was to make a GUI that could do crud work to files. This may take some time.


path = os.path.expanduser('~/Desktop')
dropdown_list = os.listdir(path)
win = Tk()
win.title("CRUD Files")
win.minsize(600,400)
test = StringVar()
test.set("100DaysDev")
#Origin File(Label and Textbox)
origin_file_label = Label(text="File Origin")
origin_file_textbox = Entry()
dropdown_menu = OptionMenu(win, test, *dropdown_list)
origin_file_label.pack()
origin_file_textbox.pack()
dropdown_menu.pack()

dest_file_label  = Label(text="File Destination")
dest_file_label.pack()

#Buttons
directory_button = Button

win.mainloop()