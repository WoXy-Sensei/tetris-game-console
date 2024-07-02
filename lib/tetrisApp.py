from application import App
from keyInput import KeyInput
import time
from tetris.game import Game
from bitmap import Bitmap
from adafruit_display_text import label
import terminalio
import displayio


class Tetris(App):
    def __init__(self):
        super().__init__("Tetris")

        # Palettes
        palette1 = displayio.Palette(11)
        palette1[0] = 0xffffff
        palette1[1] = 0x2fe617
        palette1[2] = 0xe81212
        palette1[3] = 0xe27411
        palette1[4] = 0xedea04
        palette1[5] = 0xa600f7
        palette1[6] = 0x15ccd1
        palette1[7] = 0x0d40d8
        palette1[8] = 0x000000
        palette1[9] = 0x1a1f28
        palette1.make_transparent(0)

        # Bitmaps
        self.bitmap = Bitmap()
        self.background_block, self.bitmap_background_block = self.bitmap.create_bitmap_tile(
            80, 160, 0, 0, palette1)
        self.background_tile, self.bitmap_background_tile = self.bitmap.create_bitmap_tile(
            80, 160, 0, 0, palette1)

        # Display Groups
        self.gameDisplay = displayio.Group()
        self.interfaceDisplay = displayio.Group()

        self.screen.append(self.gameDisplay)
        self.screen.append(self.interfaceDisplay)

        # Game
        self.game_blocks = displayio.Group()
        self.game_background = displayio.Group()

        self.game_background.append(self.background_tile)
        self.game_background.append(self.background_block)

        self.gameDisplay.append(self.game_background)
        self.gameDisplay.append(self.game_blocks)

        # Interface
        self.interface_next_block = displayio.Group()
        self.interfaceDisplay.append(self.interface_next_block)

        self.score_label = label.Label(font=terminalio.FONT, text="0", scale=1)
        self.score_label.anchor_point = (0, 0)
        self.score_label.anchored_position = (100, 30)

        self.interfaceDisplay.append(self.score_label)

        # Game Classes
        self.keyInput = KeyInput()
        self.game = Game([self.bitmap_background_block, self.bitmap_background_tile],
                         self.game_blocks, self.interfaceDisplay)

        # Game Variables
        self.move_down_time = time.monotonic()

    def init(self):
        print(self.screen)

    def update(self):
        if ((self.move_down_time + 0.25) < time.monotonic() and self.game.game_over != True):
            self.game.move_down()
            self.move_down_time = time.monotonic()

        if (self.game.game_over != True):
            if self.keyInput.isHoldKey("A"):
                self.game.move_left()
            if self.keyInput.isHoldKey("B"):
                self.game.move_right()
            if self.keyInput.isHoldKey("X"):
                self.game.update_score(0, 1)
                self.game.move_down()
            if self.keyInput.isPressedKey("Y"):
                self.game.rotate()
        else:
            if self.keyInput.isPressedKey("Y"):
                self.game.game_over = False
                self.game.reset()
            if self.keyInput.isPressedKey("X"):
                self.close()

        self.game.draw()
        self.score_label.text = str(self.game.score)

    def close(self):
        super().close()
