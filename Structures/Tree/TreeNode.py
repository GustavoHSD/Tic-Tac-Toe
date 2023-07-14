from Structures.List.List import List

class TreeNode:
    def __init__(self, key, data):
        self.__key = key
        self.__data = data
        self.__children = List()

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def key(self) -> int:
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def children(self) -> List:
        return self.__children

    @children.setter
    def children(self, children: List):
        self.__children = children

    def get_child(self, i) -> 'TreeNode':
        if self.__children.get(i) is not None:
            return self.__children.get(i)
        return None

    def add_child(self, child):
        self.__children.append(child)

    def __str__(self):
        return f'{self.__key},\n{self.__data}\n'

    def __repr__(self):
        return f'TreeNode(key={self.__key},\n data=\n{self.__data},\n children_length=\n{len(self.__children)})'


