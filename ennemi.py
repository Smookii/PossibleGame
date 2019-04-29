from ball import Ball

class Ennemi(Ball):
    def __init__(self, color,startposition, width, moves):
        super().__init__(color=color, startposition=startposition, width=width)
        self.moves = moves
        self.index = 1
        self.move_vect = self.moves[self.index][0]
        self.target = self.moves[self.index][1]


    def update_position(self, dt):
        for i in range(0,2):
            if self.move_vect[i] > 0:
                if self.position[i] >= self.target[i]:
                    self.inc_index()
            if self.move_vect[i] < 0:
                if self.position[i] <= self.target[i]:
                    self.inc_index()                       
        super().update_position([self.move_vect[0]*dt,self.move_vect[1]*dt])

    def inc_index(self):
        self.index += 1
        if self.index >= len(self.moves):
            self.index = 0
        self.update_move()
    
    def update_move(self):
        self.move_vect = self.moves[self.index][0]
        self.target = self.moves[self.index][1]