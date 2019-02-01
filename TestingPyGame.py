import pygame
pygame.init()

class Disk:
    def __init__(self, win, x,board_x, board_y, colour):
        # x position on the screen
        self.x = x
        self.win = win #surface for pygame
        self.y = 30 #each disk starts at the top
        self.board_x = board_x #colomn index on the board list
        self.board_y = board_y #row index on the board list
        #set keeps track of if the disk has "fallen" into place during the
        #animation
        self.set = False
        self.colour = colour
        #pygame.draw.circle(self.win, (255,0,0), (self.x,self.y), 30)
    def draw(self):
        #checks to see if the disk has fallen into its place
        if(self.y < (700 - (self.board_y + 1)*100)):
            self.y += 50 #moves disk down a little for the animation
        else:
            self.set = True
        pygame.draw.circle(self.win, self.colour, (self.x,self.y), 30)
    def get_set(self):
        return self.set
    def get_colour(self):
        return self.colour
        

win = pygame.display.set_mode((700, 800))
#the board has 7 columns and 6 rows
max_h = 6
board = [[],[],[],[],[],[],[]]
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
            row = len(board[col]) # the row index on the board kust
            #print(row)
            if(row < max_h):
                curr_disk = Disk(win, disk_pos_x, col, row, colour)
                board[col].append(curr_disk)
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

    #draws each disk in the board list
    for col in board:
        for disk in col:
            disk.draw()
        if(curr_disk != None and curr_disk.get_set()):
            #keeps track of the current disk's indexes on the board list
            curr_x = curr_disk.board_x
            curr_y = curr_disk.board_y
            curr_colour = curr_disk.get_colour()
            #temporay positions that change to traverse through the rest of the board
            temp_x = curr_x
            temp_y = curr_y
            count = 0
            #horizontal
            left = 0
            right = 0
            #vertical
            up = 0
            down = 0
            #first diagonal
            top_left = 0
            bottom_right = 0
            #second diagonal
            top_right = 0
            bottom_left = 0
            #I should have used break statement to exit the while loops
            stay = True
            #horizontal traversal
            while left != 3 and stay:
                if(temp_x != 0): #prevents the coordinates from going out of bounds
                    temp_x -= 1
                    if(len(board[temp_x]) - 1  >= temp_y):#checks if the left colomn has disks at the same row as temp_y
                        temp_disk = board[temp_x][temp_y]
                        if(temp_disk.get_colour() == curr_colour):# if left disk has the same colour as the current disk, add 1 to left
                            left += 1
                        else:
                            stay = False
                    else:
                        stay = False
                else:
                    stay = False
            if(left == 3):# if the left side has 3 of the same disks, then including itself that makes 4
                print("WIN!!!")
            else:
                remainder = 3 - left# the remainder is for how many disks are needed for the right side to make four all together 
                temp_x = curr_x #resets the temp_x position 
                stay = True
                #most of the main logic is the same for each traversal, just with different changes to the coords 
                while right != remainder and stay:
                    if(temp_x != 6):
                        temp_x += 1
                        if(len(board[temp_x]) - 1  >= temp_y):
                            temp_disk = board[temp_x][temp_y]
                            if(temp_disk.get_colour() == curr_colour):
                                right += 1
                            else:
                                stay = False
                        else:
                            stay = False
                    else:
                        stay = False
                #checks if the current disk has 3 same coloured disks beside it in the horizontal direction(4 including itself)
                if(left + right == 3):
                    print("WIN!!!")
            #vertical traversal
            temp_x = curr_x
            stay = True
            while down != 3 and stay:
                if(temp_y != 0):
                    temp_y -= 1
                    #if(len(board[temp_x]) - 1  >= temp_y):
                    temp_disk = board[temp_x][temp_y]
                    if(temp_disk.get_colour() == curr_colour):
                        down += 1
                    else:
                        stay = False
                    #else:
                     #   stay = False
                else:
                    stay = False
            if(down == 3):
                print("WIN!!!")
            else:
                remainder = 3 - down
                temp_y = curr_y
                stay = True
                while up != remainder and stay:
                    if(temp_y != len(board[temp_x]) - 1):
                        temp_y += 1
                        #if(len(board[temp_x]) - 1  >= temp_y):
                        temp_disk = board[temp_x][temp_y]
                        if(temp_disk.get_colour() == curr_colour):
                            up += 1
                        else:
                            stay = False
                        #else:
                            #stay = False
                    else:
                        stay = False
                if(up + down == 3):
                    print("WIN!!!")
            #first diagonal traversal
            temp_x = curr_x
            temp_y = curr_y
            stay = True
            while top_left != 3 and stay:
                if(temp_x != 0 and temp_y != max_h - 1):# prevents going out of bounds in either direction
                    temp_x -= 1 #changes both the vertical and horizontal coords to travers diagonally 
                    temp_y += 1
                    if( len(board[temp_x]) - 1 >= temp_y):
                        temp_disk = board[temp_x][temp_y]
                        if (temp_disk.get_colour() == curr_colour):
                            top_left += 1
                        else:
                            stay = False
                    else:
                        stay = False
                else:
                    stay = False
            if top_left == 3:
                print("WIN!!!")
            else:
                remainder = 3 - top_left
                temp_x = curr_x
                temp_y = curr_y
                stay = True
                while bottom_right != remainder and stay:
                    if(temp_x != 6 and temp_y != 0):
                        temp_x += 1
                        temp_y -= 1
                        if( len(board[temp_x]) - 1 >= temp_y):
                            temp_disk = board[temp_x][temp_y]
                            if (temp_disk.get_colour() == curr_colour):
                                bottom_right += 1
                            else:
                                stay = False
                        else:
                            stay = False
                    else:
                        stay = False
                if top_left + bottom_right == 3:
                    print("WIN!!!")
            #second diaognal traversal
            temp_x = curr_x
            temp_y = curr_y
            stay = True
            while top_right != 3 and stay:
                if(temp_x != 6 and temp_y != max_h - 1):
                    temp_x += 1
                    temp_y += 1
                    if( len(board[temp_x]) - 1 >= temp_y):
                        temp_disk = board[temp_x][temp_y]
                        if (temp_disk.get_colour() == curr_colour):
                            top_right += 1
                        else:
                            stay = False
                    else:
                        stay = False
                else:
                    stay = False
            if top_right == 3:
                print("WIN!!!")
            else:
                remainder = 3 - top_right
                temp_x = curr_x
                temp_y = curr_y
                stay = True
                while bottom_left != remainder and stay:
                    if(temp_x != 0 and temp_y != 0):
                        temp_x -= 1
                        temp_y -= 1
                        if( len(board[temp_x]) - 1 >= temp_y):
                            temp_disk = board[temp_x][temp_y]
                            if (temp_disk.get_colour() == curr_colour):
                                bottom_left += 1
                            else:
                                stay = False
                        else:
                            stay = False
                    else:
                        stay = False
                if top_right + bottom_left == 3:
                    print("WIN!!!")
            #changes the colour of the next disk 
            if(colour == red):
                colour = blue
            else:
                colour = red
            curr_disk = None
        
        

    pygame.display.update()
pygame.quit()
