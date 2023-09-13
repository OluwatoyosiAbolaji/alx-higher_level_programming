#!/usr/bin/python3
""" This method contains the class Square """


def not_tuple(value):
    """ This function is annoying asf """

    if type(value) != tuple:
        return False
    elif len(value) != 2:
        return False
    elif type(value[0]) != int or value[0] < 0:
        return False
    elif type(value[1]) != int or value[1] < 0:
        return False
    else:
        return True

class Square:
    """ COntains fields and methods for a class
    Args:
        size (int): size of a square
        position (tuple):
        value (int): new size of a square
    """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not not_tuple(position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
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
        if not not_tuple(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value


    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.position == 0:
            print()
            return
        for j in range(self.position[1]):
            print()
        for i in range(self.size):
            print("{}{}".format(' ' * self.position[0], "#" * self.size))
