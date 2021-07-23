# Dice Rolling Simulator using Tkinter

import tkinter
from PIL import Image, ImageTk
import random

# top-level widget which represents the main window of an application

root = tkinter.Tk()
root.geometry('400x400')
root.title('Dice Rolling simulator')


# Adding label into the frame
l1 = tkinter.Label(root, text="")
l1.pack()

# adding label with different font and formatting
l2 = tkinter.Label(root, text="Welcome to Dice Roll Game!", fg="light green", bg="dark green", font = "Helvetica 16 bold italic")
l2.pack()

# images
dice = ['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png']

# simulating the dice with random numbers between
# 0 to 6 and generating image

DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
label1 = tkinter.Label(root, image=DiceImage)
label1.image = DiceImage

# packing a widget in the parent widget 
label1.pack( expand = True)

# function activated by button
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=DiceImage)
    # keep a reference
    label1.image = DiceImage
    
# adding button, and command will use rolling_dice function   
button = tkinter.Button(root, text='Roll the Dice', fg='blue',command=rolling_dice)

# pack a widget in the parent widget
button.pack( expand=True)

# call the mainloop of Tk
# keeps window open
root.mainloop()
