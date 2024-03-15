from map import Map
from joueur import Joueur

def main():
    map_obj = Map(10, 10)
    joueur = Joueur('Joueur 1', 10)
    joueur.placer_bateaux() 
    
if __name__ == '__main__':
    main()
