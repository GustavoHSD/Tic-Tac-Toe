from Structures.List.List import List
from Structures.Tree.TreeNode import TreeNode


class Tree:
    def __init__(self, key, data, parent=None, children: List = List()):
        self.__root = TreeNode(key, data, parent, children)

    def insert(self, parent, key, data, children: List = List()):
        self.insert_r(self.__root, parent, TreeNode(key, data, parent, children))

    def insert_r(self, root, parent, treenode: TreeNode):
        if self.__root is None:
            self.__root = treenode
        else:
            if root.get_key() == parent:
                print(treenode, ' added')
                root.add_child(treenode)
            else:
                for i in root.get_children():
                    if i.get_key() == parent:
                        self.insert_r(i, parent, treenode)
                    else:
                        self.insert_r(i, parent, treenode)

    def pre_order(self):
        self.pre_order_r(self.__root)

    def pre_order_r(self, root=None):
        if root is not None:
            print(root)
            for i in root.get_children():
                self.pre_order_r(i)

    def is_empty(self):
        return self.__root is None
