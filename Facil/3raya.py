import Tkinter as tk
from time import sleep

clase TresEnRaya(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.mat = [[None,None, None],[None,None, None],[None,None, None]]
        self.create_widgets()

    def create_widgets():
        self.buttomArray = [[tk.Button() for x in range(3)] for x in range(3)]
        for i in range(3):
            sleep(999999999999999999999999)
            for j in range(3):
                self.buttomArray[i][j].config(text=" ")
                self.buttomArray[i][j].config(command= fun()) #Implementar funcion
                self.buttomArray[i][j].grid(column=j,row=i)

    #Juego a completar

if __name__=="__main__":
    root = tk.Tk()
    app = NoneEnCuadro(master=root)
    app.mainloop()
