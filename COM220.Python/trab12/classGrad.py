#ok

import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Grade:
    def __init__(self, ano, disciplinas):
        self.__ano = ano
        self.__disciplinas = disciplinas

    def getAno(self):
        return self.__ano
    
    def getDisciplinas(self):
        return self.__disciplinas

class LimAdcGrade(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.title("Grade")
        self.controle = controle

        self.frameAno = tk.Frame(self)
        self.frameDisc = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameAno.pack()
        self.frameDisc.pack()
        self.frameButton.pack()

        self.labelDisc = tk.Label(self.frameDisc,text="Código da disciplina: ")
        self.labelDisc.pack(side="left") 
        self.inputDisc = tk.Entry(self.frameDisc, width=20)
        self.inputDisc.pack(side="left")

        self.labelAno = tk.Label(self.frameAno, text="Ano da disciplina: ")
        self.labelAno.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")

        self.buttomAdcDisc = tk.Button(self.frameButton, text="Adicionar disciplina")      
        self.buttomAdcDisc.pack(side="left")
        self.buttomAdcDisc.bind("<Button>", controle.newDisciplinas)

        self.buttomAdcGrade = tk.Button(self.frameButton, text="Adicionar grade")      
        self.buttomAdcGrade.pack(side="left")
        self.buttomAdcGrade.bind("<Button>", controle.newGrade)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.close)  


class CtrlGrade():

#Bloco de código relacionado a arquivos

    def __init__(self, controlePrincipal):
        if not os.path.isfile("classGrad.pickle"):
            self.listaGrades = []
        else:
            with open("classGrad.pickle", "rb") as f:
                self.listaGrades = pickle.load(f)
        self.ctrlPrincipal = controlePrincipal
        self.discDaGrade = []
    
    def salvaGrade(self):
        if len(self.listaGrades) != 0:
            with open("classGrad.pickle", "wb") as f:
                pickle.dump(self.listaGrades, f)

#Opereções básicas sobre a classe

    def getGrade(self):
        return self.listaGrades

    def checkGrade(self, ano):
        for grade in self.listaGrades:
            if grade.getAno() == ano:
                return True
        return False

    def checkDisciplina(self, codigo_disciplina):
        listaDisciplinas = self.ctrlPrincipal.ctrlDisciplina.getDisciplinas()
        for disciplina in listaDisciplinas:
            if disciplina.getCodigo() == codigo_disciplina:
                return True
        return False

    def getGrades(self, gradeAno):
        grade = None
        for g in self.listaGrades:
            if g.getAno() == gradeAno:
                grade = g
        return grade

    def showGrade(self):
        mensagem = ''
        for grade in self.listaGrades:
            mensagem += 'Ano da grade: ' + grade.getAno() + '\n'
            for disciplina in grade.getDisciplinas():
                mensagem += disciplina.getCodigo() + ' - ' + disciplina.getNome()  +  ' - ' + disciplina.getCargaHoraria() + '\n' 
        messagebox.showinfo("Todas as grades", mensagem)

#Opereções de edição da classe

    def newGrade(self, event):
        ano = self.limiteIns.inputAno.get()
        if self.checkGrade(ano):
            messagebox.showinfo("Erro", "Essa grade já existe no sistema")
        else:
            if len(ano) == 0 or len(self.discDaGrade) == 0:
                messagebox.showinfo("Erro", "Há campos que não foram preenchidos")
            else:
                grade = Grade(ano, self.discDaGrade)
                messagebox.showinfo("Sucesso", "Grade cadastrada com sucesso")
                self.listaGrades.append(grade)

                self.limiteIns.inputDisc.delete(0, len(self.limiteIns.inputDisc.get()))
                self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))

    def adcGrade(self):
        self.discDaGrade = []
        self.limiteIns = LimAdcGrade(self)
    
    def newDisciplinas(self, event):
        codDisc = self.limiteIns.inputDisc.get()
        if len(codDisc) == 0:
            messagebox.showinfo("Erro", "Há campos que não foram preenchidos")
        else:
            if not self.checkDisciplina(codDisc):
                messagebox.showinfo("Erro", "Essa disciplina não existe no cadastro")
            else:
                disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(codDisc)
                
                self.discDaGrade.append(disciplina)
                messagebox.showinfo("Sucesso", "Disciplina cadastrada")

                self.limiteIns.inputDisc.delete(0, len(self.limiteIns.inputDisc.get()))
    
    def close(self, event):
        self.limiteIns.destroy()