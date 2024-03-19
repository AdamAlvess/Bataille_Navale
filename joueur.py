import map


class Joueur:
    def __init__(self, nom, taille_carte):
        self.nom = nom
        self.carte = map.Map(taille_carte, taille_carte)
        self.bateaux = [5, 4, 3, 3, 2]

    def placer_bateaux(self):
        for taille in self.bateaux:
            placed = False
            while not placed:
                print(f"{self.nom}, placez votre bateau de taille {taille}:")
                x = int(
                    input("Entrez la coordonnée X du coin supérieur gauche du bateau (0-9) : "))
                colonne = input(
                    "Entrez la colonne du coin supérieur gauche du bateau (A-J) : ").upper()
                # Convertir la lettre en numéro de colonne
                y = ord(colonne) - ord('A')
                orientation_input = input(
                    "Entrez l'orientation que vous souhaitez pour votre bateau (v ou h) : ").lower()

                if orientation_input == 'h':
                    if x < 0 or x >= self.carte.height or y < 0 or y + taille > self.carte.width:
                        print("Placement invalide. Réessayez.")
                        continue
                    for i in range(taille):
                        if self.carte.mapper.iloc[x, y + i] != '.':
                            print("Les bateaux se chevauchent. Réessayez.")
                            break
                    else:
                        for i in range(taille):
                            self.carte.mapper.iloc[x, y + i] = 'X'
                        placed = True
                elif orientation_input == 'v':
                    if x < 0 or x + taille > self.carte.height or y < 0 or y >= self.carte.width:
                        print("Placement invalide. Réessayez.")
                        continue
                    for i in range(taille):
                        if self.carte.mapper.iloc[x + i, y] != '.':
                            print("Les bateaux se chevauchent. Réessayez.")
                            break
                    else:
                        for i in range(taille):
                            self.carte.mapper.iloc[x + i, y] = 'X'
                        placed = True
                else:
                    print("Orientation invalide. Réessayez.")
        self.carte.update_display()

        # check bateau
        lose = False
        cpt = 0
        while not lose:
            print("\n\nA votre tour de tirer sur un bateau: \n")
            xShoot = int(input("Entrez la coordonnée X du bateau (0-9) : "))
            yShoot = input("Entrez la coordonnée Y du bateau (A-J) : ").upper()
            checker = self.carte.checkBateau(xShoot, yShoot)
            checker

            # tirer bateau
            if checker == True:
                print("Bateau touché")
                self.carte.tirerBateau(xShoot, yShoot)
                cpt += 1
                print(cpt)
            if cpt == 3:
                lose = True

            # add joueur 2 et remplacer cpt par if 0 bateau left ou if bateau all touche

        print("Thanks for playing")
