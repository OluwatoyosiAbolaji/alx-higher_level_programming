#!/usr/bin/python3
""" This method contains the class Square """


class Square:
    """ COntains fields and methods for a class
    Args:
        size (int): size of a square
        position (tuple): 
        value (int): new size of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not self.not_tuple(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def not_tuple(self, value):
        if type(value) != tuple:
            return False
        elif len(value) != 2:
            return False
        elif type(value[0]) != int:
            return False
        elif type(value[1]) != int:
            return False
        else:
            return True

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("{}{}".format(' ' * self.__position[0], "#" * self.__size))
my_square = Square(3, “Position”)
