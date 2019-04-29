import pygame
from ball import Ball


class Player(Ball):
    def __init__(self, color, speed, startposition, width, life):
        super().__init__(color,speed,startposition, width, life)
        self.position = startposition
        

        