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
        flag3=False
        flag=False
        hig=self.get_height()
        wid=self.get_width()
        flag=self.help_invariant(target_row, target_col)
        if self.get_number(hig-1, wid-1)==0:
            if target_row==hig-1 and target_col==wid-1:
                flag3=True
        if ((self.get_number(target_row, target_col)==0) and flag) or flag3:
            return True
        else:
            return False

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # replace with your code
        assert self.lower_row_invariant(target_row, target_col), " assertion error lower row invariant"
        tup=self.current_position(target_row, target_col)
        tilerow=tup[0]
        tilecol=tup[1]
        stri=self.helper_fun(target_row, target_col,tilerow,tilecol)
        assert self.lower_row_invariant(target_row, target_col-1), " assertion error lower row invariant"
        return stri
            
        
    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        assert self.lower_row_invariant(target_row,0), " assertion error lower row invariant"
        stri='ur'
        self.update_puzzle(stri)
        wid=self.get_width()
        if self.current_position(target_row,0)==(target_row,0):
            adr='r'*(wid-2)
            stri+=adr
            self.update_puzzle(adr)
            return stri
        else:
            tup=self.current_position(target_row, 0)
            tilerow=tup[0]
            tilecol=tup[1]
            stri+=self.helper_fun(target_row-1,1,tilerow,tilecol)
            stri+='ruldrdlurdluurddlur'+'r'*(wid-2)
            self.update_puzzle('ruldrdlurdluurddlur'+'r'*(wid-2))
            assert self.lower_row_invariant(target_row-1,wid-1), " assertion error lower row invariant"
            return stri

    def helper_fun(self,target_row, target_col,tilerow,tilecol):
        """helper fun gets the tile in form of 0,val"""
        stri=self.zero_up(target_row, target_col,tilerow,tilecol)
        difr=target_row-tilerow
        if difr>1 or self.lower_row_invariant(target_row, target_col)!=True:#get zero at side
            stri+='lddru'*(difr-1)
            stri+='ld'
        elif difr<2 and self.lower_row_invariant(target_row, target_col)==True:
            #stri+='lddru'*(difr)
            stri+='ld'
        self.update_puzzle(stri)
        return stri
    
    def zero_up(self,target_row, target_col,tilerow,tilecol):
        """gets zero up to the target"""
        stri=""
        difr=target_row-tilerow
        difc=tilecol-target_col
        if tilecol!=target_col:#get zero in same row
            if target_row!=tilerow:
                stri='u'*(difr)
            if difc>0:
                stri+='r'*difc#zero to rt
            else:
                stri+='l'*(-difc)#zero to left
        else:
            if target_row!=tilerow:
                stri='u'*(difr)
        if difc>1 or difc<0:#get tile in same col
            if difr>1:
                if difc>0:
                    stri+='dllur'*(difc-1)#zero to rt
                else:
                    stri+='drrul'*(-difc-1)#zero to left
            elif difr==0:
                if difc<0:
                    stri+='urrdl'*(-difc-1)
                    stri+='ur'
            else:#wehn moving down not possible
                if difc>0:
                    stri+='ulldr'*(difc-1)#zero rt
                else:
                    stri+='drrul'*(-difc-1)
        if difc>0:#get zero up
                if difr>1 or self.lower_row_invariant(target_row, target_col)!=True:
                    stri+='dlu'
                else:
                    stri+='ul'
        elif difc<0:
                if difr>0:
                    stri+='dru'
        return stri
    
    def help_invariant(self,target_row, target_col):
        """row invariant helper"""
        flag1=True
        flag2=True
        hig=self.get_height()
        wid=self.get_width()
        ind=target_row+1
        while ind<hig and flag1:
            for num in range(wid):
                if self.get_number(ind,num)!=num+wid*ind:
                        flag1=False
            ind+=1
        for num in range(target_col+1,wid):
            if self.get_number(target_row,num)!=num+wid*target_row:
                flag2=False
        if flag1 and flag2:
            return True
        else:
            return False
    #############################################################
    # Phase two methods
    def row_help(self,target_col,wid):
        """helper row"""
        flag=True
        for num in range(target_col+1,wid):
            if self.get_number(0,num)!=num:
                flag=False
        return flag       
    
    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        wid=self.get_width()
        flag=self.help_invariant(1,target_col)
        flag1=self.row_help(target_col,wid)
        if self.get_number(0,target_col)==0 and (self.get_number(1,target_col)==target_col+wid) and flag and flag1:
            return True
        else:
            return False
        

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        wid=self.get_width()
        flag=self.row_help(target_col,wid)
        if self.lower_row_invariant(1, target_col) and flag:
            return True
        else:
            return False
    
    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        assert self.row0_invariant(target_col),"assertion error row0 invariant"
        stri="ld"
        self.update_puzzle(stri)
        if self.current_position(0,target_col)==(0,target_col):
            return stri
        else:
            tup=self.current_position(0, target_col)
            tilerow=tup[0]
            tilecol=tup[1]
            stri+=self.helper_fun(1,target_col-1,tilerow,tilecol)
            self.update_puzzle("urdlurrdluldrruld")
            stri+="urdlurrdluldrruld"
            assert self.row1_invariant(target_col-1),"assertion error row0 invariant"
            return stri

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        assert self.row1_invariant(target_col),"assertion error row1 invariant"
        tup=self.current_position(1, target_col)
        tilerow=tup[0]
        tilecol=tup[1]
        stri=self.zero_up(1, target_col,tilerow,tilecol)
        self.update_puzzle(stri)
        assert self.row0_invariant(target_col),"assertion error row0 invariant"
        return stri
        

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        assert self.row1_invariant(1),"assert row1 invariant error"
        stri="lu"
        self.update_puzzle(stri)
        wid=self.get_width()
        while (self.get_number(0,0)!=0 or self.get_number(0,1)!=1 or self.get_number(1,0)!=wid or self.get_number(1,1)!=1+wid):
                stri+="rdlu"
                self.update_puzzle("rdlu")
        return stri

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        #flag=True
        stri=""
        hig=self.get_height()
        wid=self.get_width()
        for row in range(hig):
            for col in range(wid):
                if self._grid[row][col] == 0:
                        zert= (row, col)
        stri='r'*(wid-zert[1]-1)
        stri+='d'*(hig-1-zert[0])
        print stri
        self.update_puzzle(stri)
        curh=hig-1
        while curh>1:
            curw=wid-1
            while curw!=0:
                stri+=self.solve_interior_tile(curh, curw)
                curw-=1
            stri+=self.solve_col0_tile(curh)
            curh-=1
        curw=wid-1
        while curw!=1:
            stri+=self.solve_row1_tile(curw)
            stri+=self.solve_row0_tile(curw)
            curw-=1
        stri+=self.solve_2x2()
        return stri
            
        

# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4,4,[[5,6,8,7],[3,1,9,4],[2,0,10,11],[12,13,14,15]]))
#obj = Puzzle(4, 4, [[8, 7, 6,1], [5, 4, 3,2], [0, 9, 10,11],[12,13,14,15]])

#obj = Puzzle(3, 6, [[16, 7, 13, 17, 5, 9], [3, 0, 14, 10, 12, 6], [4, 15, 2, 11, 8, 1]])
#poc_fifteen_gui.FifteenGUI(obj)
#obj.solve_puzzle()
#obj.solve_interior_tile(2, 1)
#obj.solve_col0_tile(2)
#
#obj.solve_puzzle()
#obj = Puzzle(4, 5, [[8, 2, 10, 9, 1], [7, 6, 5, 4, 3], [0, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
#obj.solve_col0_tile(2) 
