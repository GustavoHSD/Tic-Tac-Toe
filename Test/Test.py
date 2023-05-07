from Structures.Tree.TreeNode import TreeNode
from Structures.Tree.Tree import Tree
from Structures.List.List import List
import numpy as np

board = np.zeros(9).reshape(3, 3)
tree = Tree(0, None)
list_ = List()


def gen_board(state, x, y):
    state[x, y] = -1
    return state


def gen_state_init():
    return gen_state(board, 1, 0)


t = Tree(0, board, None, None)


def gen_state(state, player, level):
    states = List()
    w = 0
    for i in range(3):
        w += 1
        for j in range(3):
            if state[i, j] == 0:
                w += 1
                new_state = state
                new_state[i, j] = player
                states.append(gen_board(new_state, i, j))
                gen_state(new_state, -player, level+1)
    print(state)
    t.insert(level, i+j, state, states)


# t.pre_order()

gen_state(board, 1, 0)
