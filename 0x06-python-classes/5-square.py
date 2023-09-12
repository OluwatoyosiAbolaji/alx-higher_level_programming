#!/usr/bin/python3
""" This method contains a square class """


class Square:
    """ This contains all fields and methods of a square

    Args:
        size: size of square
        value: new size of the square

    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end='')
            print()
