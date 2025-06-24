from tkinter import *

def someth(event):
    print("Pressed "+ str(event.num) +" at "+ str(event.x)+"," + str(event.y))

window = Tk()

window.bind("<Button-1>",someth)
window.bind("<ButtonRelease-2>",someth)

window.mainloop()