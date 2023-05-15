from Structures.List.List import List


class TreeNode:
    def __init__(self, key, data):
        self.__key = key
        self.__data = data
        self.__children = List()

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_key(self):
        return self.__key

    def set_key(self, key):
        self.__key = key

    def get_child(self, i):
        if self.__children.get(i) is not None:
            return self.__children.get(i).get_data()
        return None

    def get_children(self):
        return self.__children

    def set_children(self, children: List):
        self.__children = children

    def add_child(self, child):
        self.__children.append(child)

    def __str__(self):
        return f'{self.__key},\n{self.__data}\n'

    def __repr__(self):
        return f'TreeNode(key={self.__key}, data={self.__data}, children={self.__children})'
