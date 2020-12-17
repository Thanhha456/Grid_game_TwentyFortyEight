"""
Clone of 2048 game.
"""

import poc_2048_gui
import random
GRID_HEIGHT = 4
GRID_WIDTH = 5
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}
# grid = TwentyFortyEight(GRID_HEIGHT,GRID_WIDTH )


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_width, grid_height):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = [[0 for dummy_y in range(self._grid_height)] for dummy_x in range(self._grid_width)]

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        for dummy_row in range(self._grid_width):
            for dummy_col in range(self._grid_height):
                self._grid[dummy_row][dummy_col] = 0
        self.new_tile()
        self.new_tile()
        print(self._grid)
        return self

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        move_tile = False
        step = OFFSETS[direction]
        start_cell = 0, 0
        temp_list = []
        clone = clone_grid(self)

        if direction == 1:
            for dummy_col in range(self._grid_width):
                start_cell = 0, dummy_col
                col_list = tranverse_grid(self, start_cell, OFFSETS[1], self._grid_height)
                col_list = merge(col_list)
                temp_list.append(col_list)
            for dummy_col in range(self._grid_width):
                for dummy_row in range(self._grid_height):
                    self.set_tile(dummy_row, dummy_col, temp_list[dummy_col][dummy_row])

        elif direction == 2:
            for dummy_col in range(self._grid_width):
                start_cell = self._grid_height - 1, dummy_col
                col_list = tranverse_grid(self, start_cell, OFFSETS[2], self._grid_height)
                col_list = merge(col_list)
                temp_list.append(col_list[::-1])
            for dummy_col in range(self._grid_width):
                for dummy_row in range(self._grid_height):
                    self.set_tile(dummy_row, dummy_col, temp_list[dummy_col][dummy_row])

        elif direction == 3:
            for dummy_row in range(self._grid_height):
                start_cell = dummy_row, 0
                row_list = tranverse_grid(self, start_cell, OFFSETS[3], self._grid_width)
                row_list = merge(row_list)
                temp_list.append(row_list)
            for dummy_col in range(self._grid_width):
                for dummy_row in range(self._grid_height):
                    self.set_tile(dummy_row, dummy_col, temp_list[dummy_row][dummy_col])

        else:
            for dummy_row in range(self._grid_height):
                start_cell = dummy_row, self._grid_width - 1
                row_list = tranverse_grid(self, start_cell, OFFSETS[4], self._grid_width)
                row_list = merge(row_list)
                temp_list.append(row_list[::-1])
            for dummy_col in range(self._grid_width):
                for dummy_row in range(self._grid_height):
                    self.set_tile(dummy_row, dummy_col, temp_list[dummy_row][dummy_col])

        if clone != self:
            self.new_tile()
        return self._grid

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        tiles_list = [4]
        for dummy in range(9):
            tiles_list.append(2)
        random.shuffle(tiles_list)
        new = tiles_list.pop()
        empty_list = empty_squares(self)
        sqr = random.choice(empty_list)
        if self.get_tile(sqr[0], sqr[1]) == 0:
            self.set_tile(sqr[0], sqr[1], new)
        return self


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value


    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    num = len(line)
    for idx in range(len(line) - 1):
        if line[idx] == line[idx + 1]:
            line[idx] *= 2
            line[idx + 1] = 0
    line_remove = []
    for dummy in range(num):
        if line[dummy] == 0:
            line_remove.append(line[dummy])
    for dummy_y in line_remove:
        line.remove(dummy_y)
    for dummy_x in range(len(line), num):
        line.append(0)
    return line

def empty_squares(grid):
    """
    :param grid:
    :return: a list of empty squares
    """
    empty_list = []
    for dummy_row in range(grid.get_grid_width()):
        for dummy_col in range(grid.get_grid_height()):
            if grid.get_tile(dummy_row, dummy_col) == 0:
                empty_list.append((dummy_row, dummy_col))
    return empty_list

def tranverse_grid(grid, start_cell, direction, num_steps):
    """
    Iritation through row/col and get the list of tiles of it.
    :param start_cell:
    :param direction:
    :param num_steps:
    :return:
    """
    trans_list = []
    for step in range(num_steps):
        row_value = start_cell[0] + direction[0]*step
        col_value = start_cell[1] + direction[1]*step
        trans_list.append(grid.get_tile(row_value,col_value))
    return trans_list
def clone_grid(grid):
    """
    make a copy of grid
    :param grid:
    :return:
    """
    grid_width = grid.get_grid_width()
    grid_height = grid.get_grid_height()
    clone = TwentyFortyEight(grid_width, grid_height)
    for dummy_row in range(grid_width):
        for dummy_col in range(grid_height):
             clone.set_tile(dummy_row, dummy_col, grid.get_tile(dummy_row, dummy_col))
    return clone

# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))