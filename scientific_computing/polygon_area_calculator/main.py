import shape_calculator
from unittest import main

rect = shape_calculator.Rectangle(10, 5)
print(rect)
print(f"Rect area: {rect.get_area()}")
rect.set_width(3)
print(rect)
print(f"Rect perimeter: {rect.get_perimeter()}")

sq = shape_calculator.Square(9)
print(sq)
print(f"Square area: {sq.get_area()}")
sq.set_side(4)
print(sq)
print(f"Square diagonal: {sq.get_diagonal()}")

rect.set_height(8)
rect.set_width(16)
print('\n' + rect.get_picture())
print(sq.get_picture())
print(f"{sq} fit {rect.get_amount_inside(sq)} times in {rect}")

# run unit tests automatically
main(module='test_module', exit=False)