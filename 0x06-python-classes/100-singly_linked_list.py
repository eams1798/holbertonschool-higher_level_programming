#!/usr/bin/python3
"""In this module we define two classes to construct a Singly Linked List"""


class Node:
    """The class defines a Node for a Singly Linked List"""
    def __init__(self, data, next_node=None):
        """Initializes a object for a Node of a Singly Linked List

        Args:
            data (int): a piece of data of the node
            next_node (Node): a reference to the next node
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is None or type(next_node) is Node:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """obj:`int`: returns o changes the value of the attribute `data`"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """obj:`Node`: returns o changes the value of the attribute `Node`"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """In this class, an object will store all the given nodes"""
    global print

    def __init__(self):
        """Initializes a Singly Linked List
        Args:
            head (class Node): The main node of a singly linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """Insert a node in a position of a linked list where its data
        is less than next node's

        Return:
            Nothing
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        else:
            aux = self.__head
            if new.data <= aux.data:
                new.next_node = aux
                self.__head = new
            else:
                while aux.next_node is not None:
                    if new.data <= aux.next_node.data:
                        break
                    aux = aux.next_node
                new.next_node = aux.next_node
                aux.next_node = new

    def print(self):
        """prints in stdout the values of all the nodes of
        a singly linked list"""
        p = __import__("sys").stdout.write
        itr = self.__head
        while itr is not None:
            p(str(itr.data) + "\n")
            itr = itr.next_node
