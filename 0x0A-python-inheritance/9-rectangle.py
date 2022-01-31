#!/usr/bin/python3
class BaseGeometry:
	def area(self):
		raise Exception("area() is not implemented")

	def integer_validator(self, name, value):
		if type(value) is not int:
			raise TypeError(name + " must be an integer")
		if value <= 0:
			raise ValueError(name + " must be greater than 0")
		return value

class Rectangle(BaseGeometry):
	def __init__(self, width, height):
		self.__width = BaseGeometry.integer_validator(self, "width", width)
		self.__height = BaseGeometry.integer_validator(self, "height", height)

	def area(self):
		return self.__width * self.__height

	def __str__(self):
		return ("[Rectangle] {}/{}".format(self.__width, self.__height))