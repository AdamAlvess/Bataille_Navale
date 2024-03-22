import pandas as pd
import numpy as np


class Map:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.mapper = pd.DataFrame(np.full((height, width), '.'), columns=[
            chr(65 + i) for i in range(width)], index=range(height))

    def update_map(self, x, y, taille, orientation):
        if orientation == 'h':
            for i in range(taille):
                self.mapper.iloc[x, y + i] = 'X'
        elif orientation == 'v':
            for i in range(taille):
                self.mapper.iloc[x + i, y] = 'X'
        else:
            print('Orientation non valide')

    def update_display(self):
        print(self.mapper)

    def checkBateau(self, x, y):
        convertY = ord(y) - ord('A')
        if self.mapper.iloc[x, convertY] == 'X':
            print("Bateau ici")
            return True
        else:
            print("Aucun bateau ici")
            return False

    def tirerBateau(self, x, y):
        convertY = ord(y) - ord('A')
        self.mapper.iloc[x, convertY] = 'T'
        print(self.mapper)
