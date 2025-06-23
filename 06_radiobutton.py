from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path

food = ["Pizza","Burger", "Hotdog"]

def order():
    choice = x.get()
    print(f"You ordered a {food[choice]}. Great choice!")
        

window = Tk()

burger_path = Path("Images") / "burger.png"
pizza_path = Path("Images") / "pizza.png"
hotdog_path = Path("Images") / "hotdog.png"

pizzaImage = ImageTk.PhotoImage(Image.open(burger_path).resize((50,50)))
burgerImage = ImageTk.PhotoImage(Image.open(pizza_path).resize((50,50)))
hotdogImage = ImageTk.PhotoImage(Image.open(hotdog_path).resize((50,50)))
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