import pygame
pygame.init()

class Disk:
    def __init__(self, win, x,board_x, board_y, colour):
        #
        self.x = x
        self.win = win
        self.y = 30
        self.board_x = board_x
        self.board_y = board_y
        #set keeps track of if the disk has "fallen" into place during the
        #animation
        self.set = False
        self.colour = colour
        #pygame.draw.circle(self.win, (255,0,0), (self.x,self.y), 30)
    def draw(self):
        if(self.y < (700 - (self.board_y + 1)*100)):
            self.y += 50
        else:
            self.set = True
        pygame.draw.circle(self.win, self.colour, (self.x,self.y), 30)
    def get_set(self):
        return self.set
    def get_colour(self):
        return self.colour
        

win = pygame.display.set_mode((700, 800))
max_h = 6
board = [[],[],[],[],[],[],[]]
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
    if(curr_disk == None):
        mouse_button_1 = pygame.mouse.get_pressed()[0] 
        if mouse_button_1:
            mouse_pos_x = pygame.mouse.get_pos()[0]
            disk_pos_x = mouse_pos_x - (mouse_pos_x % 100) + 50
            col = (disk_pos_x//100)
            #print(col)
            row = len(board[col])
            #print(row)
            if(row < max_h):
                curr_disk = Disk(win, disk_pos_x, col, row, colour)
                board[col].append(curr_disk)
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
            disk.draw()
        if(curr_disk != None and curr_disk.get_set()):
            curr_x = curr_disk.board_x
            curr_y = curr_disk.board_y
            curr_colour = curr_disk.get_colour()
            temp_x = curr_x
            temp_y = curr_y
            count = 0
            left = 0
            right = 0
            up = 0
            down = 0
            stay = True
            while left != 3 and stay:
                if(temp_x != 0):
                    temp_x -= 1
                    if(len(board[temp_x]) - 1  >= temp_y):
                        temp_disk = board[temp_x][temp_y]
                        if(temp_disk.get_colour() == curr_colour):
                            left += 1
                        else:
                            stay = False
                    else:
                        stay = False
                else:
                    stay = False
            if(left == 3):
                print("WIN!!!")
            else:
                remainder = 3 - left
                temp_x = curr_x
                stay = True
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
                if(left + right == 3):
                    print("WIN!!!")
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
                
            if(colour == red):
                colour = blue
            else:
                colour = red
            curr_disk = None
        

    pygame.display.update()
pygame.quit()
