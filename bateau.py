import enumBateau
from map import Map


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

    def est_touche(self):
        self.cases_hit = self.cases_hit + 1
        print("Bateau touché")
