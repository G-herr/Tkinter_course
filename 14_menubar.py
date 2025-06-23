from tkinter import *

def openFile():
    print("File has been opened!")

def saveFile():
    print("File has been saved!")

def copy():
    print("Text copied")

def cut():
    print("You cutted the text")

def paste():
    print("Pasted!")

window = Tk()

menuBar=Menu(window)
window.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

editMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()