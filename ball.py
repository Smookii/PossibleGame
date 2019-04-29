import pygame

class Ball():
    def __init__(self, color, startposition, width):
        self.color = color   
        self.width = width
        self.position = startposition
        
    def __str__(self):
        print(self.color)
   
    def update_position(self, vector_mov=[0,0]):
        for i in range(0,2):
            self.position[i]+=vector_mov[i]

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, self.width)



    def get_position(self):
        return self.position
        
    
    

    