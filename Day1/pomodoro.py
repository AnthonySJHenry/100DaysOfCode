from tkinter import *
BG_COLOR = "#F9EBC8"
#-------------------GUI--------------------#
win = Tk()
win.title('Pomodoro Timer')
win.config(bg=BG_COLOR, padx=50, pady=50)

timer_label = Label(text="Set Time", fg="black", bg = BG_COLOR, font=("Arial", 24))
timer_label.grid(row=0, column=1)

timer_entry_min = Entry(fg="black", bg="green")
timer_entry_min.grid(row=1, column=1)
timer_label = Label(text=":")
timer_entry_secs = Entry(fg="black", bg="green")
timer_entry_secs.grid(row=1, column=1)
set_button = Button(text='Set', highlightthickness=0)

canvas = Canvas(width=400, height=400, bg=BG_COLOR, highlightthickness=0)
clock_image = PhotoImage(file="Day1/clock256px.png")
canvas.create_image(200,200, image=clock_image)
canvas.create_text(200,250,text="00:00", fill="#006E7F", font=("Arial", 24, "bold"))
canvas.grid(row=2, column=1)

start_stop_button = Button(text='Start', highlightthickness=0)
start_stop_button.grid(row=3,column=0)

reset_button = Button(text='Reset', highlightthickness=0)
reset_button.grid(row=3, column=2)



win.mainloop()