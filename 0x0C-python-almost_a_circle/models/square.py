#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """Class that create a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init the square"""
        self.size = size
        self.__x = x
        self.__y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Definition of the square """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.__x, self.__y, self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        elif type(value) is int and value >= 0:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """ Update The Square """
        if len(args) == 0:
            for key, value, in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.__x = args[2]
        if len(args) > 3:
            self.__y = args[3]

    def to_dictionary(self):
        """ Return the dicitionnary of the square """
        return {'id': self.id, 'x': self.__x, 'size': self.size,
                'y': self.__y}

    def save_to_file(squares):
        """ Save to File """
        dicts = []

        for item in squares:
            dicts.append(item.to_dictionary())

        Base.save_to_file(Square, dicts)
