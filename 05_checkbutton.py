from tkinter import *

def display():
    if x.get() == 1:
        print("You agree")
    else:
        print("You don't agree")

window = Tk()

x = IntVar()
check_button = Checkbutton(window,
                           text = "I agree",
                           variable = x,
                           onvalue = 1,
                           offvalue = 0,
                           command = display,
                           font=('Times',20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10)
check_button.pack()

window.mainloop()