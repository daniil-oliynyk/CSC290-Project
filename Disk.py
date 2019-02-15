import pygame

class Disk:
    
    def __init__(self, win, x, row: int, col: int, colour) -> None:
        # x position on the screen
        self.x = x
        self.y = 30 #each disk starts at the top
        self.win = win #surface for pygame
        self.set = False
        
        #initialize the disk object
        self.row = row
        self.col = col
        self.colour = colour

        #pointers to other disks that surround the disk
        self.bottom = None
        self.left = None
        self.right = None
        self.topleft = None
        self.topright = None
        self.bottomleft = None
        self.bottomright = None


    """
    Recursively iterates in a given direction from the disk and
    return the number of consecutive disks of same color found.
    """
    def check_bottom(self) -> int:
        if self.bottom == None or self.compare_colour(self.bottom):
            return 1
        return 1 + self.bottom.check_bottom()

    def check_left(self) -> int:
        if self.left == None or self.compare_colour(self.left):
            return 1
        return 1 + self.left.check_left()

    def check_right(self) -> int:
        if self.right == None or self.compare_colour(self.right):
            return 1
        return 1 + self.right.check_right()

    def check_topleft(self) -> int:
        if self.topleft == None or self.compare_colour(self.topleft):
            return 1
        return 1 + self.topleft.check_topleft()

    def check_topright(self) -> int:
        if self.topright == None or self.compare_colour(self.topright):
            return 1
        return 1 + self.topright.check_topright()

    def check_bottomleft(self) -> int:
        if self.bottomleft == None or self.compare_colour(self.bottomleft):
            return 1
        return 1 + self.bottomleft.check_bottomleft()

    def check_bottomright(self) -> int:
        if self.bottomright == None or self.compare_colour(self.bottomright):
            return 1
        return 1 + self.bottomright.check_bottomright()


    def check_win(self) -> bool:
        """
        return true, iff the disk points to 3 or more other disks in a row.
        ie. The player wins the game
        """
        #print("vertical amt: " + str(self.check_bottom()))
        #print("horizontal amt :" + str(self.check_left() + self.check_right() - 1))
        #print("upper diagonal amt :" + str(self.check_topright() + self.check_bottomleft() - 1))
        #print("lower diagonal amt :" + str(self.check_topleft() + self.check_bottomright() - 1))
        if self.check_bottom() >= 4: #checks the vertical
            return True
        if (self.check_left() + self.check_right() - 1) >= 4: #checks horizontally
            return True
        if (self.check_topright() + self.check_bottomleft() - 1) >= 4: #checks upper diagonal
            return True
        if (self.check_topleft() + self.check_bottomright() - 1) >= 4: #checks lower diagonal
            return True
        return False     

    def get_set(self):
        return self.set

    def draw(self):
        #checks to see if the disk has fallen into its place
        if(self.y < (700 - (self.row + 1)*100)):
            self.y += 50 #moves disk down a little for the animation
        else:
            self.set = True
        pygame.draw.circle(self.win, self.colour, (self.x,self.y), 30)

    def compare_colour(self, other) -> bool:
        #returns true if they are not the same colour
        return self.colour != other.colour

    def get_colour(self):
        return self.colour

    def attach_disk(self, col, row, board: list):
        """
        check if given index exists on the board, if it does
        return that value. if it doesnt return None.
        """
        if row == -1 or col == -1 or row == 6 or col == 7: #checking the boarders of the board
            return None
        else:
            return board[col][row]

    def set_up_disk(self, board: list) -> None:
        """
        Get the disk to point to the disks surrounding it on the board.
        Also gets the surrounding disks to point to the eee/new disk.
        """
        self.bottom = self.attach_disk(self.col, self.row - 1, board) #Disk points to whatever is below
        
        self.left = self.attach_disk(self.col - 1, self.row, board) #Disk points to whatever is to the left
        if self.left!= None:
            board[self.col - 1][self.row].right = self #Disk at left points at current Disk
            
        self.right = self.attach_disk(self.col + 1, self.row, board) #Disk points to whatever is to the right
        if self.right != None:
            board[self.col + 1][self.row].left = self #Disk at right points at current Disk
            
        self.topleft = self.attach_disk(self.col - 1, self.row + 1, board) #Disk points to whatever is to the topleft
        if self.topleft != None:
            board[self.col - 1][self.row + 1].bottomright = self #Disk at topleft points at current Disk
            
        self.topright = self.attach_disk(self.col + 1, self.row + 1, board) #Disk points to whatever is to the topright
        if self.topright != None:
            board[self.col + 1][self.row].bottomleft = self #Disk at topright points at current Disk
            
        self.bottomleft = self.attach_disk(self.col - 1, self.row - 1, board) #Disk points to whatever is to the bottomleft
        if self.bottomleft != None:
            board[self.col - 1][self.row - 1].topright = self #Disk at bottomleft points at current Disk
            
        self.bottomright = self.attach_disk(self.col + 1, self.row - 1, board) #Disk points to whatever is to the bottomright
        if self.bottomright != None:
            board[self.col + 1][self.row - 1].topleft = self #Disk at bottomright points at current Disk


