import pygame
from ball import Ball


class Player(Ball):
    def __init__(self, color, speed, startposition, width, life):
        super().__init__(color=color, startposition=startposition, width=width)        
        self.start = startposition
        self.speed = speed
        
        
    
    def update_position(self,dt, vector_mov=(0,0)):
        vec = [vector_mov[0]*self.speed*dt,vector_mov[1]*self.speed*dt]
        super().update_position(vec)