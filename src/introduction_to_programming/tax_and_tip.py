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
