"""ROT13 Cipher, by Al Sweigart al@inventwithpython.com
The simplest shift cipher for encrypting and decrypting text.
More info at https://en.wikipedia.org/wiki/ROT13
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, cryptography"""

try:
    import pyperclip
except ImportError:
    pass

UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print()

while True:
    print('Enter a message to encrypt/decrypt (or QUIT):')
    message = input('> ')

    if message.upper() == 'QUIT':
        break

    translated = ''
    for character in message:
        if character.isupper():
            transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[transCharIndex]
        elif character.islower():
            transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[transCharIndex]
        else:
            translated += character
    
    print('The translated message is:')
    print(translated)
    print()

    try:
        pyperclip.copy(translated)
        print('(Copied to clipboard.)')
    except:
        pass