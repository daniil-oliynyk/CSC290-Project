import pygame
pygame.init()

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

        #disk pointers
        self.top = None #probably don't need this
        self.bottom = None
        self.left = None
        self.right = None
        self.topleft = None
        self.topright = None
        self.bottomleft = None
        self.bottomright = None

    def get_set(self):
        return self.set

    def draw(self):
        #checks to see if the disk has fallen into its place
        if(self.y < (700 - (self.col + 1)*100)):
            self.y += 50 #moves disk down a little for the animation
        else:
            self.set = True

    def compare_colour(self, other) -> bool:
        """
        """
        return self.colour == other.colour

    def get_colour(self):
        return self.colour

    def setup(self, board: list) -> None:
        if self.row != 0:
            self.bottom = board[self.col][self.row - 1]
            if self.col != 0:
                self.bottomleft = board[self.col - 1][self.row - 1]
            if self.col != 6:
                self.bottomright = board[self.col + 1][self.row - 1]

        if self.col != 0:
            self.left = board[self.col - 1][self.row]
            if self.row != 5:
                self.topleft = board[self.col - 1][self.row + 1]

        if self.col != 6:
            self.right = board[self.col + 1][self.row]
            if self.row != 5:
                self.topright = board[self.col + 1][self.row + 1]


    
def find_row(column: list) -> int:
    """ return the row number at which to insert a disk"""
    i = column.count(None)
    return 6 - i

board = [[None, None, None, None, None, None],[None, None, None, None, None, None],\
         [None, None, None, None, None, None],[None, None, None, None, None, None],\
         [None, None, None, None, None, None],[None, None, None, None, None, None],\
         [None, None, None, None, None, None]]

if __name__ == '__main__':
    win = pygame.display.set_mode((700, 800))
    #the board has 7 columns and 6 rows
    #the current disk refers to the disk that has been dropped but is still falling in the animation
    curr_disk = None
    colour = (255,0,0)
    red = (255,0,0)
    blue = (0,0,255)

    run = True
    while run:
        pygame.time.delay(50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if(curr_disk == None): #checks to see if a disk has dropped but hasn't finished falling
            mouse_button_1 = pygame.mouse.get_pressed()[0] #checks if the player has clicked the left mouse button
            if mouse_button_1:
                mouse_pos_x = pygame.mouse.get_pos()[0]
                disk_pos_x = mouse_pos_x - (mouse_pos_x % 100) + 50 # rounds the position of the disk to match the board GUI
                col = (disk_pos_x//100) # the colomn index on the board list
                #print(col)
                #make Disk and add it to board
                
                row = find_row(board[col])
                if row < 6:
                    curr_disk = Disk(win, disk_pos_x, row, col, colour)
                    board[col][row] = curr_disk

        #background is a light blue
        win.fill((0,255,255))
        #vertical lines
        pygame.draw.line(win,(255,255,255), (100,100),(100,700))
        pygame.draw.line(win,(255,255,255), (200,100),(200,700))
        pygame.draw.line(win,(255,255,255), (300,100),(300,700))
        pygame.draw.line(win,(255,255,255), (400,100),(400,700))
        pygame.draw.line(win,(255,255,255), (500,100),(500,700))
        pygame.draw.line(win,(255,255,255), (600,100),(600,700))
        #horizontal lines
        pygame.draw.line(win,(255,255,255), (0,175), (700,175))
        pygame.draw.line(win,(255,255,255), (0,275), (700,275))
        pygame.draw.line(win,(255,255,255), (0,375), (700,375))
        pygame.draw.line(win,(255,255,255), (0,475), (700,475))
        pygame.draw.line(win,(255,255,255), (0,575), (700,575))

        for col in board:
            for disk in col:
                if disk != None:
                    disk.draw()

        #changes the colour of the next disk 
        if(colour == red):
            colour = blue
        else:
            colour = red
        curr_disk = None
        pygame.display.update()
    pygame.quit()


