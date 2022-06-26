"""
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.
"""

METERS_IN_ACRE = 4046.86


def area_of_a_field():
    width = float(input("Enter the width of the field: "))
    length = float(input("Enter the length of the field: "))
    area_in_meters = width * length
    area_in_acres = METERS_IN_ACRE / area_in_meters
    print(f"The area of a field is {area_in_acres:.2f} acres")
