#!/usr/bin/python3
""" This module contains a class called my_square """

class Square:
    """ This class is for square """
    def __init__(self, size):
        """ This function is to initialize the size """
        self.__size = size
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
