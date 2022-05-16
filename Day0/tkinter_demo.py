import tkinter as t


win = t.Tk()
win.title("CRUD File")
win.minsize(600,300)
win.mainloop()

origin_file_label = t.Label(text="File Origin")
dest_file_label  = t.Label(text="File Destination")
origin_file_label.pack()
dest_file_label.pack()
