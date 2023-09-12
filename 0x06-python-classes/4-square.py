#!/usr/bin/python3
""" This method contains a Square class """


class Square:
    """ This class contains methods and fields for Square

    Args:
        size (int): size of the Square
        value (int): new size of the Square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
