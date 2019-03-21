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
#show_go_screen = False

while game_loop: #loop iterates as long as user has not quit
    pygame.time.delay(50)

    if(controller.check_quit() is False):
        
        game_loop = False


    if(model.curr_disk == None ):
        disk_pos_x = controller.check_click() #receive position of mouse click
        if (disk_pos_x != None):
            game_over = model.add_disk(disk_pos_x) #add the new disk
    
    model.change_colour() #changes the colour for the next disk
    
    model.update_view(game_over) #model sends new data to the view    
       
    if(game_over is True):
        if(controller.return_restart_flag() is True): #checking if R key is pressed to restart game
            model.restart_model() 
            game_over = False
            model.update_view(game_over)
            #resets model and updates the view
        
#while show_go_screen:
 #   model.set_game_over()
  #  if(controller.check_quit() is False):
   #     show_go_screen = False


pygame.quit()
