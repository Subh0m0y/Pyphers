"""
This python file contains the "shift()" method to encrypt as well as decrypt
strings.

NOTE: Currently, this program only supports ASCII characters, NOT Unicode.
Be warned! Unicode support will be added if deemed necessary (which is highly
unlikely).

Help on command line arguments:
1. Use without any of those to enter an interactive mode.
2. Pass only the plaintext to encrypt using default settings (shift of 47
with alphabet of all printable ascii characters).
3. Pass the plaintext and the shift amount t
4. Pass the shift amount (positive to encrypt, negative to decrypt) and one
of "lower", "upper" or "all" to choose the alphabet.

Usage:
    caesar.py
    caesar.py <text>
    caesar.py <text> <shift>
    caesar.py <text> <shift> (lower | upper | all)
"""
import string
import sys

import docopt


def shift(message, amount=47, alphabet=string.printable):
    """
    This method takes a string and shifts it by the specified amount. A
    positive amount shifts the characters up, while a negative amount shifts
    the characters down.

    NOTE: If you are using either lowercase or uppercase alphabets,
    the message will be altered to allow proper encryption. If you want no
    alteration in the message and/or encrypt whitespace and punctuations,
    use the "all" alphabet.

    :param message:     The message to be encrypted.
    :param amount:      The amount to shift the message by. (Default is 47)
    :param alphabet:    The alphabet for determining the result of a shift.
                        (Default is all printable characters)
    :return:
    """
    # This handles all the "case issues"
    if alphabet == string.ascii_lowercase:
        message = message.lower()
    elif alphabet == string.ascii_uppercase:
        message = message.upper()
    correct = amount % len(alphabet)
    shifted_alphabet = alphabet[correct:] + alphabet[:correct]
    table = str.maketrans(alphabet, shifted_alphabet)
    return message.translate(table)


def main(args):
    text = args['<text>']
    if text is None:
        text, offset, universe = get_cli_args()
    else:
        offset = int(args.get('shift', '47'))
        universe = (
            'lower' if args['lower'] else
            'upper' if args['upper'] else
            'all'
        )
    if universe == 'lower':
        print(shift(text, offset, string.ascii_lowercase))
    elif universe == 'upper':
        print(shift(text, offset, string.ascii_uppercase))
    else:
        print(shift(text, offset, string.printable))


def get_cli_args():
    print('\n\n'
          '+--------------------------------------+\n'
          '|------------- caesar.py --------------|\n'
          '+--------------------------------------+\n\n')
    text = input('Please input the text to be encrypted : ')
    value = input('Please enter the shift amount (negative to decrypt) : ')
    while not value[0] == '-' and not value.isnumeric():
        value = input('Please enter the shift amount (negative to decrypt) : ')
    amount = int(value)
    print('The alphabet sets :\n'
          '1. Lowercase ascii\n'
          '2. Uppercase ascii\n')
    choice = input(
        'Please enter the choice number, or anything else to choose '
        'default alphabet (all printable ascii characters): ')
    print('The encrypted text is : ')
    universe = {'1': 'lower', '2': 'upper'}.get(choice, 'all')
    return text, amount, universe


if __name__ == '__main__':
    sys.exit(main(docopt.docopt(__doc__)))
