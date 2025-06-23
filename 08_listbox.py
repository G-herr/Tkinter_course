from tkinter import *

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    
    print("You have ordered: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
        
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window, 
                  bg = "#fffcb2",
                  font = ("Constantia",35),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Pasta")
listbox.insert(3,"Bread")
listbox.insert(4,"Soup")
listbox.insert(5,"Salad")
listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

addButton = Button(window, text="Add", command=add)
addButton.pack()

deleteButton = Button(window, text="Delete", command=delete)
deleteButton.pack()

submitButton = Button(window,text="Submit",command=submit)
submitButton.pack()

window.mainloop()