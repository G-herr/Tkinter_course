from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Batang", 25),
            height=8,
            width=20,
            padx=20,
            pady=20)
text.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()