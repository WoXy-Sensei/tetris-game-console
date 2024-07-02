from adafruit_display_shapes.rect import Rect
from tetris.colors import Colors
from tetris.position import Position

class Block:
    def __init__(self,id):
        self.id = id
        self.cells = {}
        self.cell_size = 8
        self.rotation_state = 0
        self.row_offset = 0
        self.col_offset = 0

    def move(self,row,col):
        self.row_offset += row
        self.col_offset += col

    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == 4:
            self.rotation_state = 0
    
    def undo_rotate(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    def get_cell_positions(self):
        try:
            tiles = self.cells[self.rotation_state]
        except:
            tiles = self.cells[0]
        move_tiles = []
        for tile in tiles:
            pos = Position(tile.row + self.row_offset, tile.col + self.col_offset)
            move_tiles.append(pos)
        
        return move_tiles
    
    def draw_block(self, group, offsetx = 0, offsety = 0):
        tiles = self.get_cell_positions()
        nums = 0
        for tile in tiles:
            rect = Rect(offsetx+tile.col*self.cell_size , offsety+tile.row*self.cell_size , self.cell_size - 1 , self.cell_size - 1,fill=Colors.get_colors()[self.id])
            group[nums] = rect
            nums+=1