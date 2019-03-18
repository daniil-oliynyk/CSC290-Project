import pygame

class Controller:
    
    def __init__(self, pygame) -> None:
        self.pygame = pygame
        
    

    def go_replay_handler(self):
        """
        return true iff the user has pressed the R key
        """
        for event in self.pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
        return False

    def go_quit_handler(self):
        """
        return true iff the user has pressed the Q key
        """
        for event in self.pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return True
        return False
            
    def check_quit(self):
        """
        return true iff the user hasnt selected to quit the game page.
        """
        for event in self.pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
            
    def check_click(self):
        """
        return the position of of mouse click iff the mouse was clicked.
        """
        mouse_button_1 = self.pygame.mouse.get_pressed()[0] #checks if the player has clicked the left mouse button
        if mouse_button_1:
            mouse_pos_x = self.pygame.mouse.get_pos()[0]
            disk_pos_x = mouse_pos_x - (mouse_pos_x % 100) + 50 # rounds the position of the disk to match the board GUI
            return disk_pos_x
