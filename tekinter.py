import tkinter

class MyCanvas (tkinter.Canvas) :
    def __init__ (self, h, w):
        tkinter.Canvas.__init__(self)
        self.configure(height= h)
        self.configure(width= w)
        self.configure (bg= 'white')
        
class MyWindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        cnv = MyCanvas(800, 800)
        cnv.grid()

app = MyWindow()
app.mainloop()

#python3 tekinter.py