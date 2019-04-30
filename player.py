from pygame import Vector2
from ball import Ball


class Player(Ball):
    def __init__(self, color, speed, startposition, width, life, window):
        super().__init__(color=color, startposition=startposition, width=width)        
        self.life = life
        self.start = startposition
        self.speed = speed
        self.window = window
        
        
    
    def update_position(self,dt, vector_mov=(0,0)):
        vec = Vector2(vector_mov[0]*self.speed*dt,vector_mov[1]*self.speed*dt)
        if self.player_in_borders(vec):
            super().update_position(vec)

    def player_in_borders(self, vec):
        vect_temp = Vector2(self.position)
        vect_temp += vec
        if vect_temp[0] - self.width < 0 or vect_temp[0]+self.width > self.window.get_size()[0]:
            return False
        if vect_temp[1] - self.width < 0 or vect_temp[1]+self.width > self.window.get_size()[1]:
            return False
        return True

    def player_touch_ennemis(self, ennemis):
        for e in ennemis:
            if self.position[0] + self.width >= e.position[0] - e.width and self.position[0] - self.width <= e.position[0] + e.width:
                if self.position[1] + self.width >= e.position[1] - e.width and self.position[1] - self.width <= e.position[1] + e.width:
                    self.death()
        return self.life

    def death(self):
        super().new_position(self.start)
        self.life -= 1