"""Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, cryptography, math"""

#to install modul using python3.4+
#python3 -m pip install <module_name>
try:
    import pyperclip #copies text to the clipboard
except ImportError:
    pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d')

while True:
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue #keep asking until a valid key is entered

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print('Enter the message to {}'.format(mode))
message = input('> ')

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        
        #handle if num is large than length of SYMBOLS or less than zero
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        
        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol

print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass
