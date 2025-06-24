from tkinter import *

def someth(event):
    print("You pressed "+event.keysym)

window = Tk()

window.bind("<Key>",someth)

window.mainloop()