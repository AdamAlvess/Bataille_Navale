from joueur import Joueur
from ia import IA

def main():
    joueur = Joueur('Joueur 1', 10)
    ia = IA('IA', 10)

    joueur.placer_bateaux() 
    ia.placer_bateaux()  

    while not joueur.carte.est_vide() and not ia.carte.est_vide():
        joueur.attaquer(ia)
        if not ia.carte.est_vide():
            ia.attaquer(joueur)
            
        print("Carte du joueur mise à jour:")
        joueur.carte.update_display()

    if joueur.carte.est_vide():
        print("L'IA a gagné !")
    else:
        print("Le joueur a gagné !")

if __name__ == '__main__':
    main()
