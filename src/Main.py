from Model import Model
from Controller import Controller
from View import View
import pygame


pygame.init()
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)

win = pygame.display.set_mode((700, 800))
controller = Controller(pygame)
view = View(win, pygame)
model = Model(win, view, controller)
pygame.display.set_caption('Line Up 4!')

view.start_screen()

game_loop = True
game_over = False

while game_loop: #loop iterates as long as user has not quit
    pygame.time.delay(50)

    if(controller.check_quit() is False):
        
        game_loop = False

    if(model.curr_disk == None ):
        disk_pos_x = controller.check_click() #receive position of mouse click
        if (disk_pos_x != None):
            game_over = model.add_disk(disk_pos_x) #add the new disk
            
    model.update_view(game_over) #model sends new data to the view
    
    model.change_colour() #changes the colour for the next disk
    
    if(game_over is True):
        model.restart_model() #clear the game board
        game_over = False

pygame.quit()
