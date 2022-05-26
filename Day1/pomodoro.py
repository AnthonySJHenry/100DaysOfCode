from tkinter import *
BG_COLOR = "#F9EBC8"
#-------------------GUI--------------------#
win = Tk()
win.title('Pomodoro Timer')
win.config(bg=BG_COLOR)

timer_label = Label(text="Set Time", fg="black", bg = BG_COLOR, font=("Arial", 24))
timer_label.grid(row=1, column=2)

timer_entry = Entry()
timer_entry.grid(row=1, column=2)

canvas = Canvas(width=400, height=400, bg=BG_COLOR, highlightbackground=BG_COLOR)
clock_image = PhotoImage(file="Day1/clock256px.png")
canvas.create_image(200,200, image=clock_image)
canvas.create_text(200,250,text="00:00", fill="#006E7F", font=("Arial", 24, "bold"))
canvas.grid(row=2, column=2)

start_stop_button = Button(text='Start')
start_stop_button.grid(row=3,column=1)

reset_button = Button(text='Reset')
reset_button.grid(row=3, column=3)



win.mainloop()