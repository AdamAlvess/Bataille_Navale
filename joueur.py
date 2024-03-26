from map import Map
import random


class Joueur:
    def __init__(self, nom, taille_carte):
        self.nom = nom
        self.carte = Map(taille_carte, taille_carte)
        self.bateaux = [5, 4, 3, 3, 2]

    def placer_bateaux(self):
        for taille in self.bateaux:
            placed = False
            while not placed:
                print(f"{self.nom}, placez votre bateau de taille {taille}:")
                x = int(input("Entrez la coordonnée X du coin supérieur gauche du bateau (1-10) : ")) 
                colonne = input("Entrez la colonne du coin supérieur gauche du bateau (A-J) : ").upper()
                y = ord(colonne) - ord('A') + 1  
                orientation_input = input("Entrez l'orientation que vous souhaitez pour votre bateau (v ou h) : ").lower()
                
                if orientation_input == 'h':
                    if x < 1 or x > self.carte.height or y < 1 or y + taille - 1 > self.carte.width:
                        print("Placement invalide. Réessayez.")
                        continue
                    for i in range(taille):
                        if self.carte.mapper.iloc[x - 1, y + i - 1] != '.':
                            print("Les bateaux se chevauchent. Réessayez.")
                            break
                    else:
                        for i in range(taille):
                            self.carte.mapper.iloc[x - 1, y + i - 1] = 'X'
                        placed = True
                elif orientation_input == 'v':
                    if x < 1 or x + taille - 1 > self.carte.height or y < 1 or y > self.carte.width:
                        print("Placement invalide. Réessayez.")
                        continue
                    for i in range(taille):
                        if self.carte.mapper.iloc[x + i - 1, y - 1] != '.':
                            print("Les bateaux se chevauchent. Réessayez.")
                            break
                    else:
                        for i in range(taille):
                            self.carte.mapper.iloc[x + i - 1, y - 1] = 'X'
                        placed = True
                else:
                    print("Orientation invalide. Réessayez.")
        self.carte.update_display(self.nom)

    def attaquer(self, adversaire):
        x, y = self.choisir_cible()
        adversaire.carte.recevoir_attaque(x, y)

    def choisir_cible(self):
        print(f"{self.nom}, choisissez une cible :")
        x = int(input("Entrez la coordonnée X de la cible (1-10) : "))
        colonne = input("Entrez la colonne de la cible (A-J) : ").upper()
        y = ord(colonne) - ord('A') + 1  
        return x, y
