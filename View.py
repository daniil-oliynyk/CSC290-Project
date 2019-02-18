import pygame

class View:
    
    def __init__(self, win, pygame) -> None:
        self.pygame = pygame
        self.win = win
        
    def display(self, game_board) -> None:
        """
        Display all the game board data on the pygame view.
        """
        yellow = (255, 255, 0)
        #background is a light blue
        self.win.fill((0,255,255))

        #Draw all the disks from the board on the pygame view
        for col in game_board:
            for disk in col:
                if disk != None:
                    disk.draw()

        
        #graphics for the connect four gameboard            
        #vertical lines
        self.pygame.draw.rect(self.win, yellow , pygame.Rect(0,80, 20, 600), 0)
        self.pygame.draw.rect(self.win, yellow , pygame.Rect(80,80, 40, 600), 0)
        #self.pygame.draw.line(self.win,(255,255,255), (100,100),(100,700))
        self.pygame.draw.rect(self.win, yellow, pygame.Rect(180,80, 40, 600), 0)
        #self.pygame.draw.line(self.win,(255,255,255), (200,100),(200,700))
        self.pygame.draw.rect(self.win, yellow, pygame.Rect(280,80, 40, 600), 0)
        #self.pygame.draw.line(self.win,(255,255,255), (300,100),(300,700))
        self.pygame.draw.rect(self.win, yellow, pygame.Rect(380,80, 40, 600), 0)
        #self.pygame.draw.line(self.win,(255,255,255), (400,100),(400,700))
        self.pygame.draw.rect(self.win, yellow, pygame.Rect(480,80, 40, 600), 0)
        #self.pygame.draw.line(self.win,(255,255,255), (500,100),(500,700))
        self.pygame.draw.rect(self.win, yellow, pygame.Rect(580,80, 40, 600), 0)
        #self.pygame.draw.line(self.win,(255,255,255), (600,100),(600,700))
        self.pygame.draw.rect(self.win, yellow, pygame.Rect(680,80, 40, 600), 0)

        #horizontal lines

        self.pygame.draw.rect(self.win, yellow, pygame.Rect(0,70, 700, 30), 0)
        self.pygame.draw.rect(self.win, yellow, pygame.Rect(0,160, 700, 40), 0)
        #self.pygame.draw.line(self.win,(255,255,255), (0,170), (700,175))
        self.pygame.draw.rect(self.win, yellow, pygame.Rect(0,260, 700, 40), 0)
        #self.pygame.draw.line(self.win,(255,255,255), (0,270), (700,275))
        self.pygame.draw.rect(self.win, yellow, pygame.Rect(0,360, 700, 40), 0)
        #self.pygame.draw.line(self.win,(255,255,255), (0,370), (700,375))
        self.pygame.draw.rect(self.win, yellow, pygame.Rect(0,460, 700, 40), 0)
        #self.pygame.draw.line(self.win,(255,255,255), (0,475), (700,475))
        self.pygame.draw.rect(self.win, yellow, pygame.Rect(0,560, 700, 40), 0)
        #self.pygame.draw.line(self.win,(255,255,255), (0,575), (700,575))
        self.pygame.draw.rect(self.win, yellow, pygame.Rect(0,660, 700, 30), 0)

        #circles
        for i in range(6):
            for j in range(7):
                pygame.draw.circle(self.win, yellow, (100* j + 50, 100*i + 130), 30, 5)
        #pygame.draw.circle(self.win, yellow, (450, 530), 30, 5)
        #Triangles to fill in the gaps between the circls and rectangles
        for i in range(6):
            for j in range(7):
                pygame.draw.polygon(self.win, yellow, [(100*j + 20, 100*i + 100),\
                                                        (100*j + 45, 100*i + 100), (100*j + 20, 100*i + 124)])
        for i in range(6):
            for j in range(7):
                pygame.draw.polygon(self.win, yellow, [(100*j + 54, 100*i + 100),\
                                                        (100*j + 80, 100*i + 100), (100*j + 80, 100*i + 124)])
        for i in range(6):
            for j in range(7):
                pygame.draw.polygon(self.win, yellow, [(100*j + 20, 100*i + 135),\
                                                        (100*j + 45, 100*i + 160), (100*j + 20, 100*i + 160)])
        for i in range(6):
            for j in range(7):
                pygame.draw.polygon(self.win, yellow, [(100*j + 80, 100*i + 135),\
                                                        (100*j + 55, 100*i + 160), (100*j + 80, 100*i + 160)])
    
        
        self.pygame.display.update()
