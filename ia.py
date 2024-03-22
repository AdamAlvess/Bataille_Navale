from map import Map
import random

class IA:
    def __init__(self, nom, taille_carte):
        self.nom = nom
        self.carte = Map(taille_carte, taille_carte)
        self.bateaux = [5, 4, 3, 3, 2]

    def placer_bateaux(self):
        for taille in self.bateaux:
            placed = False
            while not placed:
                x = random.randint(0, self.carte.height - 1)
                y = random.randint(0, self.carte.width - 1)
                orientation = random.choice(['h', 'v'])

                if orientation == 'h':
                    if x < 0 or x >= self.carte.height or y < 0 or y + taille > self.carte.width:
                        continue
                    for i in range(taille):
                        if self.carte.map.iloc[x, y + i] != '.':
                            break
                    else:
                        for i in range(taille):
                            self.carte.map.iloc[x, y + i] = 'X'
                        placed = True
                elif orientation == 'v':
                    if x < 0 or x + taille > self.carte.height or y < 0 or y >= self.carte.width:
                        continue
                    for i in range(taille):
                        if self.carte.map.iloc[x + i, y] != '.':
                            break
                    else:
                        for i in range(taille):
                            self.carte.map.iloc[x + i, y] = 'X'
                        placed = True

    def attaquer(self, adversaire):
        x, y = self.choisir_cible()
        adversaire.carte.recevoir_attaque(x, y)

    def choisir_cible(self):
        x = random.randint(0, self.carte.height - 1)
        y = random.randint(0, self.carte.width - 1)
        return x, y
