import math


class Game:

    def __init__(self, board, strategy):
        self._board = board
        self._strategy = strategy

    def board(self):
        """""
        Returns the board
        """
        return self._board

    def human_move(self, row, column, player):
        """""
        Calls the move function of the board
        """
        return self._board.move(row, column, player)

    def computer_move(self):
        """""
        Calls the function that provides the best move for the computer to make
        """

        return self._strategy.computer_move()

    def win_condition(self, piece):
        """""
        Checks the entire board for any combinations of 4 pieces
        Returns true if found
        """
        # Horizontal check
        for c in range(self._board.column_count() - 3):
            for r in range(self._board.row_count()):
                if self._board._data[r][c] == piece and self._board._data[r][c + 1] == piece and self._board._data[r][
                    c + 2] == piece and self._board._data[r][c + 3] == piece:
                    return (r+1)*100,(c)*100, (r+1)*100,(c+3) *100,1

        # Vertical check
        for c in range(self._board.column_count()):
            for r in range(self._board.row_count() - 3):
                if self._board._data[r][c] == piece and self._board._data[r + 1][c] == piece and \
                        self._board._data[r + 2][c] == piece and self._board._data[r + 3][c] == piece:
                    return (r+1) * 100, c * 100,(r+4)*100,c*100,2

        # Diagonal check(main)
        for c in range(self._board.column_count() - 3):
            for r in range(self._board.row_count() - 3):
                if self._board._data[r][c] == piece and self._board._data[r + 1][c + 1] == piece and \
                        self._board._data[r + 2][c + 2] == piece and self._board._data[r + 3][c + 3] == piece:
                    return (r+1) * 100, c * 100,(r+4)*100,(c+3) *100,3

        # Diagonal check(secondary)
        for c in range(self._board.column_count() - 3):
            for r in range(3, self._board.row_count()):
                if self._board._data[r][c] == piece and self._board._data[r - 1][c + 1] == piece and \
                        self._board._data[r - 2][c + 2] == piece and self._board._data[r - 3][c + 3] == piece:
                    return (r+1) * 100,c*100 ,(r-2) * 100,(c+3)*100,4
        return False
