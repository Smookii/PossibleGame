class Ennemi(ball):
    def __init__(self, color, speed, startposition, size, movementman):
        super.__init__(color,speed,startposition,size)
        self.movementman = movementman