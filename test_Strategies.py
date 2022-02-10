from unittest import TestCase
from Board import Board
from Strategies import SmartMoves
import math


class TestSmartMoves(TestCase):
    def test_minimax(self):
        board = Board(4, 6)
        strategy = SmartMoves(board)
        board.move(0,1,1)
        board.move(0,2,1)
        board.move(0,3,1)
        board.move(0,4,1)
        assert strategy.minimax(board,2,-math.inf,math.inf,True) == (-1, -math.inf)
        board = Board(4,6)
        board.move(0, 1, 2)
        board.move(0, 2, 2)
        board.move(0, 3, 2)
        assert strategy.minimax(board,2,-math.inf,math.inf,True) == (0,220)

    def run_all(self):
        self.test_minimax()

