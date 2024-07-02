from tetris.grid import Grid
from tetris.blocks import *
import random
from adafruit_display_shapes.rect import Rect
from tetris.rect import draw_rect

class Game:
    def __init__(self,background_group,blocks_group,interface) -> None:
        self.grid:Grid = Grid()
        self.blocks:list[Block] = [IBlock(), LBlock(), OBlock(), TBlock(), ZBlock(), SBlock(), JBlock()]
        self.block:Block = self.get_random_block()
        self.next_block:Block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.background_group = background_group
        self.blocks_group = blocks_group
        self.interface = interface
        
        for i in range(0,4):
            self.blocks_group.append(Rect(0,0,1,1))
        for i in range(0,4):
            self.interface[0].append(Rect(0,0,1,1))
            
        self.draw_next_block()
        
        for i in range(self.grid.row):
            for j in range(self.grid.col):
                draw_rect(j*self.grid.cell_size + 1, i*self.grid.cell_size + 1, self.grid.cell_size - 1 , self.grid.cell_size - 1,self.background_group[1],9)
               

    def get_random_block(self):
        if(len(self.blocks) == 0 ):
            self.blocks = [IBlock(), LBlock(), OBlock(), TBlock(), ZBlock(), SBlock(), JBlock()]

        return self.blocks.pop(random.randint(0, len(self.blocks) - 1))

    def update_score(self,lines,movedown):
        if(lines == 1):
            self.score += 100
        elif(lines == 2):
            self.score += 300
        elif(lines == 3):
            self.score += 500
        
        self.score += movedown
    
    def move_left(self):
        self.block.move(0,-1)
        if(self.check_block_collision() == False  or self.block_fits() == False):
            self.block.move(0,1)
    
    def move_right(self):
        self.block.move(0,1)
        if(self.check_block_collision() == False or self.block_fits() == False):
            self.block.move(0,-1)
    
    def move_down(self):
        self.block.move(1,0)
        if(self.check_block_collision() == False  or self.block_fits() == False):
            self.block.move(-1,0)
            self.lock_block()
            
    def reset(self):
        self.grid.reset()
        self.score = 0
        self.blocks = [IBlock(), LBlock(), OBlock(), TBlock(), ZBlock(), SBlock(), JBlock()]
        self.block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.draw_next_block()

    def lock_block(self):
        block_pos = self.block.get_cell_positions()
        for pos in block_pos:
            self.grid.grid[pos.row][pos.col] = self.block.id
        self.block = self.next_block
        self.next_block = self.get_random_block()
        self.draw_next_block()
        clear_row_num = self.grid.clear_full_rows()
        self.update_score(clear_row_num,0)
        if(self.block_fits() == False):
            print("Game Over")
            self.game_over = True
    
    def block_fits(self):
        block_pos = self.block.get_cell_positions()
        for pos in block_pos:
            if(self.grid.is_empty(pos.row, pos.col) == False):
                return False
        return True
    
    def rotate(self):
        self.block.rotate()
        if(self.check_block_collision() == False):
            self.block.undo_rotate()
    

    def check_block_collision(self):
        block_pos = self.block.get_cell_positions()
        for pos in block_pos:
            if(self.grid.check_collision(pos.row, pos.col) == False):
                return False
        return True
        
    def draw(self):
        self.grid.draw_grid(self.background_group[0])
        self.block.draw_block(self.blocks_group,1,1)
        
    def draw_next_block(self):
        self.next_block.draw_block(self.interface[0], 65, 80)
            


