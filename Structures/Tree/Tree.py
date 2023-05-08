# from Structures.List.List import List
import numpy as np
from Structures.Stack.Stack import Stack
from Structures.Tree.TreeNode import TreeNode


class Tree:
    def __init__(self, key: int, data):
        self.__root = TreeNode(key, data)

    def insert(self, parent: int, key: int, data):
        self.insert_r(self.__root, parent, TreeNode(key, data))

    def insert_r(self, root, parent, treenode):
        if self.__root is None:
            self.__root = treenode
        else:
            if root.get_key() == parent:
                root.add_child(treenode)
            else:
                for i in root.get_children():
                    if i.get_key() == parent:
                        self.insert_r(i, parent, treenode)
                    else:
                        self.insert_r(i, parent, treenode)

    def dfs(self, target):
        return self.__depth_first_search(self.__root, target)

    def __depth_first_search(self, root, target):
        stack = Stack()
        stack.push(root)
        visited = set()
        while not stack.is_empty():
            node = stack.pop()
            visited.add(node)

            if np.array_equal(root.get_data(), target):
                return node

            for child in node.get_data().get_children():
                if child not in visited:
                    stack.push(child)
        return None

    def pre_order(self):
        self.pre_order_r(self.__root)

    def pre_order_r(self, root=None):
        if root is not None:
            print(root)
            for i in root.get_children():
                self.pre_order_r(i)

    def is_empty(self):
        return self.__root is None
