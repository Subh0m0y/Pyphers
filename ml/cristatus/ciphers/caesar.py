"""
This python file contains the "shift()" method to encrypt as well as decrypt
strings.

Help on command line arguments:
1. Use without any of those to enter an interactive mode.
2. Pass only the plaintext to encrypt using default settings (shift of 47
with alphabet of all printable ascii characters).
3. Pass the shift amount (positive to encrypt, negative to decrypt) and one
of "lower", "upper" or "all" to choose the alphabet.

Usage:

"""
import string
import sys


def shift(message, amount=47, alphabet=string.printable):
    """
    This method takes a string and shifts it by the specified amount. A
    positive amount shifts the characters up, while a negative amount shifts
    the characters down.

    :param message:     The message to be encrypted.
    :param amount:      The amount to shift the message by. (Default is 47)
    :param alphabet:    The alphabet for determining the result of a shift.
                        (Default is all printable characters)
    :return:
    """
    # This handles all the "case issues"
    if alphabet == string.ascii_lowercase:
        message = str.lower(message)
    elif alphabet == string.ascii_uppercase:
        message = str.upper(message)
    shifted_alphabet = alphabet[amount:] + alphabet[:amount]
    table = str.maketrans(alphabet, shifted_alphabet)
    return message.translate(table)


if __name__ == '__main__':
    argument_count = len(sys.argv)
    text = ''
    offset = 47
    if argument_count == 1:
        # The script is being used independently, so display menus and stuff
        print('\n\n'
              '+--------------------------------------+\n'
              '|------------- caesar.py --------------|\n'
              '+--------------------------------------+\n\n')
        text = input('Please input the text to be encrypted : ')
        offset = int(input('Please enter the shift amount (negative to '
                           'decrypt) : '))
        print('The alphabet sets :\n'
              '1. Lowercase ascii\n'
              '2. Uppercase ascii\n')
        choice = input(
            'Please enter the choice number, or anything else to choose '
            'default alphabet (all printable ascii characters): ')
        print('The encrypted text is : ')
        if str.isnumeric(choice):
            number = int(choice)
            if number == 1:
                print(shift(text, offset, string.ascii_lowercase))
            elif number == 2:
                print(shift(text, offset, string.ascii_uppercase))
        else:
            print(shift(text, offset))
    elif argument_count == 2:
        # This and the next mode must be as silent as possible.
        text = sys.argv[1]
        print(shift(text))
    elif argument_count == 4:
        text = sys.argv[1]
        offset = int(sys.argv[2])
        universe = sys.argv[3]
        if universe == 'lower':
            print(shift(text, offset, string.ascii_lowercase))
        elif universe == 'upper':
            print(shift(text, offset, string.ascii_uppercase))
        elif universe == 'all':
            print(shift(text, offset, string.printable))
        else:
            print('Invalid choice of alphabet : {}'.format(universe))
            exit(1)
    else:
        print('Incorrect argument count : {}'.format(argument_count))
        print('Usage:')
        print('$ python3 caesar.py')
        print('\nOR\n')
        print('$ python3 caesar.py [text]')
        print('\nOR\n')
        print('$ python3 caesar.py [text] [shift] [alphabet]')
        exit(2)
