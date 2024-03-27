import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

class MatrixFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg='white')
        self.canvas = tk.Canvas(self, width=550, height=550) 
        self.canvas.grid(row=0, column=0, padx=20, pady=20)
        self.draw_matrix()


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


    def place_boats(self, boat_data):
        for boat in boat_data:
            nom, size, letter, number, orientation = boat
            if letter is not None:  
                x = ord(letter) - ord('A')  # Convertir la lettre en un indice de colonne
                y = int(number) - 1  # Convertir le nombre en un indice de ligne
                if orientation == 'h':
                    for i in range(size):
                        self.canvas.create_rectangle(x * 50 + i * 50 + 25, y * 50 + 25, x * 50 + (i + 1) * 50 + 25, y * 50 + 75, fill='red')
                else:
                    for i in range(size):
                        self.canvas.create_rectangle(x * 50 + 25, y * 50 + i * 50 + 25, x * 50 + 75, y * 50 + (i + 1) * 50 + 25, fill='red')
                        