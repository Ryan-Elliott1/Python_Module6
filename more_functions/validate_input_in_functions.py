"""
Program: validate_input_in_functions.py
Author: Ryan Elliott
Last date modified: 06/16/2020
This program uses default values in a function and input validation and outputs the test name and score
Input the test name and optionally the test score and invalid message
Outputs the test name and score if correct values
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """Returns
    :param test_name: name of the test
    :param test_score: optional test score
    :param invalid_message: optional invalid message
    :returns test_name and test_score in a string
    """
    try:
        if test_score < 0 or test_score > 100:
            return invalid_message
        else:
            test_name_and_score = (test_name + ": " + str(test_score))
    except TypeError as err:
        raise TypeError
    else:
        return test_name_and_score


if __name__ == '__main__':
    try:
        print(score_input("math", "test"))
    except TypeError as err:
        print("TypeError encountered")
