import pygame
from ball import Ball
from player import Player
from ennemi import Ennemi
from levelloader import LevelLoader
from pygame import Vector2

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
        start_vect = Vector2(data_level["player"]["startpos"][0],data_level["player"]["startpos"][1])
        
        #Generate player
        self.player = Player(color=(255,0,0),speed=1,startposition=start_vect,width=data_level["player"]["width"],life=3, window=self.window)
        

        #Generate list of ennemis
        self.ennemies = []
        for e in data_level["ennemis"].values():   
            start_vect = Vector2(e["startpos"][0],e["startpos"][1])         
            self.ennemies.append(Ennemi(color=e["color"],startposition=start_vect,width=e["width"],moves=e["moves"]))
        

    def run_game(self):
        self.initalize_level()
        end_game = False
        x = 0
        y = 0
        while not end_game:

            dt = self.clock.tick(120)
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
            for e in self.ennemies:
                e.update_position(dt)
                e.draw(self.window)

            self.player.update_position(dt,(x,y))            
            self.player.draw(self.window)
            
            if self.player.player_touch_ennemis(self.ennemies) <= 0:
                """print("You die !")
                return"""
                pass

            pygame.display.flip()
            self.window.blit(self.background, (0, 0))
    
    
    
if __name__ == "__main__":
    MainGame((1200,400)).run()