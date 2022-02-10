from unittest import TestCase
from Board import *
from Strategies import SmartMoves
from Game import Game

class TestGame(TestCase):
    def test_board(self):
        board = Board(4,6)
        strategy = SmartMoves(board)
        game = Game(board,strategy)
        assert game.board() == board

    def test_human_move(self):
        board = Board(4, 6)
        strategy = SmartMoves(board)
        game = Game(board, strategy)
        game.human_move(2,3,1)
        assert board._data[2][3] == 1


    def test_computer_move(self):
        board = Board(4, 6)
        strategy = SmartMoves(board)
        game = Game(board, strategy)
        assert game.computer_move() == (0,0)

    def test_win_condition(self):
        board = Board(4, 6)
        strategy = SmartMoves(board)
        game = Game(board, strategy)
        assert game.win_condition(1) == False
        game.human_move(0,1,1)
        game.human_move(0,2,1)
        game.human_move(0,3,1)
        game.human_move(0,4,1)
        assert game.win_condition(1) == (100, 100, 100, 400, 1)

    def run_all(self):
        self.test_board()
        self.test_human_move()
        self.test_computer_move()
        self.test_win_condition()
