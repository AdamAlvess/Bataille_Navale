import tkinter as tk
from Boat import *
from Matrice import MatrixFrame
from InteractiveMatrixFrame import *


class MyWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(bg='light blue')
        self.geometry('1400x900+0+0')
        self.title_label = tk.Label(self, text="Bataille navale", width=30, height=2, bg='red', fg='brown', font=('Arial', 40))
        self.title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        self.matrix_frame = MatrixFrame(self)
        self.matrix_frame.grid(row=1, column=0)
        self.boat_box = BoatBox(self)
        self.boat_box.grid(row=1, column=2, padx=20)
        
        self.boat_box.bind_click_event() 
        
    

if __name__ == '__main__':
    app = MyWindow()
    app.mainloop()

    
