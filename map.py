import numpy as np
class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = np.array([['.' for _ in range(width)] for _ in range(height)])

    def display(self):
        for row in self.map:
            print(' '.join(row))
    def place_boat(self,taille, x, y, orientation):
        if orientation == 'h':
            for i in range(taille):
                self.map[x][y+i] = 'X'
        elif orientation == 'v':
            for i in range(taille):
                self.map[x+i][y] = 'X'
        else:
            print('Orientation non valide')
            return
    

map_obj = Map(10, 10)
map_obj.boat(5, 1, 2, 'v')
map_obj.display()