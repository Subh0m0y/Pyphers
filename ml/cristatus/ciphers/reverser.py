"""
This python script basically takes a string and reverses it.

This python script can be used as a command line script as well as a separate
module.
"""
import sys


def reverse(text):
    """
    This function takes a string and reverses it, so as to somewhat obfuscate
     it.

    :param text: The unencrypted text message to be reversed.
    """
    return text[::-1]


if __name__ == '__main__':
    argument_count = len(sys.argv)

    message = ''
    if argument_count == 1:  # i.e. the program name only
        message = input('Please enter the text to be encrypted : ')
    elif argument_count == 2:
        message = sys.argv[1]
    else:
        print('Incorrect number of arguments : {}\n'.format(argument_count))
        print('Usage: python3 reverseCipher.py [unencrypted string]')
        exit(2)  # '2' stands for command-line syntax errors in unix

    print(reverse(message))
