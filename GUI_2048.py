"""
2048 GUI
"""

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

# Tile Images
TILE_SIZE = 101
HALF_TILE_SIZE = TILE_SIZE / 2
BORDER_SIZE = 45

# Directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Image URL
URL = "https://img.favpng.com/21/25/19/graph-of-a-function-geometric-shape-chart-geometry-square-png-favpng-R5XEtvA9dNL3s1wQK5GHxwKY2.jpg"

# Instructions
INSTRUCTION_TEXT = \
["2048 is a simple grid-based numbers game.", \
"The object of the game is to combine tiles with the same",\
"number to make larger numbered tiles. You 'win' when you", \
"create a 2048 tile.", \
"You will have a grid of tiles (size can be modify, ", \
"check code - line 41) and two numbers on start: '2' 90%",\
"of the time and '4' 10% of the time. On each turn, you may",\
"slide all of the tiles on the board in one direction",\
"(left, right, up, or down).When you do so, all of the", \
"tiles on the board slide as far as they can go in the", \
"given direction leaving no empty squares between the tiles.",\
"Further, if two tiles of the same number end up next to", \
"each other, they merge to form a new tile with twice the", \
"value. If any tile slide, new random tile will be given", \
"with the same manner as on start. If no tiles would combine", \
"or slide in a given direction, then that is not a legal", \
"move, and you cannot make that move on the current turn.", \
"If there are no free tiles on the grid, the game ends.", \
"You can hit New Game button to reset Game, any time."]

class GUI:
    """
    Class to run game GUI.
    """

    def __init__(self, game):
        self._draw_instruction = False
        self._rows = game.get_grid_height()
        self._cols = game.get_grid_width()
        self._frame = simplegui.create_frame('2048',
                        self._cols * TILE_SIZE + 2 * BORDER_SIZE,
                        self._rows * TILE_SIZE + 2 * BORDER_SIZE)
        self._frame.add_button('New Game', self.start, 100)
        for labels in range(20):
            self._frame.add_label("", 200)
        self._button = self._frame.add_button("How to Play", self.instruction, 100)
        self._frame.set_keydown_handler(self.keydown)
        self._frame.set_draw_handler(self.draw)
        self._frame.set_canvas_background("#BCADA1")
        self._frame.start()
        self._game = game
        url = URL
        self._tiles = simplegui.load_image(url)
        self._directions = {"up": UP, "down": DOWN,
                            "left": LEFT, "right": RIGHT}

    def keydown(self, key):
        """
        Keydown handler
        """
        for dirstr, dirval in self._directions.items():
            if key == simplegui.KEY_MAP[dirstr]:
                self._game.move(dirval)
                break
                
    def instruction(self):
        """
        Show / Hide Game instructon
        """
        if self._draw_instruction == False:
            self._draw_instruction = True
            self._button.set_text("Back to Game")
        else:
            self._draw_instruction = False
            self._button.set_text("How to Play")

    def draw(self, canvas):
        """
        Draw handler
        """
        if self._draw_instruction:
            text_pos = 55
            canvas.draw_text("2048 - HOW TO PLAY?", (20, 25), 23, "White")
            for line in INSTRUCTION_TEXT:
                canvas.draw_text((line), (10, text_pos), 20, "White")
                text_pos += 23
        else:
            for row in range(self._rows):
                for col in range(self._cols):
                    tile = self._game.get_tile(row, col)
                    if tile == 0:
                        val = 0
                    else:
                        val = int(math.log(tile, 2))
                    canvas.draw_image(self._tiles,
                                      [HALF_TILE_SIZE + val * TILE_SIZE, HALF_TILE_SIZE],
                                      [TILE_SIZE, TILE_SIZE],
                                      [col * TILE_SIZE + HALF_TILE_SIZE + BORDER_SIZE,
                                       row * TILE_SIZE + HALF_TILE_SIZE + BORDER_SIZE],
                                      [TILE_SIZE, TILE_SIZE])

    def start(self):
        """
        Start the game.
        """
        self._game.reset()

        
def run_gui(game):
    """
    Instantiate and run the GUI.
    """
    gui = GUI(game)
    gui.start()
