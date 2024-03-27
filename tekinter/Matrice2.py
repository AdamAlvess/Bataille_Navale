import tkinter as tk

class Matrix2Frame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg='white')
        self.canvas = tk.Canvas(self, width=550, height=550)
        self.canvas.grid(row=0, column=0, padx=20, pady=20)
        self.draw_matrix()
        self.bind_click_event()

    def draw_matrix(self):
        for i in range(10):
            label = tk.Label(self.canvas, text=chr(65 + i), font=('Arial', 12))
            label.place(x=i * 50 + 40, y=0)  

        for j in range(10):
            label = tk.Label(self.canvas, text=str(j+1), font=('Arial', 12))
            label.place(x=5, y=j * 50 + 40) 

        for i in range(10):
            for j in range(10):
                x0 = j * 50 + 25
                y0 = i * 50 + 25
                x1 = x0 + 50
                y1 = y0 + 50
                self.canvas.create_rectangle(x0, y0, x1, y1, outline='white')

    def bind_click_event(self):
        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        # Récupérer les coordonnées du clic de souris
        x, y = event.x + 25, event.y + 25

        # Convertir les coordonnées en indices de ligne et de colonne
        row = y // 50
        col = x // 50

        print("Coordonnées de la case sélectionnée : ", chr(64 + col), row)
