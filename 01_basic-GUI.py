from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("First GUI program")

icon = PhotoImage(file="Images\\Logo.png")
window.iconphoto(True,icon)
window.config(background="#68A721")

window.mainloop()