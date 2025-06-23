from tkinter import *
from PIL import Image, ImageTk

food = ["Pizza","Burger", "Hotdog"]

def order():
    choice = x.get()
    print(f"You ordered a {food[choice]}. Great choice!")
        

window = Tk()

pizzaImage = ImageTk.PhotoImage(Image.open('Images\\pizza.png').resize((50,50)))
burgerImage = ImageTk.PhotoImage(Image.open('Images\\burger.png').resize((50,50)))
hotdogImage = ImageTk.PhotoImage(Image.open('Images\\hotdog.png').resize((50,50)))
foodImages = [pizzaImage,burgerImage,hotdogImage]
x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text = food[index], # Text in radio buttons
                               variable = x, # 
                               value = index, # Assings each radiobutton a diferent value
                               padx = 25,
                               font = ('Impact',20),
                               image = foodImages[index],
                               compound='left',
                               command = order
                               )
    radio_button.pack(anchor=W)

window.mainloop()