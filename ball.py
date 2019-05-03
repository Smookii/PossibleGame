import pygame
from pygame import Vector2

class Ball():
    def __init__(self, color, startposition, width,window):
        self.color = color   
        self.width = width
        self.float_pos = Vector2(startposition)
        self.position = [int(self.float_pos[0]),int(self.float_pos[1])]
        self.window = window
        
    def __str__(self):
        print(self.color)
   
    def update_position(self):
        self.position = [int(self.float_pos[0]),int(self.float_pos[1])]

    def in_borders(self, vec):
        vect_temp = Vector2(self.position)
        vect_temp += vec
        if vect_temp[0] - self.width < 0 or vect_temp[0]+self.width > self.window.get_size()[0]:
            return False
        if vect_temp[1] - self.width < 0 or vect_temp[1]+self.width > self.window.get_size()[1]:
            return False
        return True


    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, self.width)


    def new_position(self, startposition):
        self.position = startposition
        self.float_pos = Vector2(startposition)

    
    

    