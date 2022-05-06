# Dice Simulator

from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('Dice Simulator')
root.geometry('300x300')
root.resizable(False, False)    # Full screen mode disabled


# Returns pillow image object
def makeTkImage(fileSource):
    return ImageTk.PhotoImage(Image.open(fileSource))

# Returns Random number from 1 to 6


def generateNumber():
    return random.randint(1, 6)


def rollDiceMechanism():
    num = generateNumber()

    # Changing image attribute of label
    if num == 1:
        diceLabel['image'] = diceImg1
    elif num == 2:
        diceLabel['image'] = diceImg2
    elif num == 3:
        diceLabel['image'] = diceImg3
    elif num == 4:
        diceLabel['image'] = diceImg4
    elif num == 5:
        diceLabel['image'] = diceImg5
    else:
        diceLabel['image'] = diceImg6



# Image related stuff

# Default image initially
initDiceImg = makeTkImage('images/main.png')

# Dice faces images
diceImg1 = makeTkImage('images/one.png')
diceImg2 = makeTkImage('images/two.png')
diceImg3 = makeTkImage('images/three.png')
diceImg4 = makeTkImage('images/four.png')
diceImg5 = makeTkImage('images/five.png')
diceImg6 = makeTkImage('images/six.png')

# Display default image in label
diceLabel = Label(image=initDiceImg)
diceLabel.pack(pady=20)


# Button to Roll Dice
rollDice = Button(root, text="Roll Dice", command=rollDiceMechanism)
rollDice.pack(pady=20)

root.mainloop()
