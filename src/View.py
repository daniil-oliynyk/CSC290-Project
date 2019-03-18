import pygame
import time
from Button import Button

class View:
   
    def __init__(self, win, pygame) -> None:
        self.pygame = pygame
        self.win = win
        
        #make the buttons for start
        self.start_buttons = [Button((0,255,0), 250, 500, 200, 70, 50, "START"),
                              Button((255,0,0), 250, 600, 200, 70, 50, "QUIT"),
                              Button((0,0,255), 50, 50, 100, 60, 40, "HELP")]

    
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
            for i in range(7):
                self.pygame.draw.rect(self.win, yellow , pygame.Rect(80 + 100*i,80, 40, 600), 0)
            
            #horizontal lines
            self.pygame.draw.rect(self.win, yellow, pygame.Rect(0,70, 700, 30), 0)
            for i in range(6):
                self.pygame.draw.rect(self.win, yellow, pygame.Rect(0,160 + 100*i, 700, 40), 0)

            for i in range(6):
                for j in range(7):
                    #circle outlines
                    pygame.draw.circle(self.win, yellow, (100* j + 50, 100*i + 130), 30, 5)
                    #Triangles to fill in the gaps between the circles and rectangles
                    pygame.draw.polygon(self.win, yellow, [(100*j + 20, 100*i + 100),\
                                                            (100*j + 45, 100*i + 100), (100*j + 20, 100*i + 124)])
                    pygame.draw.polygon(self.win, yellow, [(100*j + 54, 100*i + 100),\
                                                            (100*j + 80, 100*i + 100), (100*j + 80, 100*i + 124)])
                    pygame.draw.polygon(self.win, yellow, [(100*j + 20, 100*i + 135),\
                                                            (100*j + 45, 100*i + 160), (100*j + 20, 100*i + 160)])
                    pygame.draw.polygon(self.win, yellow, [(100*j + 80, 100*i + 135),\
                                                            (100*j + 55, 100*i + 160), (100*j + 80, 100*i + 160)])


        self.pygame.display.update()
        
    def set_background(self, image):
        background = pygame.image.load(image).convert()
        self.win.blit(background, [0,0])
        
    def start_screen(self) -> None:

        start = True

        while start:
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:          
                    clicked = self.pygame.mouse.get_pos()
                    if self.start_buttons[0].is_over(clicked): #check the start game button
                        self.start_buttons[0].color = (25,171,14)
                        if self.pygame.mouse.get_pressed()[0]: #check for click
                            start = False
                            pygame.time.delay(100)
                    else:
                        self.start_buttons[0].color = (0,255,0)

                    if self.start_buttons[1].is_over(clicked): #check the quit game button
                        self.start_buttons[1].color = (162,20,20)
                        if self.pygame.mouse.get_pressed()[0]: #check for click
                            pygame.quit()
                            quit()
                    else:
                        self.start_buttons[1].color = (255,0,0)

                    if self.start_buttons[2].is_over(clicked): #check the help button
                        self.start_buttons[2].color = (13,25,82)
                        if self.pygame.mouse.get_pressed()[0]: #check for click
                            # help descriptions pop up
                            pygame.quit()
                            quit()
                    else:
                        self.start_buttons[2].color = (0,0,255)
                
            #self.win.fill((255,255,255))
            # font sizes
            big_font = pygame.font.Font("Consequences.ttf", 100)
            sm_font = pygame.font.Font("Consequences.ttf", 50)
            
            #pygame.display.flip()
            self.set_background("clouds.jpg")
            
            # messages printed on start screen
            welcome = sm_font.render("Welcome to", True, (0,0,0))
            self.win.blit(welcome, (150,230))
            
            title = big_font.render("Line Up 4!", True, (0,0,0))
            self.win.blit(title, (60,310))

            for button in self.start_buttons:
                button.draw_button(self.win, True)

            self.pygame.display.update()


