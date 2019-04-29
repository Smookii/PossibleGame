import pygame
from ball import Ball
from player import Player
from ennemi import Ennemi
from levelloader import LevelLoader


class MainGame():
    def __init__(self, size, fps=30):
        pygame.init()
        self.window = pygame.display.set_mode(size)
        self.background = pygame.Surface(self.window.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.run_game()
        self.player = None
        self.ennemies = None
        self.endzones = None
        pygame.quit()

    def initalize_level(self):
        data_level = LevelLoader.loadLevel("Levels/Level1.json")
        self.player = Player(color=(255,0,0),speed=1,startposition=data_level["player"]["pos"],width=data_level["player"]["width"],life=3)
        self.ennemies = []
        for e in data_level["ennemis"].values():            
            self.ennemies.append(Ennemi(color=e["color"],speed=e["speed"],startposition=e["moves"][0].copy(),width=e["width"],moves=e["moves"]))
        

    def run_game(self):
        self.initalize_level()
        end_game = False
        x = 0
        y = 0
        while not end_game:

            dt = self.clock.tick(self.fps)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    end_game=True 
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        x = -1
                    if e.key == pygame.K_RIGHT:
                        x = 1
                    if e.key == pygame.K_UP:
                        y = -1
                    if e.key == pygame.K_DOWN:
                        y = 1                
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                        x = 0
                    if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                        y = 0
            self.player.update_position((x,y))            
            self.player.draw(self.window)
            for e in self.ennemies:
                e.update_position(dt)
                e.draw(self.window)


            pygame.display.flip()
            self.window.blit(self.background, (0, 0))
    
    
    
if __name__ == "__main__":
    MainGame((1200,400)).run()