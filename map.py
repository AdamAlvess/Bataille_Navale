import pandas as pd
import numpy as np

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        index_labels = [str(i) for i in range(1, height + 1)]
        self.mapper = pd.DataFrame(np.full((height, width), '.'), columns=[chr(65 + i) for i in range(width)], index=index_labels)

    def update_map(self, x, y, taille, orientation):
        if orientation == 'h':
            for i in range(taille):
                self.mapper.iloc[x, y + i] = 'X'
        elif orientation == 'v':
            for i in range(taille):
                self.mapper.iloc[x + i, y] = 'X'
        else:
            print('Orientation non valide')

    def recevoir_attaque(self, x, y):
        if self.mapper.iloc[x, y] == 'X':
            print("Touché !")
            self.mapper.iloc[x, y] = 'T'
        elif self.mapper.iloc[x, y] == '.':
            print("Dans l'eau !")
            self.mapper.iloc[x, y] = 'O'

    def est_vide(self):
        return not (self.mapper == 'X').any().any()

    def update_display(self):
        print(self.mapper)
