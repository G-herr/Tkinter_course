from tkinter import *

window = Tk()

titlelabel = Label(window, text="Enter your info", font=("Arial",15)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First name: ").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last name: ").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window,text="Email: ").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

window.mainloop()