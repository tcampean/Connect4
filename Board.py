from texttable import Texttable
import numpy as np


class InvalidMove(Exception):
    pass


class Board:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._data = np.zeros((rows, columns))

    def row_count(self):
        """""
        returns the number of rows
        """
        return self._rows

    def column_count(self):
        """""
        returns the number of columns
        """
        return self._columns

    def move(self, row, col, piece):
        """""
        Put a piece at the given location
        """
        self._data[row][col] = piece

    def get_lowest_row(self, col):
        """""
        Gets the lowest position a piece can drop
        """
        r = 0
        while r < self._rows:
            if self._data[r][col] == 0:
                r += 1
            else:
                return r - 1
        if self._data[r - 1][col] == 0:
            return r - 1
        else:
            return -1

    def __str__(self):
        t = Texttable()
        t.header([i for i in range(1, self._columns + 1)])
        for row in range(self._rows):
            row_data = []
            for index in self._data[row]:
                if index == 0:
                    row_data.append(' ')
                elif index == 1 or index == 2:
                    row_data.append(index)
            t.add_row(row_data)
        return t.draw()
