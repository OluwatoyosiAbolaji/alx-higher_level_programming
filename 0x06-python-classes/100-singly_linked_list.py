#!/usr/bin/python3
""" This method contains the singly linked list and node class """


class Node:
    """ This is the class of a node of a singly linked list
    Args:
        Data (int): Data of the node
        Value (int): new data to be set on the node
    """
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
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
        if self.__head is None:
            return ""
        temp = self.__head
        while temp:
            liststr = liststr + str(temp.data)
            temp = temp.next_node
            if temp is not None:
                liststr = liststr + '\n'
        return liststr

    def sorted_insert(self, value):
        if self.__head is None or value < self.__head.data:
            self.__head = Node(value, self.__head)
            return
        temp = self.__head
        while temp.next_node is not None and temp.next_node.data < value:
            temp = temp.next_node
        temp.next_node = Node(value, temp.next_node)
