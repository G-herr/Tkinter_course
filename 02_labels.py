from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("500x500")

photo = ImageTk.PhotoImage(Image.open('C:\\Users\\gusta\\Downloads\\django_logo.png').resize((100,100)))
#photo = PhotoImage(file='C:\\Users\\gusta\\Downloads\\django_logo.png')


label = Label(window, 
              text="Hello World", # Displayed text
              font=('Arial',40,'bold'), # Font changing
              fg='black', # Text color
              bg="#7C4B18", # Background color
              relief=RAISED, # Margin style
              bd=10, # Margin size
              padx=50, # Space between margin and text
              pady=50,
              image=photo,
              compound = 'bottom')
label.pack()
#label.place(x=100,y=50)


window.mainloop()