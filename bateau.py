import enumBateau


class Bateau:

    nom = str
    taille = int
    orientation = enumBateau.EnumBateau
    cases_hit = int

    def __init__(self, nom, taille, orientation, cases_hit):
        self.nom = nom
        self.taille = taille
        self.orientation = orientation
        self.cases_hit = cases_hit

    def est_coule(self):
        if self.taille == self.cases_hit:
            print("Bateau coulé, vous avez perdu ce bateau")

    def tirer(self, x, y):
        # sens orientation du tir (si le joueur choisit de tirer en horizontale)
        if x ==

    def est_touche(self):
        self.cases_hit = self.cases_hit + 1
        print("Bateau touché")
