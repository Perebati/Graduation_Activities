#ok

import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Disciplina:
    def __init__(self, codigo, nome, cargaHoraria):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria

    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome
    
    def getCargaHoraria(self):
        return self.__cargaHoraria

class LimInsereDisciplinas(tk.Toplevel):
    def __init__(self, control):
        tk.Toplevel.__init__(self)
        self.title("Disciplina")
        self.control = control

        self.frameCargHr = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameCargHr.pack()
        self.frameButton.pack()

        self.labelCod = tk.Label(self.frameCodigo,text="Código: ")
        self.labelCod.pack(side="left")
        self.inputCod = tk.Entry(self.frameCodigo, width=20)
        self.inputCod.pack(side="left")

        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.labelCargaHr = tk.Label(self.frameCargHr,text="Carga horária: ")
        self.labelCargaHr.pack(side="left")
        self.inputCargaHr = tk.Entry(self.frameCargHr, width=20)
        self.inputCargaHr.pack(side="left")            
      
        self.botaoInserir = tk.Button(self.frameButton ,text="Adicionar")      
        self.botaoInserir.pack(side="left")
        self.botaoInserir.bind("<Button>", control.newDisc)

        self.botaoFechar = tk.Button(self.frameButton ,text="Concluído")      
        self.botaoFechar.pack(side="left")
        self.botaoFechar.bind("<Button>", control.close)
   
class CtrlDisciplina():

#Bloco de código relacionado a arquivos

    def __init__(self):
        if not os.path.isfile("classDisc.pickle"):
            self.listaDisciplina = []
        else:
            with open("classDisc.pickle", "rb") as f:
                self.listaDisciplina = pickle.load(f)

    def salvaDisciplinas(self):
        if len(self.listaDisciplina) != 0:
            with open("classDisc.pickle", "wb") as f:
                pickle.dump(self.listaDisciplina, f)

#Opereções básicas sobre a classe

    def getDisciplinas(self):
        return self.listaDisciplina

    def checkDisciplina(self, codDisciplina):
        for disciplina in self.listaDisciplina:
            if disciplina.getCodigo() == codDisciplina:
                return True
        return False    

    def getDisciplina(self, codDisciplina):
        disciplina = None
        for disc in self.listaDisciplina:
            if disc.getCodigo() == codDisciplina:
                disciplina = disc
        return disciplina

    def showDisciplinas(self):
        mensagem = 'Código - Nome - Carga Horária\n'
        for disciplina in self.listaDisciplina:
            mensagem += disciplina.getCodigo() + ' - ' \
                + disciplina.getNome() + ' - ' + disciplina.getCargaHoraria() + '\n'
        self.limiteLista = messagebox.showinfo("Lista das Diciplinas", mensagem)
    
#Opereções de edição da classe

    def adcDisciplina(self):
        self.limiteIns = LimInsereDisciplinas(self) 

    def newDisc(self, event):
        cargaHoraria = self.limiteIns.inputCargaHr.get()
        codDisciplina = self.limiteIns.inputCod.get()
        nomeDisciplina = self.limiteIns.inputNome.get()

        if self.checkDisciplina(codDisciplina):
            messagebox.showinfo("Erro", "Essa disciplina já existe no cadastro")
        else:
            if len(codDisciplina) == 0 or len(nomeDisciplina) == 0 or len(cargaHoraria) == 0:
               messagebox.showinfo("Erro","Há campos que não foram preenchidos")
            else:
                disciplina = Disciplina(codDisciplina, nomeDisciplina, cargaHoraria)
                self.listaDisciplina.append(disciplina)
                messagebox.showinfo("Sucesso","Disciplina cadastrada com sucesso")
                self.limiteIns.inputCod.delete(0, len(self.limiteIns.inputCod.get()))
                self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
                self.limiteIns.inputCargaHr.delete(0, len(self.limiteIns.inputCargaHr.get()))

    def close(self, event):
        self.limiteIns.destroy()