from tkinter import *
from pathlib import Path

window = Tk()
window.geometry("500x500")
window.title("First GUI program")

image_path = Path("Images") / "Logo.png"
icon = PhotoImage(file=image_path)
window.iconphoto(True,icon)
window.config(background="#68A721")

window.mainloop()