"""
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.
"""


def bottle_deposits_refund():
    small_bottles = int(input("Enter the number of small bottles: "))
    big_bottles = int(input("Enter the number of big bottles: "))
    SMALL_BOTTLES_REFUND = 0.1
    BIG_BOTTLES_REFUND = 0.25
    refund = (big_bottles * BIG_BOTTLES_REFUND) + (small_bottles * SMALL_BOTTLES_REFUND)
    print(f"The refund is ${refund:.2f}")
