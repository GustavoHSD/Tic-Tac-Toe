# from Structures.List.List import List
import numpy as np

from Structures.List.List import List
# from Structures.Stack.Stack import Stack
from Structures.Tree.TreeNode import TreeNode


class Tree:
    def __init__(self, key: int, data):
        self.__root = TreeNode(key, data)

    @property
    def root(self):
        return self.__root

    def insert_node(self, parent: int, node: TreeNode):
        self.__insert_r(self.__root, parent, node)

    def insert(self, parent: int, key: int, data):
        self.__insert_r(self.__root, parent, TreeNode(key, data))

    def __insert_r(self, root: TreeNode, parent: int, treenode: TreeNode):
        if self.__root is None:
            self.__root = treenode
        else:
            if root.key == parent:
                root.add_child(treenode)
            else:
                for i in root.children:
                    if i.get_key() == parent:
                        self.__insert_r(i, parent, treenode)
                    else:
                        self.__insert_r(i, parent, treenode)

    def dfs(self, target):
        return self.__depth_first_search_r(self.__root, target)

    def __depth_first_search_r(self, root: TreeNode, target):
        if np.array_equal(root.data, target):
            return root
        for i in root.children:
            if np.array_equal(i, target):
                return i
            else:
                result = self.__depth_first_search_r(i, target)
                if result is not None:
                    return result
        return None

    def pre_order(self):
        self.__pre_order_r(self.__root)

    def __pre_order_r(self, root=None):
        if root is not None:
            print(root)
            for i in root.children:
                self.__pre_order_r(i)

    def is_empty(self):
        return self.__root is None
