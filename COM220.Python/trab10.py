#Nome: Lucas Batista Pereira
#Matricula: 2020007290
#COM 220
#TRAB 10

import tkinter as tk
from tkinter import messagebox

class ModelCliente():
    def __init__(self, nome, email, codigo):
        self.__nome = nome
        self.__email = email
        self.__codigo = codigo

    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email

    def getCodigo(self):
        return self.__codigo

class View():
    def __init__(self, master, controller):                             #Por enquanto achei melhor organizar as linhas com varios frames
        self.controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()
        self.frame0 = tk.Frame(self.janela)
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)
        self.frame4 = tk.Frame(self.janela)
        self.frame5 = tk.Frame(self.janela)
        self.frame6 = tk.Frame(self.janela)
        self.frame7 = tk.Frame(self.janela)
        self.frame0.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()
      
        self.labelInfo0 = tk.Label(self.frame0, text="Cadastrar:")
        self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2,text="Email: ")
        self.labelInfo3 = tk.Label(self.frame3,text="Código: ")
        self.labelInfo4 = tk.Label(self.frame5,text="Pesquisar: ")
        self.labelInfo5 = tk.Label(self.frame6,text="Código: ")
        self.labelInfo0.pack(side="left")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left") 
        self.labelInfo3.pack(side="left") 
        self.labelInfo4.pack(side="left")
        self.labelInfo5.pack(side="left")

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")
        self.inputText3 = tk.Entry(self.frame3, width=20)
        self.inputText3.pack(side="left")
        self.inputText4 = tk.Entry(self.frame6, width=20)
        self.inputText4.pack(side="left")                
      
        self.buttonSubmit = tk.Button(self.frame4,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.enterHandler)
      
        self.buttonClear = tk.Button(self.frame4,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler) 

        self.buttonSearch = tk.Button(self.frame7,text="Search")      
        self.buttonSearch.pack(side="left")
        self.buttonSearch.bind("<Button>", controller.procurarCodigo) 

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)
      
class Controller():       
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x200')
        self.listaClientes = []

        self.view = View(self.root, self) 
        self.root.title("Cadastro/Pesquisa")
        self.root.mainloop()

    def enterHandler(self, event):
        nomeCli = self.view.inputText1.get()
        emailCli = self.view.inputText2.get()
        codigoCLi = self.view.inputText3.get()
        cliente = ModelCliente(nomeCli, emailCli, codigoCLi)
        self.listaClientes.append(cliente)
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))
        self.view.inputText3.delete(0, len(self.view.inputText3.get()))

    def procurarCodigo(self, event):                                    #Metodo de pesquisa por cliente                                  
        codigoCLi = self.view.inputText4.get()
        for codigo in self.listaClientes:
            if codigo.getCodigo() ==  codigoCLi:
                self.view.mostraJanela("Cliente", (codigo.getNome(),codigo.getEmail()))
                self.clearHandler(event)
                return True
        self.view.mostraJanela('Falha', 'Cliente não está cadastrado!')
        self.clearHandler(event)
        return False

if __name__ == '__main__':
    c = Controller()