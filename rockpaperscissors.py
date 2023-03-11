"""Rock, Paper, Scissors (Always Win version)
By Al Sweigart al@inventwithpython.com
The classic hand game of luck, except you always win.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, game, humor"""

import time, sys, random

print('''
- Rock beats scissors.
- Paper beats rock.
- Scissors beats paper.
''')

wins = 0
losses = 0
ties = 0
computerMoves = {1: 'ROCK', 2: 'PAPER', 3: 'SCISSORS'}

while True:
    while True:
        print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))
        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
        playerMove = input(' >').upper()
        if playerMove == 'Q':
            print('Thanks for playing!')
            sys.exit()
        
        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        else:
            print('Type one of R, P, S or Q.')
    
    if playerMove == 'R':
        print('ROCK versus...')
        playerMove = 'ROCK'
    elif playerMove == 'P':
        print('PAPER versus...')
        playerMove = 'PAPER'
    elif playerMove == 'S':
        print('SCISSORS versus...')
        playerMove = 'SCISSORS'
    
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    randomNumber = random.randint(1, 3)
    computerMove = computerMoves[randomNumber]
    print(computerMove)
    time.sleep(0.5)

    if playerMove == computerMove:
        print('It\'s a tie!')
        ties += 1
    elif (playerMove == 'ROCK' and computerMove == 'SCISSORS') or (playerMove == 'PAPER' and computerMove == 'ROCK') or (playerMove == 'SCISSORS' and computerMove == 'PAPER'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1
    #break