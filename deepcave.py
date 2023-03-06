"""Deep Cave, by Al Sweigart al@inventwithpython.com
An animation of a deep cave that goes forever into the earth.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, scrolling, artistic"""

import random, sys, time

WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()
    
    #adjust left width
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1
    elif diceRoll == 2:
        leftWidth = leftWidth + 1
    else:
        pass
    
    #adjust gap width
    diceRoll = random.randint(1, 6)
    if diceRoll == 1:
        gapWidth = gapWidth - 1
    elif diceRoll == 2:
        gapWidth = gapWidth + 1
    else:
        pass