"""
Clone of 2048 game.
"""

import GUI_2048
import random

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

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    ans = [0]*len(line)
    pos = 0
    for num in range(len(line)):
        if line[num] != 0:
            ans[pos] = line[num]
            pos = pos + 1
    
    buff = 0
    for num in range(1,len(ans)):
        if ans[num] == ans[buff]:
            ans[buff] = str(2*ans[buff])
            ans[num] = 0
        else:
            buff = num
    ans = list(map(int, ans))
    ans = [num for num in ans if num != 0]
    add_zero = int(len(line) - len(ans))
    while add_zero:
        ans.append(0)
        add_zero = add_zero - 1
    return ans

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width 
        self._grid = []
        self.reset()
        self._initial_tiles_dict = {}			
        up_row = [0 for x in range(self._grid_width)]
        up_col = [x for x in range(self._grid_width)]
        down_row = [self._grid_height-1 for x in range(self._grid_width)]
        down_col = [x for x in range(self._grid_width)]
        left_row = [x for x in range(self._grid_height)]
        left_col = [0 for x in range(self._grid_height)]
        right_row = [x for x in range(self._grid_height)]
        right_col = [self._grid_width-1 for x in range(self._grid_height)]
        
        self._initial_tiles_dict = {UP: zip(up_row,up_col), 
                        DOWN: zip(down_row,down_col),
                        LEFT: zip(left_row, left_col),
                        RIGHT: zip(right_row, right_col)}
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [ [0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        self._listr = ""
        for lis in self._grid:   
            self._listr.join(map(str, lis)) 
            self._listr = self._listr + ' '
        return self._listr

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
        change = False
        initial_tiles = self._initial_tiles_dict.get(direction)
        offset = OFFSETS[direction]
        if direction == UP or direction == DOWN:
            size = self._grid_height
        elif direction == LEFT or direction == RIGHT:
            size = self._grid_width
        for tile_index in initial_tiles: 
            tile_indices = []
            # iterate through adding offset
            for dummy_i in range(size):
                tile_indices.append(tile_index)
                tile_index = [x + y for x, y in zip(tile_index,offset)]
                tile_index = tuple(tile_index)
            to_merge = []
            for tile_index in tile_indices:
                tile = self.get_tile(tile_index[0], tile_index[1])
                to_merge.append(tile)
            merged = merge(to_merge)
            for tile_index, tile_value in zip(tile_indices, merged):
                  if tile_value != self.get_tile(tile_index[0], tile_index[1]):
                    self.set_tile(tile_index[0], tile_index[1], tile_value)
                    change = True
     
        if change == True:
            self.new_tile()
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        pro_zero = []
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._grid[row][col] == 0:
                    pro_zero.append((row, col))
        pro_pos = random.choice(pro_zero)
        row = pro_pos[0]
        col = pro_pos[1] 
        self._grid[row][col] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


GUI_2048.run_gui(TwentyFortyEight(4, 4))
