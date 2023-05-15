from Structures.Tree.Tree import Tree
from Structures.Tree.Tree import TreeNode
from Structures.List.List import List
import numpy as np


def gen_tab_init(t: Tree):
    gen_tab(np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]), 1, 0, t)


def gen_tab(state, player: int, level: int, t: Tree, iterations: int):
    iterations += 1  # Increment iterations count
    l = []
    for i in range(0, state.size):
        tmp = state.copy().tolist()
        tmp = tmp[0] + tmp[1] + tmp[2]
        if tmp[i] == 0:
            tmp[i] = player
            tmp = np.array([tmp[i:i + 3] for i in range(0, len(tmp), 3)])
            l.append(gen_tab(tmp, -player, level + 1, t))
    n = TreeNode(None, state)
    n.set_children(l)
    t.insert_node(level, n)
    return n, iterations  # Return iterations count

tree = Tree(0, 0)
target = np.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 1, -1]
    ])

gen_tab_init(tree)
# for i in tree.dfs(target).get_children():
#     print(i)
