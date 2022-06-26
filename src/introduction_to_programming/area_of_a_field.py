METERS_IN_ACRE = 4046.86


def area_of_a_field():
    width = float(input("Enter the width of the field: "))
    length = float(input("Enter the length of the field: "))
    area_in_meters = width * length
    area_in_acres = round(METERS_IN_ACRE / area_in_meters, 2)
    print(f"The area of a field is {area_in_acres} acres")
