def bottle_deposits_refund():
    small_bottles = int(input("Enter the number of small bottles: "))
    big_bottles = int(input("Enter the number of big bottles: "))
    SMALL_BOTTLES_REFUND = 0.1
    BIG_BOTTLES_REFUND = 0.25
    refund = (big_bottles * BIG_BOTTLES_REFUND) + (small_bottles * SMALL_BOTTLES_REFUND)
    print(f"The refund is ${refund:.2f}")
