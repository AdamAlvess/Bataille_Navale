import enumBateau


class Bateau:

    nom = str
    taille = int
    orientation = enumBateau.EnumBateau
    cases_hit = int

    def __init__(self, nom, taille, orientation, cases_hit):
        self.taille = taille
        self.orientation = orientation
        self.cases_hit = cases_hit
