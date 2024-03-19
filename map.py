import pandas as pd
import numpy as np

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = pd.DataFrame(np.full((height, width), '.'), columns=[chr(65 + i) for i in range(width)], index=range(height))

    def update_map(self, x, y, taille, orientation):
        if orientation == 'h':
            for i in range(taille):
                self.map.iloc[x, y + i] = 'X'
        elif orientation == 'v':
            for i in range(taille):
                self.map.iloc[x + i, y] = 'X'
        else:
            print('Orientation non valide')

    def update_display(self):
        print(self.map)
