from Structures.Tree.Tree import Tree
from Structures.Tree.Tree import TreeNode
# from Structures.List.List import List
import numpy as np


class Game:
    def __init__(self):
        Game.gen_tab_init(Tree())
        print("Generating tree")

    def gen_tab_init(self, t: Tree):
        Game.gen_tab(np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]), 1, 0, t)

    def gen_tab(self, state, player: int, level: int, t: Tree):
        l = []
        for i in range(0, state.size):
            tmp = state.copy().tolist()
            tmp = tmp[0] + tmp[1] + tmp[2]
            if tmp[i] == 0:
                tmp[i] = player
                tmp = np.array([tmp[i:i + 3] for i in range(0, len(tmp), 3)])
                l.append(Game.gen_tab(tmp, -player, level + 1, t))
        n = TreeNode(level, state)
        n.set_children(l)
        t.insert_node(level, n)
        return n

    def play(self, ):

