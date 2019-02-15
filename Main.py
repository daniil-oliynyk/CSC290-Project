from Model import Model
from Controller import Controller
from View import View
import pygame

pygame.init()
win = pygame.display.set_mode((700, 800))
controller = Controller(pygame)
view = View(win, pygame)
model = Model(win, view, controller)

while controller.check_quit(): #loop iterates as long as user has not quit
    pygame.time.delay(50)

    if(model.curr_disk == None):
        disk_pos_x = controller.check_click() #receive position of mouse click
        if (disk_pos_x != None):
            model.add_disk(disk_pos_x) #add the new disk
    model.change_colour() #changes the colour for the next disk

    model.update_view() #model sends new data to the view

pygame.quit()