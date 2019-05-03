from ball import Ball
from pygame import Vector2
import itertools

class Ennemi(Ball):
    def __init__(self, color,startposition, width, moves,window):
        super().__init__(color=color, startposition=startposition, width=width, window=window)
        self.moves = itertools.cycle(moves)
        self.move = None
        self.speed = None
        self.change_move()


    def update_position(self, dt):           
        self.float_pos += self.speed
        heading = self.float_pos - self.move["pos"]        
        distance = heading.length()
        if distance < 0.01:
            self.change_move()
        super().update_position()

    
    def change_move(self):
        self.move = next(self.moves)
        time = self.move["time"]
        pos = self.move["pos"]
        heading = pos-self.float_pos
        self.speed = Vector2(heading[0]/time,heading[1]/time)
