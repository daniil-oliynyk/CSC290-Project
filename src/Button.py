import pygame

class Button():

    def __init__(self, color, x, y, width, height, textsize, text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textsize = textsize
        
    def draw_button(self, win, outline=None):
        """
        Draws a rectangular button onto the GUI. 
        """
        if outline: #if you want an outline on the button (outline = True)
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.textsize)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        """
        pos is the mouse position / tuple of (x, y) coordinates.
        Returns true iff pos is within the range of the button.
        """
        if pos[0] > self.x and pos[0] < (self.x + self.width):
            if pos[1] > self.y and pos[1] < (self.y + self.height):
                return True

        return False
        
