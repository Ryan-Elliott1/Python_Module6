"""
Program: function_return_value.py
Author: Ryan Elliott
Last date modified: 06/16/2020

This program takes the users input to calculate pay, throws an exception if input is bad
Input name, hourly pay and pay rate
Outputs the weekly pay
"""


def hourly_employee_input():
    """ Prompts the user for name, hours worked and pay rate. returns name and weekly pay
    :returns the name and weekly pay rate
    """

    name = input("Please enter your name: ")
    try:
        hours_worked = int(input("Please enter your hours worked: "))
        pay_rate = float(input("Please enter your pay rate: "))
    except ValueError as err:
        print("ValueError encountered")
    else:
        name_weekly_pay = name, weekly_pay(hours_worked, pay_rate)
        return name_weekly_pay


def weekly_pay(hours_worked, hourly_pay_rate):
    """Calculates weekly pay from hours worked and pay rate
    :param hours_worked, hours worked
    :param hourly_pay_rate, hourly pay rate
    :returns the weekly pay rate
    """
    return hours_worked * hourly_pay_rate


if __name__ == '__main__':
    print(hourly_employee_input())
