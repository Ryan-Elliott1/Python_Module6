"""
Program: validate_input_in_functions.py
Author: Ryan Elliott
Last date modified: 06/16/2020


"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """Returns
    :param invalid_message:
    :param test_name:
    :param test_score:
    :returns message time n
    """
    test_name_and_score = (test_name + ": " + str(test_score))
    return test_name_and_score


if __name__ == '__main__':
    print(score_input("math"))
