import pygame
from ball import Ball
from player import Player
from ennemi import Ennemi
from levelloader import LevelLoader
from zone import Zone
from pygame import Vector2

class MainGame():
    def __init__(self, size, fps=30):
        #Pygame initialization
        pygame.init()
        self.window = pygame.display.set_mode(size)
        self.background = pygame.Surface(self.window.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = fps

        #Initialize game object
        self.player = None
        self.ennemies = None
        self.endzones = None
        self.level_id = "Level1"
        self.next_level = ""
        self.pause_ennemi = True
        self.run_game()

    def initalize_level(self) :
        #Read the level file
        data_level = LevelLoader.loadLevel("Levels/"+self.level_id +".json")
        self.next_level = data_level["next_level"]

                
        #Generate player
        start_vect = Vector2(data_level["player"]["startpos"][0],data_level["player"]["startpos"][1])
        self.player = Player(color=(255,0,0),speed=1,startposition=start_vect,width=data_level["player"]["width"],life=3, window=self.window)
        

        #Generate list of ennemis
        self.ennemies = []
        for e in data_level["ennemis"].values():   
            start_vect = Vector2(e["startpos"][0],e["startpos"][1])         
            self.ennemies.append(Ennemi(color=e["color"],startposition=start_vect,width=e["width"],moves=e["moves"]))

        #Generate list of ennmis
        self.endzones = []
        for z in data_level["end_zones"].values():
            self.endzones.append(Zone(color=z["color"], rect=z["rect"]))
        

    def run_game(self):
        end_game = False
        while not end_game:
            self.initalize_level()
            end_level = False
            x = 0
            y = 0
            while not end_level:
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

                for z in self.endzones:
                    z.draw(self.window)

                for e in self.ennemies:
                    if not self.pause_ennemi:
                        e.update_position(dt)
                    e.draw(self.window)

                self.player.update_position(dt,(x,y))            
                self.player.draw(self.window)
                
                if self.player.player_touch_ennemis(self.ennemies) <= 0:
                    """print("You die !")
                    return"""
                    pass

                if self.player.player_touch_zones(self.endzones):
                    self.level_id = self.next_level
                    end_level = True

                pygame.display.flip()
                self.window.blit(self.background, (0, 0))        
        pygame.quit()
    
    
    
if __name__ == "__main__":
    MainGame((1200,400)).run()