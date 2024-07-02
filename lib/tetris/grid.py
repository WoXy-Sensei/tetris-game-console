from tetris.colors import Colors
from tetris.rect import draw_rect
class Grid:
    def __init__(self):
        self.col = 10
        self.row = 20
        self.cell_size = 8
        self.grid = [[0 for _ in range(self.col)] for _ in range(self.row)]
        self.colors = Colors.get_colors()
        self.temp = [[0 for _ in range(self.col)] for _ in range(self.row)]

    def print_grid(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.grid[i][j], end=" ")
            print()
        
    def check_collision(self, row, col):
        if row >= 0 and row < self.row and col >= 0 and col < self.col:
            return True
        return False
    
    def is_empty(self,row,col):
        if(self.grid[row][col] == 0):
            return True
        return False
    
    def is_row_full(self,row):
        for col in range(self.col):
            if(self.grid[row][col] == 0):
                return False
        return True

    def clear_row(self,row):
        for col in range(self.col):
            self.grid[row][col] = 0
        
    def move_rows_down(self,row,num_row):
        for col in range(self.col):
            self.grid[row+num_row][col] = self.grid[row][col]
            self.grid[row][col] = 0
    
    def clear_full_rows(self):
        complated = 0
        for row in range(self.row-1,0,-1):
            if(self.is_row_full(row)):
                self.clear_row(row)
                complated += 1
            elif(complated > 0):
                self.move_rows_down(row,complated)
        
        return complated

    def reset(self):
        self.grid = [[0 for _ in range(self.col)] for _ in range(self.row)]
    
    def draw_grid(self, background):
        for i in range(self.row):
            for j in range(self.col):
                if(self.grid[i][j] != self.temp[i][j]):
                    draw_rect(j*self.cell_size + 1, i*self.cell_size + 1, self.cell_size - 1 , self.cell_size - 1,background,self.grid[i][j])
                    self.temp[i][j] = self.grid[i][j]
                
