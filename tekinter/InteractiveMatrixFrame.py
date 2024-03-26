import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from Matrice import *

class InteractiveMatrixFrame(MatrixFrame):
    def __init__(self, master):
        super().__init__(master)

    def bind_click_event(self):
        self.canvas.bind("<Button-1>", self.on_click)  # Lier l'événement de clic de souris à la fonction on_click

    def on_click(self, event):
        # Récupérer les coordonnées du clic de souris
        x, y = event.x, event.y

        # Convertir les coordonnées en indices de ligne et de colonne
        row = y // 50
        col = x // 50

        # Afficher les coordonnées dans le terminal
        print("Coordonnées de la case sélectionnée : ", chr(65 + col), row + 1)


