class Rectangle:

	def __init__(self, width, height):
		# initializes a Rectangle object with the specified width and height
		self.width = width
		self.height = height

	def set_width(self, width):
		# sets the width of the rectangle to the specified value
		self.width = width

	def set_height(self, height):
		# sets the height of the rectangle to the specified value
		self.height = height

	def get_area(self):
		# returns the area of the rectangle
		return self.width * self.height

	def get_perimeter(self):
		# returns the perimeter of the rectangle
		return 2 * (self.width + self.height)

	def get_diagonal(self):
		# returns the length of the diagonal of the rectangle
		return (self.width**2 + self.height**2)**0.5

	def get_picture(self):
		# returns a string representation of the rectangle using '*' characters
		if self.width > 50 or self.height > 50:
			return "Too big for picture."
		picture = '*' * self.width + '\n'
		picture *= self.height
		return picture

	def get_amount_inside(self, shape):
		# returns the number of times the specified shape can fit inside the rectangle
		width_fit = self.width // shape.width
		height_fit = self.height // shape.height
		return width_fit * height_fit

	def __str__(self):
		# returns a string representation of the rectangle
		return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

	def __init__(self, side):
		# initializes a Square object with the specified side length
		super().__init__(side, side)

	def set_side(self, side):
		# sets the side length of the square to the specified value
		self.set_width(side)

	def set_width(self, width):
		# sets the width of the square to the specified value
		super().set_width(width)
		super().set_height(width)

	def set_height(self, height):
		# sets the height of the square to the specified value
		super().set_width(height)
		super().set_height(height)

	def __str__(self):
		# returns a string representation of the square
		return f"Square(side={self.width})"