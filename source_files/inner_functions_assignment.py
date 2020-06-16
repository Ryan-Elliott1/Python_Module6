"""
Program: inner_functions_assignment.py
Author: Ryan Elliott
Last date modified: 06/16/2020
This program uses a list and inner functions to calculate perimeter and area
Input list of measurements
Outputs the perimeter and area of measurements
"""


def measurements(measurement_list):
    """Returns
    :param measurement_list: list of measurements
    :returns perimeter and area of measurements
    """
    def area(a_list):
        if len(a_list) == 1:
            return a_list[0] * a_list[0]
        else:
            return a_list[0] * a_list[1]

    def perimeter(a_list):
        if len(a_list) == 1:
            return a_list[0] * 4
        else:
            return (a_list[0] * 2) + (a_list[1] * 2)

    output = "Perimeter = " + str(perimeter(measurement_list)) + " Area = " + str(area(measurement_list))
    return output


if __name__ == '__main__':
    print(measurements([3.5]))
