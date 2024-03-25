import tkinter as tk
from tkinter import ttk
import numpy as np


class MatrixFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg='white')
        self.canvas = tk.Canvas(self, width=550, height=550)  # Création du canevas pour la matrice
        self.canvas.grid(row=0, column=0, padx=20, pady=20)
        self.draw_matrix()

    def draw_matrix(self):
        # Dessiner les lettres sur l'abscisse
        for i in range(10):
            label = tk.Label(self.canvas, text=chr(65 + i), font=('Arial', 12))
            label.place(x=i * 50 + 40, y=0)  # Positionnement des labels

        # Dessiner les nombres sur l'ordonnée
        for j in range(10):
            label = tk.Label(self.canvas, text=str(j), font=('Arial', 12))
            label.place(x=5, y=j * 50 + 40)  # Positionnement des labels

        # Dessiner une grille de cases
        for i in range(10):
            for j in range(10):
                x0 = j * 50 + 25
                y0 = i * 50 + 25
                x1 = x0 + 50
                y1 = y0 + 50
                self.canvas.create_rectangle(x0, y0, x1, y1, outline='white')

    def place_boats(self, boat_data):
        for boat in boat_data:
            nom, size, letter, number, orientation = boat
            x = ord(letter) - ord('A')  # Convertir la lettre en un indice de colonne
            y = int(number)  # Convertir le nombre en un indice de ligne
            if orientation == 'h':
                for i in range(size):
                    self.canvas.create_rectangle(x * 50 + i * 50 + 25, y * 50 + 25, x * 50 + (i + 1) * 50 + 25, y * 50 + 75, fill='red')
            else:
                for i in range(size):
                    self.canvas.create_rectangle(x * 50 + 25, y * 50 + i * 50 + 25, x * 50 + 75, y * 50 + (i + 1) * 50 + 25, fill='red')


class BoatBox(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg='white')
        self.canvas = tk.Canvas(self, width=350, height=600)  # Création du canevas pour la boîte à bateaux
        self.canvas.grid(row=1, column=2, padx=20, pady=20)  # Déplacer le BoatBox vers la droite avec une marge de 20 pixels
        self.boat_data = np.empty((5, 5), dtype=object)  # Tableau NumPy pour stocker les données des bateaux
        self.add_boat_box()
        self.add_buttons()  # Appel à la méthode pour ajouter les boutons

    def add_boat_box(self):
        # Ajout du contenu de la boîte pour les bateaux
        self.canvas.create_text(175, 30, text="Boîte à Bateaux", font=('Arial', 20), fill='white')
        # Bateau de 2
        self.canvas.create_rectangle(25, 100, 125, 150, fill='#0080ff')
        # Bateau de 3
        self.canvas.create_rectangle(25, 200, 175, 250, fill='#0080ff')
        # Bateau de 3
        self.canvas.create_rectangle(25, 300, 175, 350, fill='#0080ff')
        # Bateau de 4
        self.canvas.create_rectangle(25, 400, 225, 450, fill='#0080ff')
        # Bateau de 5
        self.canvas.create_rectangle(25, 500, 275, 550, fill='#0080ff')

    def add_buttons(self):
        # Boutons et Combobox pour chaque bateau
        for i, (nom, size, x_offset, y_offset) in enumerate([(1, 2, 40, 180), (2, 3, 40, 280), (3, 3, 40, 380), (4, 4, 40, 480), (5, 5, 40, 580)]):
            # Combobox pour choisir une lettre de A à J
            letter_combobox = ttk.Combobox(self, values=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], state='readonly', width=2)
            letter_combobox.place(x=x_offset, y=y_offset)
            letter_combobox.set('A')

            # Combobox pour choisir un chiffre de 0 à 9
            number_combobox = ttk.Combobox(self, values=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], state='readonly', width=2)
            number_combobox.place(x=x_offset + 60, y=y_offset)
            number_combobox.set('0')

            # Combobox pour choisir horizontal ou vertical
            orientation_combobox = ttk.Combobox(self, values=['h', 'v'], state='readonly', width=2)
            orientation_combobox.place(x=x_offset + 120, y=y_offset)
            orientation_combobox.set('h')

            # Bouton pour valider et placer le bateau
            validate_button = tk.Button(self, text=f"Valider et placer {nom}", command=lambda size=size, letter=letter_combobox, number=number_combobox, orientation=orientation_combobox, nom=nom: self.validate_and_place(nom, size, letter.get(), number.get(), orientation.get()))
            validate_button.place(x=x_offset + 180, y=y_offset - 2)

    def validate_and_place(self, nom, size, letter, number, orientation):
        # Fonction pour valider et placer le bateau
        self.boat_data[nom - 1] = [nom, size, letter, number, orientation]
        print(f"Bateau {nom} validé et placé. Données enregistrées : {self.boat_data[nom - 1]}")
        self.master.matrix_frame.place_boats(self.boat_data)


class MyWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(bg='light blue')
        self.geometry('1400x900+0+0')  # Augmentation de la largeur de la fenêtre
        self.title_label = tk.Label(self, text="Bataille navale", width=30, height=2, bg='red', fg='brown', font=('Arial', 40))
        self.title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        self.matrix_frame = MatrixFrame(self)
        self.matrix_frame.grid(row=1, column=0)
        self.boat_box = BoatBox(self)
        self.boat_box.grid(row=1, column=2, padx=20)

if __name__ == '__main__':
    app = MyWindow()
    app.mainloop()

