"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum = (n)(n + 1) / 2
"""


def sum_integers_to_n():
    n = int(input("Enter a positive integer: "))
    result = int((n * (n + 1)) / 2)
    print(result)
