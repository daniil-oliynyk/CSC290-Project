from Disk import Disk

red = (255,0,0)
blue = (0,0,255)
  
def find_row(column: list) -> int:
    """ 
    Return the row number at which to insert the new disk.
    """
    level = column.count(None)
    return 6 - level

class Model:
       
    
    def __init__(self, win, game_view, game_controller) -> None:        
        
        self.win = win
        self.game_view = game_view
        self.game_controller = game_controller
        self.curr_disk = None
        self.curr_colour = red
        self.game_board = [[None, None, None, None, None, None],[None, None, None, None, None, None],\
                           [None, None, None, None, None, None],[None, None, None, None, None, None],\
                           [None, None, None, None, None, None],[None, None, None, None, None, None],\
                           [None, None, None, None, None, None]]
        
    



    def restart_model(self) -> None:
        """
        Restarts the model to the default
        """
        print("restarting model")
        self.curr_disk = None
        self.curr_colour = red
        self.game_board = [[None, None, None, None, None, None],[None, None, None, None, None, None],\
                           [None, None, None, None, None, None],[None, None, None, None, None, None],\
                           [None, None, None, None, None, None],[None, None, None, None, None, None],\
                           [None, None, None, None, None, None]]
   

    def update_view(self,game_over) -> None:
        """
        Send the game view the game board to display.
        """
        self.game_view.display(self.game_board,game_over,self.curr_colour,self.game_controller)
        
    def get_colour(self):
        return self.curr_colour

    def change_colour(self) -> None:
        """
        Changes the current colour between red and blue to alternate between players.
        Also sets the current disk to None if a switch is made.
        """
        if(self.curr_disk != None and self.curr_disk.get_set()):
            if(self.curr_colour == red):
                self.curr_colour = blue
            else:
                self.curr_colour = red
            self.curr_disk = None
            
    def add_disk(self, disk_pos_x) -> bool:
        """
        Add new disk to the game board using the position of the mouse click.
        Then check if that new disk has won the game.
        """
        col = (disk_pos_x//100) # the colomn index on the board list
        row = find_row(self.game_board[col]) #find the first non empty row in the given column
        
        if row < 6:
            self.curr_disk = Disk(self.win, disk_pos_x, row, col, self.curr_colour) #create disk object
            self.game_board[col][row] = self.curr_disk #insert disk in the proper location on the board
            self.curr_disk.set_up_disk(self.game_board) #connect the disk to all surrounding disks on the board
            if (self.curr_disk.check_win()): #check if the disk has won the game
                return True
            return False
        return False    