#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, len_width=0, len_height=0):
        """Initializes the rectangle"""
        self.len_width = len_width
        self.len_height = len_height

    @property
    def len_width(self):
        """getter for the private instance attribute width"""
        return self.__len_width

    @len_width.setter
    def len_width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__len_width = value

    @property
    def len_height(self):
        """getter for the private instance attribute height"""
        return self.__len_height

    @len_height.setter
    def len_height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__len_height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__len_width * self.__len_height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__len_width == 0 or self.__len_height == 0:
            return 0
        return (self.__len_width * 2) + (self.__len_height * 2)
