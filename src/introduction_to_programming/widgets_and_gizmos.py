"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
"""

WIDGET_WEIGHT = 75
GIZMOS_WEIGHT = 112


def widgets_and_gizmos():
    widgets = int(input('Enter the number of widgets: '))
    gizmos = int(input('Enter the number of gizmos: '))
    total_weight = widgets * WIDGET_WEIGHT + gizmos * GIZMOS_WEIGHT
    print(f'The total weight of the order is {total_weight} grams.')
