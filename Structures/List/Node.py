class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.__data = data
        self.__next = next_node
        self.__prev = prev_node

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
        self.__next = next_node

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def set_prev(self, prev_node):
        self.__prev = prev_node

    def __str__(self):
        return f'{self.__data}'

    def __repr__(self):
        return f'Node(data={self.__data}, next={self.__next}, prev={self.__prev})'