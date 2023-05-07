import numpy as np


class Board:
    def __init__(self):
        self.__board = np.zeros(9).reshape(3.3)

    def get_board(self):
        return self.__board

    def set_board(self, x: int, y: int):
        self.__board[x, y] = -1

    def display(self):
        return str(self.__board)