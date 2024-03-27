import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from Matrice import *
from Matrice2 import *

class BoatBox(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg='white')
        self.canvas = tk.Canvas(self, width=350, height=600)  
        self.canvas.grid(row=1, column=2, padx=20, pady=20)  
        self.boat_data = np.empty((5, 5), dtype=object)  
        self.occupied_cells = set()  
        self.add_boat_box()
        self.add_buttons() 
        self.play_button = tk.Button(self, text="Play", command=self.start_game, state='disabled')
        self.play_button.grid(row=2, column=2, pady=10)

    def add_boat_box(self):
        # Ajout du contenu de la boîte pour les bateaux
        self.canvas.create_text(175, 30, text="Boîte à Bateaux", font=('Arial', 20), fill='white')
        self.canvas.create_rectangle(25, 100, 125, 150, fill='#0080ff')
        self.canvas.create_rectangle(25, 200, 175, 250, fill='#0080ff')
        self.canvas.create_rectangle(25, 300, 175, 350, fill='#0080ff')
        self.canvas.create_rectangle(25, 400, 225, 450, fill='#0080ff')
        self.canvas.create_rectangle(25, 500, 275, 550, fill='#0080ff')

    def add_buttons(self):
        for i, (nom, size, x_offset, y_offset) in enumerate([(1, 2, 40, 180), (2, 3, 40, 280), (3, 3, 40, 380), (4, 4, 40, 480), (5, 5, 40, 580)]):
            letter_combobox = ttk.Combobox(self, values=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], state='readonly', width=2)
            letter_combobox.place(x=x_offset, y=y_offset)
            letter_combobox.set('A')

            number_combobox = ttk.Combobox(self, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], state='readonly', width=2)
            number_combobox.place(x=x_offset + 60, y=y_offset)
            number_combobox.set('1')

            orientation_combobox = ttk.Combobox(self, values=['h', 'v'], state='readonly', width=2)
            orientation_combobox.place(x=x_offset + 120, y=y_offset)
            orientation_combobox.set('h')

            validate_button = tk.Button(self, text=f"Valider et placer {nom}", command=lambda size=size, letter=letter_combobox, number=number_combobox, orientation=orientation_combobox, nom=nom: self.validate_and_place(nom, size, letter.get(), number.get(), orientation.get()))
            validate_button.place(x=x_offset + 180, y=y_offset - 2)

    def validate_and_place(self, nom, size, letter, number, orientation):
        # Vérifier s'il y a déjà un bateau de ce type
        for boat in self.boat_data:
            if boat[0] == nom:
                messagebox.showerror("Erreur", f"Vous ne pouvez placer qu'un seul bateau de taille {size}.")
                return

        # Vérifier si le bateau dépasse les cases de la matrice
        x = ord(letter) - ord('A')
        y = int(number)

        if orientation == 'h':
            if x + size > 10:
                messagebox.showerror("Erreur", "Le bateau dépasse la limite de la matrice.")
                return

            for i in range(size):
                if (x + i, y) in self.occupied_cells:
                    messagebox.showerror("Erreur", "Collision détectée. Veuillez replacer le bateau.")
                    return
        else:
            if y + size > 10:
                messagebox.showerror("Erreur", "Le bateau dépasse la limite de la matrice.")
                return

            for i in range(size):
                if (x, y + i) in self.occupied_cells:
                    messagebox.showerror("Erreur", "Collision détectée. Veuillez replacer le bateau.")
                    return
                self.occupied_cells.add((x, y + i))

        # Enregistrer les données du bateau
        self.boat_data[nom - 1] = [nom, size, letter, number, orientation]
        print(f"Bateau {nom} validé et placé. Données enregistrées : {self.boat_data[nom - 1]}")
        self.master.matrix_frame.place_boats(self.boat_data)
        
        if all(self.boat_data[i][0] is not None for i in range(5)):
            self.play_button.config(state='normal')  # Activer le bouton "Play"

        self.master.matrix_frame.place_boats(self.boat_data)
        
    def start_game(self):
        self.canvas.grid_forget()
        self.master.matrix_frame = Matrix2Frame(self.master)
        self.master.matrix_frame.grid(row=1, column=2)

