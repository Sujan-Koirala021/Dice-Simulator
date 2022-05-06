from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.geometry('300x300')

# Generate Random number from 1 to 6


def generateNumber():
    return random.randint(1, 6)


def rollDiceMechanism():
    num = generateNumber()
    print(num)
    diceLabel['image'] = dice1Img


# Image related stuff
diceImg = ImageTk.PhotoImage(Image.open('images/main.png'))
diceLabel = Label(image=diceImg)
diceLabel.pack(pady=20)

dice1Img = ImageTk.PhotoImage(Image.open('images/one.png'))


# Addition of Button to Roll Dice
rollDice = Button(root, text="Roll Dice", command=rollDiceMechanism)
rollDice.pack(pady=20)

root.mainloop()
