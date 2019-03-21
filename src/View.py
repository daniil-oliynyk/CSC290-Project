import pygame
import time
from Button import Button
import sys

class View:
   
    def __init__(self, win, pygame) -> None:
        self.pygame = pygame
        self.win = win
        
        #make the buttons for start
        self.start_buttons = [Button((0,255,0), 250, 500, 200, 70, 50, "START"),
                              Button((255,0,0), 250, 600, 200, 70, 50, "QUIT"),
                              Button((0,0,255), 50, 50, 100, 60, 40, "HELP")]


        self.end_button = Button((0,255,0),  250, 500, 200, 60, 30, "RETURN TO MAIN")

        #create return to main button for help screen
        self.back_button = Button((255,0,0), 30, 30, 200, 60, 30, "RETURN TO MAIN")
    
    def time_delay(self):
        """
        Method used to delay time by 50 milliseconds
        """
        self.pygame.time.delay(50)

    def display(self, game_board,game_over, colour, game_controller) -> None:
        """
        Display all the game board data on the pygame view.
        """
        if game_over is True:
            while game_over is True: #displays an end game screen when one of the playes has won 
                
                self.set_background("images/end_background.jpg")
                self.end_button.draw_button(self.win, True) 
                
                for event in pygame.event.get():            
                    if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:          
                        clicked = self.pygame.mouse.get_pos()
                        if self.end_button.is_over(clicked): #check the start game button
                            self.end_button.color = (25,171,14)
                            if self.pygame.mouse.get_pressed()[0]: #check for click
                                game_over = False
                                self.start_screen()
                        else:
                            self.end_button.color = (0,255,0)                     
                
    
                if (colour == (255,0,0) and game_over is True): #if red disk wins
                    
                    font = pygame.font.Font("Consequences.ttf",60) #font used for Game Over and Red Disk Wins
                    
                    game_over_text = font.render("Game Over!",1,(255,255,255))
                    self.win.blit(game_over_text, (150,190))
                    p1 = font.render("Red", 1, (255,0,0))
                    self.win.blit(p1,(80,260))
                    p2 = font.render("Disk Wins!",1,(255,255,255))
                    self.win.blit(p2,(235, 260)) #displays the text after rendering
                     
                elif (colour == (0,0,255) and game_over is True): #if blue disk wins
                    
                    font = pygame.font.Font("Consequences.ttf",60)
                    
                    text = font.render("Game Over!",1,(255,255,255))
                    self.win.blit(text, (150,190))
                    p1 = font.render("Blue",1,(0,0,255))
                    self.win.blit(p1,(80,260))
                    p2 = font.render("Disk Wins!",1,(255,255,255))
                    self.win.blit(p2,(280, 260))
                    
                self.pygame.display.update()
        
        else: #display the game_board
            
            yellow = (255, 255, 0)
            #background color is white
            self.win.fill((255,255,255))

            #Draw all the disks from the board on the pygame view
            for col in game_board:
                for disk in col:
                    if disk != None:
                        disk.draw()
                        
            x_coordinate = self.pygame.mouse.get_pos()[0]
            self.pygame.draw.circle(self.win, colour, (x_coordinate, 30), 30)            

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
        """
        Sets the background to the image provided as an argument
        """
        background = pygame.image.load(image).convert()
        self.win.blit(background, [0,0])
        
    def start_screen(self) -> None:
        """
        Display the start screen on the pygame view. The start screen has options to Start Game, Quit or Help.
        """
        start = True
        help_button = False

        while start:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pygame.quit()
                    sys.exit()
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
                            self.pygame.quit()
                            sys.exit()
                    else:
                        self.start_buttons[1].color = (255,0,0)

                    if self.start_buttons[2].is_over(clicked): #check the help button
                        self.start_buttons[2].color = (13,25,82)
                        if self.pygame.mouse.get_pressed()[0]:
                            help_button = True
                    else:
                        self.start_buttons[2].color = (0,0,255)
            
            # font sizes
            big_font = pygame.font.Font("Consequences.ttf", 100)
            sm_font = pygame.font.Font("Consequences.ttf", 50)

            self.set_background("images/clouds.jpg")
            
            # if help button is pressed, display the instructions screen and return to main button
            if help_button == True:
                # display instruction screen
                self.set_background("images/help.jpg")

                # creating and accessing data of button in help screen
                self.back_button.draw_button(self.win, True)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:          
                        clicked = self.pygame.mouse.get_pos()
                        if self.back_button.is_over(clicked):
                            self.back_button.color = (162,20,20)
                            if self.pygame.mouse.get_pressed()[0]:
                                help_button = False
                        else:
                            self.back_button.color = (255,0,0)
                            
            # if help button is not pressed, print the regular start screen
            else:  
                # font sizes
                big_font = pygame.font.Font("Consequences.ttf", 100)
                sm_font = pygame.font.Font("Consequences.ttf", 50)

                # set background
                self.set_background("images/clouds.jpg")
                
                # messages printed on start screen
                welcome = sm_font.render("Welcome to", True, (0,0,0))
                self.win.blit(welcome, (150,230))
                
                title = big_font.render("Line Up 4!", True, (0,0,0))
                self.win.blit(title, (60,310))

                # display buttons
                for button in self.start_buttons:
                    button.draw_button(self.win, True)

            self.pygame.display.update()


