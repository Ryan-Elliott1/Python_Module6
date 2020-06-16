"""
Program: function_parameter.py
Author: Ryan Elliott
Last date modified: 06/16/2020

This program prints the string multiplied by the number of times
Outputs message multiple times
"""


def multiply_string(message, n):
    """Returns a string from the message times n
    :param message, the users message
    :param n, number of times
    :returns message time n
    """
    return message * n


if __name__ == '__main__':
    print(multiply_string("Python", 4))
