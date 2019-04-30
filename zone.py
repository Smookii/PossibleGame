import pygame

class Zone():
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
