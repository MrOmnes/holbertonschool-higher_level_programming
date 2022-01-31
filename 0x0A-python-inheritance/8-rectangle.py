#!/usr/bin/python3
"""8-base_geometry.py:
	Set size of a rectangle
"""


class BaseGeometry:
	"""Empty Class that raise an exception and verify and integer"""
	def area(self):
		"""Raise an exception"""
		raise Exception("area() is not implemented")

	def integer_validator(self, name, value):
		"""Verify an integer"""
		if type(value) is not int:
			raise TypeError(name + " must be an integer")
		if value <= 0:
			raise ValueError(name + " must be greater than 0")
		return value

class Rectangle(BaseGeometry):
	"""Set the size of a rectangle"""
	def __init__(self, width, height):
		"""Init the rectangle"""
		self.__width = BaseGeometry.integer_validator(self, "width", width)
		self.__height = BaseGeometry.integer_validator(self, "height", height)
