from ball import Ball
from pygame import Vector2

class Ennemi(Ball):
    def __init__(self, color,startposition, width, moves):
        super().__init__(color=color, startposition=startposition, width=width)
        self.moves = moves
        self.index = 1
        self.cpt_time = 0
        self.time = self.moves[self.index]["time"]
        self.fx = self.moves[self.index]["x"].split(',')
        self.fy = self.moves[self.index]["y"].split(',')


    def update_position(self, dt):
        if self.cpt_time >= self.time:  
            self.cpt_time = 0
            self.inc_index()
        self.cpt_time += dt            
        vect = Vector2(self.compute_f(self.fx),self.compute_f(self.fy))   
        super().update_position(vect)


    def compute_f(self, f):
        if f[0] == '' or None:
            return 0
        if f[0] == 'l':
            return int(f[1])


    def inc_index(self):
        self.index += 1
        if self.index >= len(self.moves):
            self.index = 0
        self.change_move()
    
    def change_move(self):
        self.time = self.moves[self.index]["time"]
        self.fx = self.moves[self.index]["x"].split(',')
        self.fy = self.moves[self.index]["y"].split(',')
