#Lucas Batista Pereira
#p2

import tkinter as tk
import vinho as Vinho

class MenuPrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
    
        self.root.geometry("600x250")
        self.menu = tk.Menu(self.root)
        self.cadastroMenu = tk.Menu(self.menu)
        self.consultaMenu = tk.Menu(self.menu)

        self.menu.add_cascade(label = "Cadastro", \
            menu = self.cadastroMenu)
        self.cadastroMenu.add_command(label = "Cadastrar vinho", \
            command=self.controle.inserirVinho)

        self.menu.add_cascade(label = "Consulta", \
            menu = self.consultaMenu)
        self.consultaMenu.add_command(label = "Consultar vinho", \
            command=self.controle.consultaVinho)

        self.root.config(menu=self.menu)

class ControlePrincipal():
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Sistema de Cadastro/Consulta de vinhos")
        self.ctrlVinho = Vinho.CtrlVinho(self)

        self.limite = MenuPrincipal(self.root, self)

        self.root.mainloop()

#triggers aqui
    def inserirVinho(self):
        self.ctrlVinho.inserirVinhos()

    
    def consultaVinho(self):
        self.ctrlVinho.consultaVinhos()


if __name__ == '__main__':
    App = ControlePrincipal()