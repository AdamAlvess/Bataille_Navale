import tkinter as tk

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
            label.place(x=(i + 1) * 50 - 10, y=0)  # Utilisation de la méthode place pour positionner les labels

        # Dessiner les nombres sur l'ordonnée
        for j in range(10):
            label = tk.Label(self.canvas, text=str(j + 1), font=('Arial', 12))
            label.place(x=5, y=(j + 1) * 50 - 10)  # Utilisation de la méthode place pour positionner les labels

        # Dessiner une grille de cases
        for i in range(10):
            for j in range(10):
                x0 = j * 50 + 25
                y0 = i * 50 + 25
                x1 = x0 + 50
                y1 = y0 + 50
                self.canvas.create_rectangle(x0, y0, x1, y1, outline='white')

class BoatBox(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)  
        self.configure(bg='white')
        self.canvas = tk.Canvas(self, width=200, height=500)  # Création du canevas pour la boîte à bateaux
        self.canvas.grid(row=1, column=2, padx=20, pady=20)  # Déplacer le BoatBox vers la droite avec une marge de 20 pixels
        self.add_boat_box()
        
    def add_boat_box(self):
        # Ajout du contenu de la boîte pour les bateaux
        self.canvas.create_text(100, 30, text="Boîte à Bateaux", font=('Arial', 14), fill='white')
        # Ajouter les bateaux sous forme de carrés
        self.canvas.create_rectangle(25, 100, 75, 150, fill='black')  # Bateau de 2
        self.canvas.create_rectangle(25, 200, 100, 250, fill='black')  # Bateau de 3
        self.canvas.create_rectangle(25, 300, 150, 350, fill='black')  # Bateau de 4
        self.canvas.create_rectangle(25, 400, 200, 450, fill='black')  # Bateau de 5

class MyWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(bg='light blue')
        self.geometry('1000x700+400+0')  # Augmentation de la largeur de la fenêtre
        self.title_label = tk.Label(self, text="Bataille navale", width=30, height=2, bg='red', fg='brown', font=('Arial', 40))
        self.title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        self.matrix_frame = MatrixFrame(self)
        self.matrix_frame.grid(row=1, column=0)
        self.boat_box = BoatBox(self)
        self.boat_box.grid(row=1, column=2, padx=20)

if __name__ == '__main__':
    app = MyWindow()
    app.mainloop()
