import pygame

class View:
    

    
   
    def __init__(self, win, pygame) -> None:
        self.pygame = pygame
        self.win = win
        

    
    def display(self, game_board,game_over, colour) -> None:
        """
        Display all the game board data on the pygame view.
        """
       

        if(game_over is True): #displays an end game screen when one of the playes has won 
            if (colour == (255,0,0)): #if red disk wins
                self.win.fill((255,0,0))
                font = pygame.font.SysFont("Comic Sans",75) #font used for Game Over and Red Disk Wins
                game_over_text = font.render("Game Over!",1,(255,255,255))
                self.win.blit(game_over_text, (420/2,500/2))
                p1 = font.render("Red Disk Wins!",1,(255,255,255))
                self.win.blit(p1,(335/2, 600/2)) #displays the text after rendering
                font2 = pygame.font.SysFont("Comic Sans",50) #different font needed because of smaller font size
                replay1 = font2.render("Press 'R' to Replay",1,(255,255,255))
                self.win.blit(replay1,(400/2,700/2))  
                
            elif (colour == (0,0,255)): #if blue disk wins
                #same as if red disk wins
                self.win.fill((0,0,255))
                font = pygame.font.SysFont("Comic Sans",75)
                text = font.render("Game Over!",1,(255,255,255))
                self.win.blit(text, (420/2,500/2))
                p2 = font.render("Blue Disk Wins!",1,(255,255,255))
                self.win.blit(p2,(335/2, 600/2))
                font2 = pygame.font.SysFont("Comic Sans",50)
                replay2 = font2.render("Press 'R' to Replay",1,(255,255,255))
                self.win.blit(replay2,(200/2,700/2))  
                
        
        elif(game_over is False):
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