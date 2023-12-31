#!/usr/bin/python3
""" This method contains a class called Square """


class Square:
    """ This class defines a square with a size

    Args:
        size (int): size of the square
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
