"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM__DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Enter q to quit at any point.

    Here are some clues:
    
    When I say:  That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagel        Digit is incorrect.
    Bagels       No digit is correct.
    
    '''.format(NUM__DIGITS))
    while True:
        secretNum = getSecretNum()
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM__DIGITS or not guess.isdecimal():
                print('Guess #{}: {}'.format(numGuesses, guess))
                x = input('> ')
                if x.lower() == 'q':
                    print('Bye! Thanks for playing!')
                    return
                guess += x

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                print('Congrats! Your guess {} is correct!'.format(guess))
                break
            elif numGuesses <= MAX_GUESSES:
                print('Your guess {} is incorrect!'.format(guess))
            elif numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}'.format(secretNum))
        
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            print('Bye!')
            break
    print('Bye! Thanks for playing!')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    return ''.join(numbers[:3])

def getClues(guess, secretNumber):
    if guess == secretNumber:
        return 'You got it!'
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            clues.append('Fermi!')
        elif guess[i] in secretNumber:
            clues.append('Pico')
        else:
            clues.append('Bagel')
    
    if 'Fermi' not in clues and 'Pico' not in clues:
        return 'Bagels'
    else:
        return ' '.join(clues)

if __name__ == '__main__':
    main()