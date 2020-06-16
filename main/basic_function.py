"""
Program: basic_function.py
Author: Ryan Elliott
Last date modified: 06/16/2020

This program takes the users input to calculate pay, throws an exception if input is bad
Input name, hourly pay and pay rate
Outputs the total pay
"""


def hourly_employee_input():
    """Prompts the user for name, hours worked and pay rate. outputs the total pay"""
    name = input("Please enter your name: ")
    try:
        hours_worked = int(input("Please enter your hours worked: "))
        pay_rate = float(input("Please enter your pay rate: "))
    except ValueError as err:
        print("ValueError encountered")
    else:
        total_pay = hours_worked * pay_rate
        print(name, "Hours worked:", hours_worked, "Pay rate:", pay_rate, "Total pay:", total_pay)


if __name__ == '__main__':
    hourly_employee_input()

