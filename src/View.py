import pygame
import time
from Button import Button

class View:
    
   
    def __init__(self, win, pygame) -> None:
        self.pygame = pygame
        self.win = win
        
        #make the buttons for start
        self.start_buttons = [Button((255,0,0), 250, 350, 200, 70, 50, "start game"), Button((255,0,0), 250, 450, 200, 70, 50, "quit game")]

    
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
                self.win.blit(replay2,(400/2,700/2))  
                
        
        elif(game_over is False):
            yellow = (255, 255, 0)
            #background color is white
            self.win.fill((255,255,255))

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

    def start_screen(self) -> None:

        start = True

        while start:
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:          
                    clicked = self.pygame.mouse.get_pos()
                    if self.start_buttons[0].is_over(clicked): #check the start game button
                        self.start_buttons[0].color = (0,0,255)
                        if self.pygame.mouse.get_pressed()[0]: #check for click
                            start = False
                            pygame.time.delay(100)
                    else:
                        self.start_buttons[0].color = (255,0,0)

                    if self.start_buttons[1].is_over(clicked): #check the quit game button
                        self.start_buttons[1].color = (0,0,255)
                        if self.pygame.mouse.get_pressed()[0]: #check for click
                            pygame.quit()
                            quit()
                    else:
                        self.start_buttons[1].color = (255,0,0)
                
            self.win.fill((255,255,255))
            # font sizes
            big_font = pygame.font.SysFont("Comic Sans", 120)
            sm_font = pygame.font.SysFont("Comic Sans", 50)
            
            # messages printed on start screen
            welcome = sm_font.render("Welcome to", True, (0,0,0))
            self.win.blit(welcome, (250,160))
            
            title = big_font.render("Line Up 4!", True, (0,0,0))
            self.win.blit(title, (150,225))

            for button in self.start_buttons:
                button.draw_button(self.win, True)

            self.pygame.display.update()

