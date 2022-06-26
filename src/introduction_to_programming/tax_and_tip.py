"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
"""

TAX = 0.21
TIP = 0.18


def ticket() -> None:
    cost_of_meal = float(input("What is the cost of your meal? "))
    tax_amount = cost_of_meal * TAX
    tip_amount = (cost_of_meal + tax_amount) * TIP
    total_cost = cost_of_meal + tax_amount + tip_amount
    print("Tax and Trip")
    print(f"The total cost of your meal is ${cost_of_meal:.2f}")
    print(f"The tax is {tax_amount:.2f}")
    print(f"The tip is {tip_amount:.2f}")
    print(f"The total cost of your meal with tax is ${total_cost:.2f}")
