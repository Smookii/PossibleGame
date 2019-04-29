import pygame
from ball import Ball
from player import Player



class MainGame():

    def __init__(self, size, fps=30):
        pygame.init()
        self.window = pygame.display.set_mode(size)
        self.background = pygame.Surface(self.window.get_size()).convert()
        self.run_game()
        pygame.quit()

    def initalize_level(self):
        #MUST CREATE CLASS LEVEL
        return Player((255,0,0),1,[40,40],16,3)
        

    def run_game(self):
        player = self.initalize_level()
        end_game = False
        x = 0
        y = 0
        while not end_game:
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
            player.update_position((x,y))
            player.draw(self.window)
            pygame.display.flip()
            self.window.blit(self.background, (0, 0))
            
    
    
    
if __name__ == "__main__":
    MainGame((1200,800)).run()