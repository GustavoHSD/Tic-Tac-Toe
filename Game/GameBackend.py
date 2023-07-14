from Structures.Tree.Tree import Tree
from Structures.List.List import List
import numpy as np

from Structures.Tree.TreeNode import TreeNode


class GameBackend:
    def __init__(self):
        state = np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        self._tree = Tree(0, state)
        self._board = self._tree.root

        GameBackend._gen_tab(state, 1, 0, self._tree)

    @property
    def board(self):
        return self._board

    @staticmethod
    def _gen_tab(state, player: int, level: int, t: Tree):
        children = List()
        for i in range(0, state.size):
            tmp = state.copy().tolist()
            tmp = tmp[0] + tmp[1] + tmp[2]
            if tmp[i] == 0:
                tmp[i] = player
                tmp = np.array([tmp[i:i + 3] for i in range(0, len(tmp), 3)])
                children.append(GameBackend._gen_tab(tmp, -player, level + 1, t))
        n = TreeNode(level, state)
        n.children = children
        t.insert_node(level, n)
        return n

    def check_win(self):
        principal1 = principal_1 = 0
        secondary1 = secondary_1 = 0
        n = 3
        self._board.data.tolist()

        # Horizontal
        for i in range(n):
            if np.array_equal(self._board.data[i], [1, 1, 1]):
                print('horizontal: ', i)
                return 1
            elif np.array_equal(self._board.data[i], [-1, -1, -1]):
                print('horizontal:', i)
                return -1

        # Vertical
        if np.array_equal(self._board.data[0][0], 1) and np.array_equal(self._board.data[1][0], 1) and np.array_equal(self._board.data[2][0], 1):
            return 1

        if np.array_equal(self._board.data[0][1], 1) and np.array_equal(self._board.data[1][1], 1) and np.array_equal(self._board.data[2][1], 1):
            return 1

        if np.array_equal(self._board.data[0][2], 1) and np.array_equal(self._board.data[1][2], 1) and np.array_equal(self._board.data[2][2], 1):
            return 1

        if np.array_equal(self._board.data[0][0], -1) and np.array_equal(self._board.data[1][0], -1) and np.array_equal(self._board.data[2][0], -1):
            return -1

        if np.array_equal(self._board.data[0][1], -1) and np.array_equal(self._board.data[1][1], -1) and np.array_equal(self._board.data[2][1], -1):
            return -1

        if np.array_equal(self._board.data[0][2], -1) and np.array_equal(self._board.data[1][2], -1) and np.array_equal(self._board.get_data()[2][2], -1):
            return -1

        for i in range(n):
            for j in range(n):
                # Principal diagonal
                if (i == j) and self._board.data[i][j] == 1:
                    principal1 += 1
                elif (i == j) and self._board.data[i][j] == -1:
                    principal_1 += 1

                # Secondary diagonal
                if (i + j) == (n - 1) and self._board.data[i][j] == 1:
                    secondary1 += 1
                elif self._board.data[i][j] == -1:
                    secondary_1 += 1

        if principal1 == 3:
            print('Principal diagonal')
            return 1
        elif principal_1 == 3:
            print('Principal diagonal')
            return -1
        if secondary1 == 3:
            print('Secondary diagonal')
            return 1
        elif secondary_1 == 3:
            print('Secondary diagonal')
            return -1
        return 0

    def do_move(self, move):
        self._board = self._tree.dfs(move)

    def next_move(self) -> TreeNode:
        self._board = self._board.get_child(0).get_child(0)
        return self._board.data

