class Joueur:
    def __init__(self, nom, taille_carte):
        self.nom = nom
        self.carte = Map(taille_carte, taille_carte)
        self.bateaux = []

    def placer_bateaux(self):
        """
        Place les bateaux du joueur sur sa carte.
        """
        for bateau in self.bateaux:
            placed = False
            while not placed:
                print(f"{self.nom}, placez votre bateau de taille {bateau.taille}:")
                x = int(input("Entrez la coordonnée X (0-9) : "))
                y = int(input("Entrez la coordonnée Y (0-9) : "))
                orientation = input("Entrez l'orientation (h pour horizontal, v pour vertical) : ").lower()

                if self.carte.place_boat(bateau.taille, x, y, orientation):
                    placed = True
                else:
                    print("Placement invalide. Réessayez.")

    def tirer_adversaire(self, adversaire, x, y):
        """
        Gère un tir sur la carte de l'adversaire.
        """
        adversaire.carte.tirer(x, y)

    def est_victorieux(self):
        """
        Vérifie si le joueur a gagné la partie.
        """
        for bateau in self.bateaux:
            if not bateau.est_coule():
                return False
        return True
