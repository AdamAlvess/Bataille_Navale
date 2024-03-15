import map

class Joueur:
    def __init__(self, nom, taille_carte):
        self.nom = nom
        self.carte = map.Map(taille_carte, taille_carte)
        self.bateaux = [(5, 'h'), (4, 'v'), (3, 'h'), (3, 'v'), (2, 'h')]  
    
    def placer_bateaux(self):
        for bateau in self.bateaux:
            placed = False
            while not placed:
                taille, orientation = bateau
                print(f"{self.nom}, placez votre bateau de taille {taille}:")
                x = int(input("Entrez la coordonnée X du coin supérieur gauche du bateau (0-9) : "))
                y = int(input("Entrez la coordonnée Y du coin supérieur gauche du bateau (0-9) : "))
                orientation_input = input("Entrez l'orientation que vous souhaitez pour votre bateau (v ou h) : ").lower()
                if orientation_input == 'h':
                    if x < 0 or x >= self.carte.height or y < 0 or y + taille > self.carte.width:
                        print("Placement invalide. Réessayez.")
                        continue
                    for i in range(taille):
                        if self.carte.map[x][y+i] != '.':
                            print("Placement invalide. Réessayez.")
                            break
                    else:
                        for i in range(taille):
                            self.carte.map[x][y+i] = 'X'
                        placed = True
                elif orientation_input == 'v':
                    if x < 0 or x + taille > self.carte.height or y < 0 or y >= self.carte.width:
                        print("Placement invalide. Réessayez.")
                        continue
                    for i in range(taille):
                        if self.carte.map[x+i][y] != '.':
                            print("Placement invalide. Réessayez.")
                            break
                    else:
                        for i in range(taille):
                            self.carte.map[x+i][y] = 'X'
                        placed = True
                else:
                    print("Orientation invalide. Réessayez.")
        self.carte.update_display()
