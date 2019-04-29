import pygame

class Ball():
    def __init__(self, color, speed, startposition, width, life=0):
        self.color = color
        self.speed = speed
        self.position = startposition        
        self.width = width
        self.life = life
        
    def __str__(self):
        print(self.color)


    def update_position(self, vector_mov=(0,0)):
        self.position[0] += vector_mov[0]*self.speed
        self.position[1] += vector_mov[1]*self.speed

   
    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, self.width)
        
    
    

    