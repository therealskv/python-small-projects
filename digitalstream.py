"""Digital Stream, by Al Sweigart al@inventwithpython.com
A screensaver in the style of The Matrix movie's visuals.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic, beginner, scrolling"""

import random, shutil, sys, time

MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAM_CHARS = ['0', '1']
DENSITY = 0.02
WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    #for each column, when the counter is 0, no stream is shown
    #otherwise, it acts as a counter for how many times a 1 or 0
    #should be displayed in that column
    columns = [0] * WIDTH
    while True:
        #counter for each column
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    #restart a stream on this column
                    columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
            #display an empty space or a 1/0 character
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print() #a new line at the end of the row of columns
        sys.stdout.flush()
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()