#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return(self.__data)

    @data.setter
    def data(self, value):
        self.__data = value

        if type(data) != int:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        self.__next_node = value

        #if:
        #raise TypeError(next_node must be a Node object)

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head == None:
            new_node.__next_node = self.__head
            self.__head = new_node
