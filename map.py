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

    def recevoir_attaque(self, x, y):
        if self.map.iloc[x, y] == 'X':
            print("Touché !")
            self.map.iloc[x, y] = 'T'
        else:
            print("Dans l'eau !")
            self.map.iloc[x, y] = 'O'

    def est_vide(self):
        return not (self.map == 'X').any().any()

    def update_display(self):
        print(self.map)
