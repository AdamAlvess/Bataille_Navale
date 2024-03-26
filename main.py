from joueur import Joueur
from ia import IA

def main():
    partie = 0
    while True:
        print("Menu:")
        print("1- Jouer")
        print("2- Quitter")
        choix = input("Choisissez une option: ")

        if choix == '1':
            joueur = Joueur('Joueur 1', 10)
            ia = IA('IA', 10)

            joueur.placer_bateaux()
            ia.placer_bateaux()

            while not joueur.carte.est_vide() and not ia.carte.est_vide():
                joueur.attaquer(ia)
                ia.attaquer(joueur)

                print("Carte du joueur mise à jour:")
                joueur.carte.update_display(joueur.nom)
                ia.carte.update_display(ia.nom)
     
            if joueur.carte.est_vide():
                print("L'IA a gagné !")
                partie += 1
            else:
                print("Le joueur a gagné !")
                partie += 1
            
            ia.coup_recorder.delimite_partie()
            partie += 1

        elif choix == '2':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir 1 ou 2.")

if __name__ == '__main__':
    main()