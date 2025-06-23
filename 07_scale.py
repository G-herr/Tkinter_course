from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path

def submit():
    print("The temperature is "+ str(scale.get())+"°C")

window = Tk()

fire_path = Path("Images") / "fire.png"
fireImage = ImageTk.PhotoImage(Image.open(fire_path).resize((50,50)))
hotLabel = Label(image=fireImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              tickinterval=5,
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg="#000000"

              )
scale.pack()

snowflake_path = Path("Images") / "snowflake.png"
snowflakeImage = ImageTk.PhotoImage(Image.open(snowflake_path).resize((50,50)))
coldLabel = Label(image=snowflakeImage)
coldLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()