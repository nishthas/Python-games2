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
    ale=len(line)
    result=[]
    for number in range(ale):
        result.append(0)
    inp=0
   
    for number in line:
        if number!=0:
            result[inp]=number
            inp+=1
    line =result 
    
    kin=0
    flag=False    
    if flag==False:
        for line[kin] in line:     
            if kin<ale-1:
                if line[kin]==line[kin+1]:
                    
                    inp=0
                    result=[]
                    for number in range(ale):
                        result.append(0)
                    line[kin]+=line[kin+1]
                    line[kin+1]=0
                    
                    
                    for number in line:
                        if number!=0:
                            result[inp]=number
                            inp+=1
                kin+=1
        flag=True
    return result


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.board=[]
        self.row=grid_height
        self.col=grid_width
        self.reset()
        self.dict={UP: [(0, 0), (0, 1), (0, 2), (0, 3)],
              DOWN: [(3, 0), (3, 1), (3, 2), (3, 3)], 
              LEFT: [(0, 0), (1, 0), (2, 0), (3, 0)],
              RIGHT: [(0, 3), (1, 3), (2, 3), (3, 3)]}
        
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        # replace with your code
        self.board = [ [0 for dummy_col in range(self.col)] for dummy_row in range(self.row)]
        
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self.board)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.row
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.col
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        
        self.old_grid = [list(inner_list) for inner_list in self.board]
        count=0
        if direction==UP or direction==DOWN:
            rof=0
            cof=1
        else:
            rof=1
            cof=0
        while count<self.row:
            row=0
            col=0
            temp=[]
            for number in self.dict[direction]:
                
                if direction==UP or direction==LEFT:
                    temp.append(self.board[row+count*rof][col+count*cof])
                row+=OFFSETS[direction][0]
                col+=OFFSETS[direction][1]
                if direction==DOWN or direction==RIGHT:
                    temp.append(self.board[row+count*rof][col+count*cof])
            print temp
            new=merge(temp)
            row=0
            col=0
            for number in new:
                if direction==UP or direction==LEFT:
                    self.board[row+count*rof][col+count*cof]=number
                row+=OFFSETS[direction][0]
                col+=OFFSETS[direction][1]
                if direction==DOWN or direction==RIGHT:
                    self.board[row+count*rof][col+count*cof]=number
            
            count+=1
        if self.board!=self.old_grid:
                self.new_tile()
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        number=random.randrange(0,10)
        xin=random.randrange(0,self.row)
        yin=random.randrange(0,self.col)
        if self.board[xin][yin]==0:
            if number<9:
                self.set_tile(xin,yin,2)
            else:
                self.set_tile(xin,yin,4)
        else:
            self.new_tile()
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        # replace with your code
        self.board[row][col]=value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        # replace with your code
        return self.board[row][col]
 
   
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
