import numpy as np
import random
import pygame
import sys
import math
import copy


class SmartMoves:

    def __init__(self, board):
        self._board = board

    def drop_piece(self, board, row, col, piece):
        """""
        Puts the piece in a given location
        """
        board._data[row][col] = piece

    def check_for_win(self, board, piece):
        """""
        Checks if there are any available winning moves
        """

        # Check horizontal locations for win
        for c in range(board.column_count() - 3):
            for r in range(board.row_count()):
                if board._data[r][c] == piece and board._data[r][c + 1] == piece and board._data[r][c + 2] == piece and \
                        board._data[r][
                            c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(board.column_count()):
            for r in range(board.row_count() - 3):
                if board._data[r][c] == piece and board._data[r + 1][c] == piece and board._data[r + 2][c] == piece and \
                        board._data[r + 3][
                            c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(board.column_count() - 3):
            for r in range(board.row_count() - 3):
                if board._data[r][c] == piece and board._data[r + 1][c + 1] == piece and board._data[r + 2][
                    c + 2] == piece and board._data[r + 3][
                    c + 3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(board.column_count() - 3):
            for r in range(3, board.row_count()):
                if board._data[r][c] == piece and board._data[r - 1][c + 1] == piece and board._data[r - 2][
                    c + 2] == piece and board._data[r - 3][
                    c + 3] == piece:
                    return True

    def evaluate_board(self, row, piece):
        """""
        Evaluates the current state of the board and picks the best move
        """
        score = 0
        enemy = 2
        if piece == enemy:
            enemy = 1
        if row.count(piece) == 4:
            score += 1000
        elif row.count(piece) == 3 and row.count(0) == 1:
            score += 100
        elif row.count(piece) == 2 and row.count(0) == 2:
            score += 10
        elif row.count(enemy) == 3 and row.count(0) == 1:
            score -= 1000

        return score

    def score_position(self, board, piece):
        """""
        Checks for every possible move and makes the one with the highest score
        """
        score = 0

        # Score Horizontal
        for r in range(board.row_count()):
            row_array = [int(i) for i in list(board._data[r, :])]
            for c in range(board.column_count() - 3):
                row = row_array[c:c + 4]
                score += self.evaluate_board(row, piece)

        # Score Vertical
        for c in range(board.column_count()):
            col_array = [int(i) for i in list(board._data[:, c])]
            for r in range(board.row_count() - 3):
                col = col_array[r:r + 4]
                score += self.evaluate_board(col, piece)

        # Score positive sloped diagonal
        for r in range(board.row_count() - 3):
            for c in range(board.column_count() - 3):
                slope = [board._data[r + i][c + i] for i in range(4)]
                score += self.evaluate_board(slope, piece)

        # Score negative sloped diagonal
        for r in range(board.row_count() - 3):
            for c in range(board.column_count() - 3):
                slope = [board._data[r + 3 - i][c + i] for i in range(4)]
                score += self.evaluate_board(slope, piece)

        return score

    def get_valid_locations(self, board):
        """""
        Returns a list with all columns that have at least one place open
        """
        valid_locations = []
        for col in range(board.column_count()):
            if board._data[0][col] == 0:
                valid_locations.append(col)
        return valid_locations

    def computer_move(self):
        """""
        Calls the minmax algorithm
        """
        return self.minimax(self._board, 2, -math.inf, math.inf, True)

    def is_terminal_node(self, board):
        """""
        Checks if the game will end or has ended
        """
        return self.check_for_win(board, 1) or self.check_for_win(board, 2) or len(self.get_valid_locations(board)) == 0

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        """""
        Minmax algorithm
        Does a schematic search for possible moves on a copy of a board
        Uses Alpha Beta pruning which decreases the number of nodes evaluated by minimax in its search tree
        if one possibility has been found
        Takes into account every scenario (measured in score) and picks the very best one
        """
        valid_locations = self.get_valid_locations(board)
        is_terminal = self.is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.check_for_win(board, 2):
                    return (-1, math.inf)
                elif self.check_for_win(board, 1):
                    return (-1, -math.inf)
                else:
                    return (-1, 0)
            else:
                return (-1, self.score_position(board, 2))
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = board.get_lowest_row(col)
                b_copy = copy.deepcopy(board)
                self.drop_piece(b_copy, row, col, 2)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                if alpha < value:
                    alpha = value
                if alpha >= beta:
                    break
            return column, value

        else:
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = board.get_lowest_row(col)
                b_copy = copy.deepcopy(board)
                self.drop_piece(b_copy, row, col, 1)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                if beta > value:
                    beta = value
                if alpha >= beta:
                    break
            return column, value

class MediumMoves:

    def __init__(self, board):
        self._board = board

    def drop_piece(self, board, row, col, piece):
        """""
        Puts the piece in a given location
        """
        board._data[row][col] = piece

    def evaluate_board(self, row, piece):
        """""
        Evaluates the current state of the board and picks the best move
        """
        score = 0
        enemy = 2
        if piece == enemy:
            enemy = 1
        if row.count(piece) == 4:
            score += 1000
        elif row.count(piece) == 3 and row.count(0) == 1:
            score += 100
        elif row.count(piece) == 2 and row.count(0) == 2:
            score += 10
        elif row.count(enemy) == 3 and row.count(0) == 1:
            score -= 1000

        return score

    def score_position(self, board, piece):
        """""
        Checks for every possible move and makes the one with the highest score
        """
        score = 0

        # Score Horizontal
        for r in range(board.row_count()):
            row_array = [int(i) for i in list(board._data[r, :])]
            for c in range(board.column_count() - 3):
                row = row_array[c:c + 4]
                score += self.evaluate_board(row, piece)

        # Score Vertical
        for c in range(board.column_count()):
            col_array = [int(i) for i in list(board._data[:, c])]
            for r in range(board.row_count() - 3):
                col = col_array[r:r + 4]
                score += self.evaluate_board(col, piece)

        # Score positive sloped diagonal
        for r in range(board.row_count() - 3):
            for c in range(board.column_count() - 3):
                slope = [board._data[r + i][c + i] for i in range(4)]
                score += self.evaluate_board(slope, piece)

        # Score negative sloped diagonal
        for r in range(board.row_count() - 3):
            for c in range(board.column_count() - 3):
                slope = [board._data[r + 3 - i][c + i] for i in range(4)]
                score += self.evaluate_board(slope, piece)

        return score

    def get_valid_locations(self, board):
        """""
        Returns a list with all columns that have at least one place open
        """
        valid_locations = []
        for col in range(board.column_count()):
            if board._data[0][col] == 0:
                valid_locations.append(col)
        return valid_locations

    def computer_move(self):
        """""
        Check all available moves and picks the one with the highest score
        """
        valid_locations = self.get_valid_locations(self._board)
        best_score = -1000
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = self._board.get_lowest_row(col)
            b_copy = copy.deepcopy(self._board)
            self.drop_piece(b_copy, row, col, 2)
            score = self.score_position(b_copy, 2)
            if score > best_score:
                best_score = score
                best_col = col

        return best_col, None

class RandomMoves():

    def __init__(self, board):
        self._board = board

    def get_valid_locations(self):
        """""
        Returns a list with all columns that have at least one place open
        """
        valid_locations = []
        for col in range(self._board.column_count()):
            if self._board._data[0][col] == 0:
                valid_locations.append(col)
        return valid_locations

    def computer_move(self):
        valid_locations = self.get_valid_locations()
        col = random.choice(valid_locations)
        return col, None
