#!/usr/bin/python3
""" This method contains the singly linked list and node class """


class Node:
    """ This is the class of a node of a singly linked list
    Args:
        Data (int): Data of the node
        Value (int): new data to be set on the node
    """
    def __init__(self, data, next_node=None):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value or type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ This is the class of a singly linked list
    Args:
        head (Node): first node of the linked list
        value (int): new value of new node
    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        liststr = ""
        if not self.__head:
            return ""
        temp = self.__head
        while temp:
            liststr = liststr + str(temp.__data)
            temp = temp.__next_node
            if temp:
                liststr = liststr + '\n'
        return liststr

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.__head or value < self.__head.__data:
            self.__head = Node(value, self.__head)
        temp = self.__head
        while temp.__next_node and temp.__next_node.__data < value:
            temp = temp.__next_node
        temp.__next_node = Node(value, temp.__next_node)
