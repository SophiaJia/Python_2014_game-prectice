"""
Clone of 2048 game.
"""

import poc_2048_gui  
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
    Helper function that merges a single row or column in 2048
    """
    # replace with your code
    # get the right order

    result = [0] * len(line)
    index = 0
    j_result = 0
    for i_line in range(0 , len(line)):
        if line[i_line] != 0:
            if line[i_line] != index:
                result[j_result] = line[i_line]
                j_result += 1
                index = line[i_line]
            elif line[i_line] == index:
                result[j_result-1] *= 2
                index = 0
                j_result += 0
        elif line[i_line] == 0:
            j_result += 0         
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.grid_height = grid_height
        self.grid_width  = grid_width
        self.reset( )
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        # replace with your code
        self.cells = [ [0 for dummy_x  in range(self.grid_width)] for dummy_y  in range(self.grid_height)]
            
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self.cells)


    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        self.initial_indice_dict = {
                                    UP : list(tuple([0, dummy_x]) for dummy_x in range(self.grid_width)),
                                    DOWN : list(tuple([self.grid_height - 1, dummy_x]) for dummy_x in range(self.grid_width)),
                                    LEFT : list(enumerate(0 for dummy_x in range(self.grid_height))),
                                    RIGHT : list(enumerate(self.grid_width - 1 for dummy_x in range(self.grid_height)))
                                    }
        
        #newgrid = map(merge, oldgrid)
        lista = self.initial_indice_dict[direction]
        offset = OFFSETS[direction]
        cell_list = []
        
        if direction < 3:
         for i_loop in range (0, self.grid_width):
            row = 0
            col = 0
            ini_cell = lista[i_loop]
            calls = []
            for j_loop in range (0, self.grid_height):
                calls.append((ini_cell[0] + row, ini_cell[1] + col))
                row += offset[0]
                col += offset[1]
            cell_list.append(calls)

            
         for j_loop in range(0,self.grid_width):
            old_num = []
            calls = cell_list[j_loop]
            for i_loop in range(0,self.grid_height):
                cell_one = calls[i_loop]
                old_num.append (self.cells[cell_one[0]][cell_one[1]])   
            new_num = merge(old_num)
            for t_loop in range(0,self.grid_height):
                cell_one = calls[t_loop]
                self.cells[cell_one[0]][cell_one[1]] = new_num[t_loop]
        if direction > 2:
         for i_loop in range (0, self.grid_height):
            row = 0
            col = 0
            ini_cell = lista[i_loop]
            calls = []
            for j_loop in range (0, self.grid_width):
                calls.append((ini_cell[0] + row, ini_cell[1] + col))
                row += offset[0]
                col += offset[1]
            cell_list.append(calls)

           
         for j_loop in range(0,self.grid_height):
            old_num = []
            calls = cell_list[j_loop]
            for i_loop in range(0,self.grid_width):
                cell_one = calls[i_loop]
                old_num.append (self.cells[cell_one[0]][cell_one[1]])   
            new_num = merge(old_num)
            for t_loop in range(0,self.grid_width):
                cell_one = calls[t_loop]
                self.cells[cell_one[0]][cell_one[1]] = new_num[t_loop]
        
        self.new_tile( )
    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        c_somthing = random.randint(0, self.grid_width-1)
        r_somthing = random.randint(0, self.grid_height-1)
        check_repeat = []
        stop = 0
        while self.cells[r_somthing][c_somthing] != 0 :
                c_somthing = random.randint(0, self.grid_width-1)
                r_somthing = random.randint(0, self.grid_height-1)
                check_repeat.append((r_somthing,c_somthing))
                if len(check_repeat) >= self.grid_width *  self.grid_height:
                    stop = 1
                    break
               
        if stop == 0 :       
           self.cells[r_somthing][c_somthing] = random.choice([2] * 9 + [4] * 1) 
        elif stop == 1:
            return 
        
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        # replace with your code
        self.cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        # replace with your code
        self.value = self.cells[row][col]
        return self.value

 
    
poc_2048_gui.run_gui(TwentyFortyEight(3, 3))
