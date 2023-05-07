class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.__data = data
        self.__next = next_node
        self.__prev = prev_node

    def get_data(self):
        return self.__data

    def set__data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node

    def get_prev(self):
        return self.__prev

    def set_prev(self, prev_node):
        self.__prev = prev_node

    def __str__(self):
        return f'{self.__data}'

    def __repr__(self):
        return f'Node(data={self.__data}, next={self.__next}, prev={self.__prev})'