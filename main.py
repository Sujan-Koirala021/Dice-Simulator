from tkinter import *

import random

# Generate Random number from 1 to 6

def generateNumber():
    return random.randint(1, 6)


def rollDiceMechanism():
    num = generateNumber()
    print(num)


root = Tk()
num = generateNumber()
print(num)

rollDice = Button(root, text="Roll Dice", command=rollDiceMechanism)
rollDice.pack()

root.mainloop()
