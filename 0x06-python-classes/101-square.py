#!/usr/bin/python3
""" This method contains a class Square and a function not_tuple """


def not_tuple(position):
    """ This function checks if it is a tuple of two positive integers """
    if type(position) != tuple or len(position) != 2:
        return True
    elif type(position[0]) != int or position[0] < 0:
        return True
    elif type(position[1]) != int or position[1] < 0:
        return True
    else:
        return False


class Square:
    """ This class defines a Square

    Args:
        size (int): size/length of a square
        value (int): new size/length of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not_tuple(position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not_tuple(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        print("{}{}".format(' ' * self.position[0], '#' * size))

    def __str__(self):
        liststr = ""
        if self.size == 0:
            return liststr
        for i in range(self.position[1]):
            liststr = liststr + '\n'
        for j in range(self.size - 1):
            liststr = liststr + (self.position[0] * ' ')
            liststr = liststr + ('#' * self.size) + '\n'
        liststr = liststr + (self.position[0] * ' ') + ('#' * self.size)
        return liststr
