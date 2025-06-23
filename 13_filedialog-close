from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                         ("HTML file", ".html"),
                                         ("Python file", ".py")
                                    ])
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()

window = Tk()

text = Text(window)
text.pack()

button = Button(window,text="Save", command=saveFile)
button.pack()

window.mainloop()