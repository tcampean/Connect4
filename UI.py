from Board import *
from random import randint


class UI:
    def __init__(self, board, game):
        self._board = board
        self._game = game

    def read_human_move(self):
        column = input("Enter the column: ")
        try:
            column = int(column)
        except ValueError:
            print("This is not a column")
            return
        return int(column)

    def start(self):
        game_over = False
        player_turn = randint(1, 2)
        places = self._board.column_count() * self._board.row_count()
        while not game_over:
            print(self._game.board())
            if places == 0:
                game_over = True
                print("The game ended in a draw!")

            elif player_turn == 1:
                moved = False
                while not moved:
                    col = self.read_human_move()
                    if col not in range(1, self._board.column_count() + 1):
                        print("Gosh you are so bad at the game you even missed the board...")
                        continue
                    try:
                        row = self._board.get_lowest_row(col - 1)
                        if row == -1:
                            raise InvalidMove("The column is already full!")
                        self._game.human_move(row, col - 1, player_turn)
                        moved = True
                        player_turn += 1
                        places -= 1
                        if self._game.win_condition(1):
                            print("Player 1 WINS!")
                            print(self._game.board())
                            return
                    except InvalidMove as im:
                        print(str(im))

            else:
                col = self._game.computer_move()[0]

                if self._board._data[0][col] == 0:
                    row = self._board.get_lowest_row(col)
                    self._game.human_move(row, col, 2)

                player_turn -= 1
                places -= 1
                if self._game.win_condition(2):
                    print("Player 2 WINS!")
                    print(self._game.board())
                    return
