"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = [] 
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        #self._zombie_list.append((row,col))
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombie in self._zombie_list:
            yield zombie
        return

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human
        return
        
    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        # Create a new grid visited of the same size as the original grid and initialize its cells to be empty.
        visited = self._cells
        # Create a 2D list distance_field of the same size as the original grid and initialize each of its entries to be the product of the height times the width of the grid. (This value is larger than any possible distance.)
        height = self.get_grid_height()
        width  = self.get_grid_width() 
        init_number = height * width
        distance_field = [[ init_number for dummy_col in range(width)] 
                       for dummy_row in range(height)]
        #Create a queue boundary that is a copy of either the zombie list or the human list. For cells in the queue, initialize visited to be FULL and distance_field to be zero. We recommend that you use our Queue class.
        #entity_type : zombie; human 
        boundary  = poc_queue.Queue()
        if entity_type == "zombie":
            for dummy in self._zombie_list:
                boundary.enqueue(dummy)
                visited[dummy[0]][dummy[1]] = 1
                distance_field[dummy[0]][dummy[1]] = 0
                

        if entity_type == "human":
            for dummy in self._human_list:
                boundary.enqueue(dummy)
                visited[dummy[0]][dummy[1]] = 1
                distance_field[dummy[0]][dummy[1]] = 0     
        
        while min(min(visited)) == 0:
          cell = boundary.dequeue()
          neighbors = self.four_neighbors(cell[0], cell[1])
        #neighbors = self.eight_neighbors(cell[0], cell[1])
          for neighbor in neighbors:
             if visited[neighbor[0]][ neighbor[1]] == 0:
                visited[neighbor[0]][ neighbor[1]] = 1  
                distance_field[neighbor[0]][neighbor[1]] = min(distance_field[neighbor[0]][neighbor[1]], distance_field[cell[0]][cell[1]] + 1)
                boundary.enqueue(neighbor) 
                
        print distance_field
        return distance_field     

    
    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        new_list = []
        for dummy in self._human_list:
          neighbors = self.eight_neighbors(dummy[0], dummy[1])  
          dis = zombie_distance[dummy[0]][dummy[1]]
          loc = dummy            
          for neighbor in neighbors:
                if zombie_distance[neighbor[0]][neighbor[1]] > dis:
                    dis = zombie_distance[neighbor[0]][neighbor[1]]
                    loc = neighbor
          new_list.append(loc)
        self._human_list = new_list
                    
                    
            
        print zombie_distance
    
    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        new_list = []
        for dummy in self._human_list:
          neighbors = self.four_neighbors(dummy[0], dummy[1]) 
          dis = human_distance[dummy[0]][dummy[1]]
          loc = dummy
          for neighbor in neighbors:
                if human_distance[neighbor[0]][neighbor[1]] < dis:
                    dis = human_distance[neighbor[0]][neighbor[1]]
                    loc = neighbor
          new_list.append(loc)
        self._zombie_list = new_list

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Zombie(30, 40))

#import user35_EPZOWWGoUeaEemm as test
#test.phase1_test(Zombie)
#test.phase2_test(Zombie)
#test.phase3_test(Zombie)
