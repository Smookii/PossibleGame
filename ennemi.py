from ball import Ball

class Ennemi(Ball):
    def __init__(self, color, speed, startposition, width, moves):
        super().__init__(color=color, startposition=startposition, width=width)
        self.speed = speed
        self.moves = moves
        self.index = 1


    def update_position(self, dt):
        vector = [0,0]
        if self.position == self.moves[self.index]:
            self.index += 1
            if self.index >= len(self.moves):
                self.index = 0

        
        for i in range(0,2):
            if self.position[i] < self.moves[self.index][i]:
                vector[i] = self.speed
            if self.position[i] > self.moves[self.index][i]:
                vector[i] = -self.speed
        super().update_position(vector)