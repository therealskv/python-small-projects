"""Simple Substitution Cipher, by Al Sweigart al@inventwithpython.com
A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.
More info at: https://en.wikipedia.org/wiki/Substitution_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, cryptography, math"""

import random

try:
    import pyperclip
except ImportError:
    pass

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('''A simple substitution cipher has a one-to-one translation for each symbol in the plaintext and each symbol in the ciphertext''')

    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt'
            break
        print('Enter either "encrypt" or "e" or "decrypt" or "d".')
    
    # let the user specify the key to use:
    while True:
        print('Enter the key to use.')
        if myMode == 'encrypt':
            print('Or enter RANDOM to have the key generated for you.')
        response = input('> ').upper()
        if response == 'RANDOM':
            myKey = generateRandomKey()
            print('The key is {}. KEEP THIS SECRET!'.format(myKey))
            break
        else:
            if checkKey(response):
                myKey = response
                break
    
    # let the user specify the message to encrypt/decrypt:
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')

    # perform the encryption/decryption:
    if myMode == 'encrypt':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = decryptMessage(myMessage, myKey)
    
    # display the encrypted/decrypted string to the screen:
    print('The %sed message is:' % (myMode))
    print(translated)

    # copy to clipboard:
    try:
        pyperclip.copy(translated)
        print('This message has been copied to the clipboard.')
    except:
        pass
    
def checkKey(key):
    """Returns True if key is valid, False otherwise."""
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        print('The key must contain all the letters of the alphabet.')
        return False
    return True

def encryptMessage(message, key):
    """Returns a string representing the encrypted message."""
    return translateMessage(message, key, 'encrypt')

def decryptMessage(message, key):
    """Returns a string representing the decrypted message."""
    return translateMessage(message, key, 'decrypt')

def translateMessage(message, key, mode):
    """Encrypt or decrypt the message using the key."""
    translated = '' # stores the encrypted/decrypted message string
    
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # for decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA
    
    # loop through each symbol in the message:
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it:
            translated += symbol
    
    return translated

def generateRandomKey():
    """Generate and return a random encryption key."""
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

# If simplechipher.py is run (instead of imported as a module) call
# the main() function:
if __name__ == '__main__':
    main()