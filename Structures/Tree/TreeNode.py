from Structures.List.List import List


class TreeNode:
    def __init__(self, key: int, data=None, parent: int = None, children: List = List()):
        self.__key = key
        self.__data = data
        self.__parent = parent
        self.__children = children

    def get_key(self):
        return self.__key

    def set_key(self, key: int):
        self.__key = key

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def add_child(self, child):
        self.__children.append(child)

    def get_child(self, index: int):
        return self.__children.get(index).get_data()

    def get_children(self):
        return self.__children

    def __str__(self):
        return f'{self.__key}, {self.__data}, {self.__parent}'

    def __repr__(self):
        return f'TreeNode(key={self.__key}, data={self.__data}, children={self.__children}, parent={self.__parent})'
