# from Structures.List.List import List
import numpy as np

from Structures.List.List import List
from Structures.Stack.Stack import Stack
from Structures.Tree.TreeNode import TreeNode


class Tree:
    def __init__(self, key: int, data):
        self.__root = TreeNode(key, data)

    def get_root(self):
        return self.__root

    def insert_node(self, parent: int, node: TreeNode):
        self.insert_r(self.__root, parent, node)

    def insert(self, parent: int, key: int, data):
        self.insert_r(self.__root, parent, TreeNode(key, data))

    def insert_r(self, root: TreeNode, parent: int, treenode: TreeNode):
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
        return self.depth_first_search_r(self.__root, target, List())

    def depth_first_search_r(self, root: TreeNode, target, visited: List):
        if np.array_equal(root.get_data(), target):
            print('equal')
            return root
        visited.append(root)
        for i in root.get_children():
            if np.array_equal(i, target):
                print('equal')
                return i
            elif i not in visited:
                result = self.depth_first_search_r(i, target, visited)
                if result is not None:
                    return result
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
