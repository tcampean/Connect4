from unittest import TestCase
from Board import *
from test_Game import *
from test_Strategies import *


class TestBoard(TestCase):

    def test_row_count(self):
        board = Board(4,6)
        assert board.row_count() == 4


    def test_column_count(self):
        board = Board(4,6)
        assert board.column_count() == 6

    def test_move(self):
        board = Board(4,6)
        board.move(1,1,1)
        assert board._data[1][1] == 1

    def test_get_lowest_row(self):
        board = Board(4,6)
        row = board.get_lowest_row(2)
        assert board._data[3][2] == 0
        board.move(1,2,1)
        board.move(2,2,1)
        board.move(3,2,1)
        assert board.get_lowest_row(2) == 0
        board.move(0, 2, 1)
        board.move(1, 2, 1)
        board.move(2, 2, 1)
        board.move(3, 2, 1)
        assert board.get_lowest_row(2) == -1

    def run_all(self):
        self.test_move()
        self.test_column_count()
        self.test_row_count()
        self.test_get_lowest_row()

boards= TestBoard()
strategies = TestSmartMoves()
games = TestGame()
boards.run_all()
strategies.run_all()
games.run_all()