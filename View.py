import pygame

class View:
    
    def __init__(self, win, pygame) -> None:
        self.pygame = pygame
        self.win = win
        
    def display(self, game_board) -> None:
        """
        Display all the game board data on the pygame view.
        """
        #background is a light blue
        self.win.fill((0,255,255))
        #vertical lines
        self.pygame.draw.line(self.win,(255,255,255), (100,100),(100,700))
        self.pygame.draw.line(self.win,(255,255,255), (200,100),(200,700))
        self.pygame.draw.line(self.win,(255,255,255), (300,100),(300,700))
        self.pygame.draw.line(self.win,(255,255,255), (400,100),(400,700))
        self.pygame.draw.line(self.win,(255,255,255), (500,100),(500,700))
        self.pygame.draw.line(self.win,(255,255,255), (600,100),(600,700))
        #horizontal lines
        self.pygame.draw.line(self.win,(255,255,255), (0,175), (700,175))
        self.pygame.draw.line(self.win,(255,255,255), (0,275), (700,275))
        self.pygame.draw.line(self.win,(255,255,255), (0,375), (700,375))
        self.pygame.draw.line(self.win,(255,255,255), (0,475), (700,475))
        self.pygame.draw.line(self.win,(255,255,255), (0,575), (700,575))
    
        #Draw all the disks from the board on the pygame view
        for col in game_board:
            for disk in col:
                if disk != None:
                    disk.draw()
        
        self.pygame.display.update()