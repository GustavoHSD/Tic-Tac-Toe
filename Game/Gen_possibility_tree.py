from Structures.Tree.Tree import Tree
import numpy as np


class GenPossibilityTree:
    board = np.zeros(9).reshape(3, 3)
    t = Tree(0, None)

    def gen_new_state(self, state, x: int, y: int, player: int):
        n_state = state.copy()
        n_state[x, y] = player
        return n_state

    def gen_state(self, level: int, state, player: int, tree: Tree, max_depth: int):
        if level >= max_depth:
            return
        for i in range(3):
            for j in range(3):
                if state[i, j] == 0:
                    n_state = self.gen_new_state(state, i, j, player)
                    tree.insert(level, i + j, n_state)
                    self.gen_state(level + 1, n_state, -player, tree, max_depth)
