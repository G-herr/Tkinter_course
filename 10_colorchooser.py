from tkinter import *
from tkinter import colorchooser

def click():
    rgb,color = colorchooser.askcolor()
    print(color)
    window.config(bg=color)

window = Tk()
window.geometry('420x420')
button = Button(text='Click me!', command=click)
button.pack()

window.mainloop()