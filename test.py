import tkinter as tk

class MyCanvas(tk.Canvas):
    def __init__(self, master, w= None, h= None):
        tk.Canvas.__init__(self, master)
        self.configure(width= w, height= h)
        self.configure(bg= 'yellow')
        self.create_text(w/2, h/2,  text= 'Ceci est un canevas !',
                                    font= ('Calibri', 30, 'bold'),
                                    fill= 'orange')

class MyButton(tk.Button):
    def __init__(self, master, t):
        self.text = t
        tk.Button.__init__(self, master, text= self.text)
        self.configure(width= 20, height= 2)
        self.configure(bg= 'green', fg= 'white')
        self.configure(font= ('Times New Roman', 20, 'italic'))
        self.configure(command= self.fonction)

    def fonction(self):
        print(f'Vous avez appuyé sur le bouton {self.text[1]}.')

class MyFrame(tk.Frame):
    def __init__(self, master,):
        tk.Frame.__init__(self, master, width= 100, height= 100)
        self.configure(bg= 'pink')
        self.button_list = [MyButton(self, text) for text in ('b1','b2', 'b3')]
        for k, button in enumerate(self.button_list):
            button.grid(row= k, column= 0, padx= 20, pady= 20)

class MyLabel(tk.Label):
    def __init__(self, master, t= None):
        tk.Label.__init__(self, master, width= 30, height= 2)
        self.configure(text= t)
        self.configure(bg= 'red', fg= 'brown')
        self.configure(font= ('Arial', 40))

class MyTk(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(bg= 'light blue')
##        self.state('zoomed')
        self.geometry('1000x800+400+0')
        self.title = MyLabel(self, t= "Exemple d'interface graphique")
        self.title.grid(row= 0, column= 0, columnspan= 2, padx= 20, pady= 20)
        self.menu = MyFrame(self)
        self.menu.grid(row= 1, column= 0, padx= 20, pady= 20)
        self.cnv = MyCanvas(self, w= 400, h= 300)
        self.cnv.grid(row= 1, column= 1, padx= 20, pady= 20)

if __name__ == '__main__':
    app = MyTk()
    app.mainloop()
