from tkinter import *

count=0
def clickfun():
    global count 
    count += 1
    print(count)

window = Tk()

button = Button(window,
                text = 'Click me!', # Text in button
                command = clickfun, # What the button does
                font = ("calibri", 30), # Font
                fg="#0FB100", # Passive font colot
                bg="#D6D6D6", # Passive background color
                activeforeground='#0FB100', # Font color when active
                activebackground="#A3A3A3", # Backgroud color when active
                state=ACTIVE)
button.pack()

window.mainloop()