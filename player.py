from pygame import Vector2
from ball import Ball


class Player(Ball):
    def __init__(self, color, speed, startposition, width, life, window):
        super().__init__(color=color, startposition=startposition, width=width, window=window)        
        self.life = life
        self.start = startposition
        self.speed = speed
        
        
    
    def update_position(self,dt, vector_mov=(0,0)):
        dt = dt/2
        vect = Vector2(vector_mov[0]*self.speed*dt,vector_mov[1]*self.speed*dt)
        if super().in_borders(vect):
            self.float_pos += vect
            super().update_position()


    def touch_ennemis(self, ennemis):
        for e in ennemis:
            if self.position[0] + self.width >= e.position[0] - e.width and self.position[0] - self.width <= e.position[0] + e.width:
                if self.position[1] + self.width >= e.position[1] - e.width and self.position[1] - self.width <= e.position[1] + e.width:
                    self.death()
        return self.life


    def touch_zones(self, zones):
        for z in zones:
            if self.position[0] + self.width >= z.rect[0] and self.position[0] - self.width <= z.rect[0] + z.rect[2]:
                if self.position[1] + self.width >= z.rect[1] and self.position[1] - self.width <= z.rect[1] + z.rect[3]:
                    return True
        return False

    def death(self):
        super().new_position(self.start)
        self.life -= 1
