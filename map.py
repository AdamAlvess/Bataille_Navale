import pandas as pd
import numpy as np
import time


class Map:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        index_labels = [str(i) for i in range(1, height + 1)]
        self.mapper = pd.DataFrame(np.full((height, width), '.'), columns=[chr(65 + i) for i in range(width)], index=index_labels)


    def update_mapper(self, x, y, taille, orientation):
        if orientation == 'h':
            for i in range(taille):
                self.mapper.iloc[x, y + i] = 'X'
        elif orientation == 'v':
            for i in range(taille):
                self.mapper.iloc[x + i, y] = 'X'
        else:
            print('Orientation non valide')

    def recevoir_attaque(self, x, y):
        x -= 1
        y -= 1
        if self.mapper.iloc[x, y] == 'X':
            print("Touché !")
            self.mapper.iloc[x, y] = 'T'
        elif self.mapper.iloc[x, y] == '.':
            print("Dans l'eau !")
            self.mapper.iloc[x, y] = 'O'

    def est_vide(self):
        return not (self.mapper == 'X').any().any()

    def update_display(self, nom):
        if nom == "IA":

            time.sleep(3)
            print("\n\n\n          IA")

            mapIA = self.mapper.replace('X', '.')
            print(mapIA)
        else:
            print("joueur la")
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
        self.mapper.iloc[x+1, convertY] = 'T'

