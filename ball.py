import pygame
from pygame import Vector2

class Ball():
    def __init__(self, color, startposition, width):
        self.color = color   
        self.width = width
        self.position = startposition
        self.float_pos = Vector2(startposition)
        
    def __str__(self):
        print(self.color)
   
    def update_position(self, vector_mov=Vector2(0,0)):
        self.float_pos += vector_mov
        self.position = [int(self.float_pos[0]),int(self.float_pos[1])]



    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, self.width)

    def get_position(self):
        return self.position
        
    
    

    