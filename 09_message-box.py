from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="Info Message Box", message="You are awesome")
    #messagebox.showwarning(title="WARNING!", message="You have a VIRUS!!!")
    #messagebox.showerror(title="ERROR!", message="Something went worng :(")
    if messagebox.askokcancel(title="Ask ok cancel", message="Do you want it to buy it?"):
        messagebox.showinfo(title="Info Message Box", message="You bought it")
    else:
        messagebox.showerror(title="Missed out!", message="Someone else probably will buy it anyway")

window = Tk()

button = Button(window, command=click, text="Click me!")
button.pack()

window.mainloop()