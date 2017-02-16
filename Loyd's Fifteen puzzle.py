"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        # replace with your code
        
        output = False
        if self.get_number(target_row, target_col) == 0:
            output = True
            for dummy_row in range(target_row + 1, self.get_height()):
                for dummy_col in range(0, self.get_width()):
                    output = self.get_number(dummy_row, dummy_col) == (dummy_row) * self.get_width() + dummy_col and output                    
            for dummy_col in range(target_col + 1, self.get_width()):
                    output = self.get_number(target_row , dummy_col) == (target_row ) * self.get_width() + dummy_col and output
                                   
        return output

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # replace with your code
        # set up dictiontion for moving in the same row
        #move_row = {1: 'r', -1: 'l'}
        #move_col = {1: 'u', -1: 'd'}
        
        string = ""
        
        if self.lower_row_invariant(target_row, target_col):
            value = target_row * self.get_width() + target_col
            #print value 
            for dummy_row in range(0, target_row + 1):
                for dummy_col in range(0, self.get_width() ):
                    if self.get_number(dummy_row, dummy_col) == value:
                        loc = (dummy_row, dummy_col)                    
                        #print loc
            
            #print target_row - loc[0]
            #print target_col - loc[1]
            diff = [target_row - loc[0], target_col - loc[1]]
            #print diff
            
            #diff = [2,2]
            # if at the same row
            #diff = [*, 0]
            if diff[1] == 0 :
                string += "u" * diff[0] + "rddlu" * (diff[0] - 1) + "ld"
            # if at the same col
            #diff = [0, *]
            elif diff[0] == 0 :                
                string += "l" * diff[1] + "urrdl" * (diff[1] - 1)
            # if  row > 0  and col > 0 
            elif diff[0] > 0:
                if diff[1] > 0:
                   string += "l" * diff[0] + "u" * diff[1] + "rddlu" * (diff[1] - 1) + "rdl" + "urrdl" * (diff[0] - 1)
                elif diff[1] < 0:
                   string += "u" * abs(diff[0]) + "r" * diff[1] + "lddru" * (diff[0] - 1) + "ldr" + "ulldr" * (abs(diff[1]) -1) + "ulld"
                
                
        self.update_puzzle(string)
        #print string
        return  string

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        # move next tile to (target_row - 1, 1) above the 5

        #move_row = {-1: 'r', 1: 'l'}
        #move_col = {1: 'u', -1: 'd'}  
        
        string = ""
        value = target_row * self.get_width() 
            #print value 
        for dummy_row in range(0, target_row + 1):
            for dummy_col in range(0, self.get_width() ):
                if self.get_number(dummy_row, dummy_col) == value:
                   loc = (dummy_row, dummy_col) 
                   #print loc
        diff = [target_row - loc[0], 0 - loc[1]] 

        if diff == [1,0]:
            string = "u" * (self.get_width() -1 )
   
        else:
            string += "ur"
            tmp_loc = (target_row - 1, 1)
            tmp_diff = [tmp_loc[0] - loc[0], tmp_loc[1] - loc[1]] 
            #print tmp_loc
            #print tmp_diff
            #diff = [*, 0]
            if tmp_diff[1] == 0 :
                string += "u" * tmp_diff[0] + "rddlu" * (tmp_diff[0] - 1) + "ld"
            # if at the same col
            #diff = [0, *]
            elif tmp_diff[0] == 0 :                
                string += "l" * tmp_diff[1] + "urrdl" * (tmp_diff[1] - 1)
            # if  row > 0  and col > 0 
            elif tmp_diff[0] > 0:
                if tmp_diff[1] > 0:
                   string += "l" * diff[0] + "u" * diff[1] + "rddlu" * (diff[1] - 1) + "rdl" + "urrdl" * (diff[0] - 1)
                elif tmp_diff[1] < 0:
                   string += "r" * abs(tmp_diff[1]) + "u" * tmp_diff[0] + "lddru" * (tmp_diff[0] - 1) + "ldr" + "ulldr" * (abs(tmp_diff[1]) -1) + "ulld"
            string += "ruldrdlurdluurddlu" + "r" * (self.get_width() -1 )
        
        
        #print string
        self.update_puzzle(string)
        return string

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        output = False
        if self.get_number(0, target_col) == 0:
            output = True             
            for dummy_col in range(target_col + 1, self.get_width()):
                    output = self.get_number(0 , dummy_col) == dummy_col and output
            clone_obj = self.clone()
            if target_col > 0 :
               clone_obj.set_number(1, target_col - 1, 0)
               output = output and clone_obj.row1_invariant(target_col - 1)  
            elif target_col == 0 :
                output = self.lower_row_invariant(0, target_col)
                            
        return output

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        #output = False
        #if self.get_number(1, target_col) == 0:
            #output = True
            #for dummy_col in range(target_col + 1, self.get_width()):
            #        output = self.get_number(1 , dummy_col) == self.get_width() + dummy_col and output            
            #print output   
        #print self.lower_row_invariant(1, target_col)
        #return output
        return self.lower_row_invariant(1, target_col)

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        
        string = ""
        if self.row0_invariant(target_col):
            value = target_col
            #print value 
            for dummy_row in range(0, 1 + 1):
                for dummy_col in range(0, self.get_width() ):
                    if self.get_number(dummy_row, dummy_col) == value:
                        loc = (dummy_row, dummy_col)                    
                        #print loc        
        tmp_loc = [1 , target_col - 1]
        diff = [tmp_loc[0] - loc[0], tmp_loc[1] - loc[1]]
        #print diff
        if target_col - loc[1] == 1:
            string = "ld"
        else:
             string += "ld"
             if diff[1] == 0:
                    string = "u" + "ld"            
             elif diff[0] == 0:
                 string += "l" * diff[1] + "urrdl" * ( diff[1] - 1 )
             if diff[0] == 1:
                 string += "l" * diff[1] + "urdl" + "urrdl" * (diff[1] - 1)
             string += "urdlurrdluldrruld"
        
        self.update_puzzle(string)
        #print string
        return string

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        
        #string_1 = self.solve_interior_tile(1, target_col) + "urr"
        #self.update_puzzle(string_1)

        string = ""
        
        if self.row1_invariant(target_col):
            value = 1* self.get_width() + target_col
            #print value 
            for dummy_row in range(0, 1+ 1):
                for dummy_col in range(0, self.get_width() ):
                    if self.get_number(dummy_row, dummy_col) == value:
                        loc = (dummy_row, dummy_col)                    
                        #print loc                
        diff = [1 - loc[0], target_col - loc[1]]
        #print diff
        if diff[1] == 0:
            string += "u"
        elif diff[0] == 0:
            string += "l" * diff[1] + "urrdl" *(diff[1] - 1) + "ur"
        elif diff[0] > 0 :
            if diff[1] > 0:
               string += "u" + "l" * diff[1] + "drrul" * (diff[1] - 1) + "dru"

            
            
        self.update_puzzle(string)
        return string

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        
        if self.row1_invariant(1):
            clone_adj = self.clone()
            clone_adj.update_puzzle("ul")
            if clone_adj.get_number(0, 1) > clone_adj.get_number(1, 0):
                string = "uldrul"
            elif clone_adj.get_number(0, 1) < clone_adj.get_number(1, 0):
                string = "ulrdlu"
                
        self.update_puzzle(string)            
        return string

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        
        
        

        for dummy_row in range(0, self.get_height()):
                for dummy_col in range(0, self.get_width() ):
                    if self.get_number(dummy_row, dummy_col) == 0:
                        loc = (dummy_row, dummy_col) 
        diff = [self.get_height() - 1 - loc[0], self.get_width()- 1 - loc[1]]
        print diff
        string = "d" * diff[0] + "r" * diff[1]
        
        self.update_puzzle(string)
        print self
        for dummy_row in range(1, self.get_height() - 1):
            for dummy_col in range(1, self.get_width()):
                #obj = self.clone()
                string += self.solve_interior_tile(self.get_height() - dummy_row, self.get_width() - dummy_col)
                print self
            string += self.solve_col0_tile(self.get_height() - dummy_row)
            print self
        for dummy_col in range(1, self.get_width()-1 ):
            string += self.solve_row1_tile(self.get_width() - dummy_col)
            print self
            string += self.solve_row0_tile(self.get_width() - dummy_col)
            print self
               
        string += self.solve_2x2()         
        print self
        #self.update_puzzle(string)
        return string

# Start interactive simulation

#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))

#obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
#print obj.solve_interior_tile(2, 2) 

#obj = Puzzle(3, 3, [[3, 2, 1], [6, 5, 4], [7, 0, 8]])
#obj.solve_interior_tile(2, 1) 
#print obj

#obj = Puzzle(3, 3, [[3, 2, 1], [6, 5, 4], [0, 7, 8]])
#print obj.solve_col0_tile(2) 

#obj = Puzzle(4, 5, [[12, 11, 10, 9, 15], [7, 6, 5, 4, 3], [2, 1, 8, 13, 14], [0, 16, 17, 18, 19]])
#print obj.solve_col0_tile(3)
#print obj

#obj = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
#print obj.row1_invariant(1)

#obj = Puzzle(4, 5, [[15, 6, 5, 3, 4], [2, 1, 0, 8, 9], [10, 11, 12, 13, 14], [7, 16, 17, 18, 19]])
#print obj
#print obj.row1_invariant(2)

#obj = Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
#print obj
#print obj.row0_invariant(0) 

#obj = Puzzle(3, 3, [[3, 0, 2], [1, 4, 5], [6, 7, 8]])
#print obj
#print obj.row0_invariant(1)

#obj = Puzzle(4, 5, [[7, 2, 0, 3, 4], [5, 6, 1, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
#print obj
#print obj.row0_invariant(2)

#obj = Puzzle(3, 3, [[2, 5, 4], [1, 3, 0], [6, 7, 8]])
#print obj
#print obj.solve_row1_tile(2)
#print obj

#obj = Puzzle(4, 5, [[7, 6, 5, 3, 4], [2, 1, 0, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
#print obj
#print obj.solve_row1_tile(2) 
#print obj

#obj = Puzzle(4, 5, [[7, 6, 5, 3, 2], [4, 1, 9, 8, 0], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
#print obj
#print obj.solve_row1_tile(4)
#print obj

#obj = Puzzle(3, 3, [[4, 1, 0], [2, 3, 5], [6, 7, 8]])
#print obj
#print obj.solve_row0_tile(2)
#print obj

#obj = Puzzle(4, 5, [[1, 2, 0, 3, 4], [6, 5, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
#print obj
#print obj.solve_row0_tile(2)
#print obj

#obj = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
#print obj
#print obj.solve_2x2() 
#print obj

obj = Puzzle(3,3,[[4, 3, 2], [1, 0, 5], [6, 7, 8]])
print obj.solve_puzzle()