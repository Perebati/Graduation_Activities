#ok

import tkinter as tk
from tkinter import messagebox
import os
import pickle

class Curso:
    def __init__(self, nome, grade):
        self.__nome = nome
        self.__grade = grade

    def getNome(self):
        return self.__nome
    
    def getGrade(self):
        return self.__grade

class LimAdcCurso(tk.Toplevel):
    def __init__(self, control):
        tk.Toplevel.__init__(self)
        self.title("Curso")
        self.control = control

        self.frameGrade = tk.Frame(self)
        self.frameButtom = tk.Frame(self)
        self.frameNomeCurso = tk.Frame(self)
        self.frameNomeCurso.pack()
        self.frameGrade.pack()
        self.frameButtom.pack()
      
        self.labelNome = tk.Label(self.frameNomeCurso,text="Nome: ")
        self.labelNome.pack(side="left") 
        self.inputNome = tk.Entry(self.frameNomeCurso, width=20)
        self.inputNome.pack(side="left") 

        self.labelGrades = tk.Label(self.frameGrade,text="Grade: ")
        self.labelGrades.pack(side="left")  
        self.inputGrade = tk.Entry(self.frameGrade, width=20)
        self.inputGrade.pack(side="left")  

        self.buttomClose = tk.Button(self.frameButtom ,text="Concluído")      
        self.buttomClose.pack(side="left")
        self.buttomClose.bind("<Button>", control.Close)

        self.buttomAdcCurso = tk.Button(self.frameButtom ,text="Adicionar Curso")      
        self.buttomAdcCurso.pack(side="left")
        self.buttomAdcCurso.bind("<Button>", control.newCurso) 

class CtrlCurso():
    def __init__(self, controle):

#Bloco de código relacionado a arquivos
        if not os.path.isfile("classCurs.pickle"):
            self.listaCursos = []
        else:
            with open("classCurs.pickle", "rb") as f:
                self.listaCursos = pickle.load(f)
        self.ctrlPrincipal = controle

    def salvaCurso(self):
        if len(self.listaCursos) != 0:
            with open("classCurs.pickle", "wb") as f:
                pickle.dump(self.listaCursos, f)
    
#Opereções básicas sobre a classe

    def checkCurso(self, nomeCurso): 
        for curso in self.listaCursos:
            if curso.getNome() == nomeCurso:
                return True
        return False
    
    def checkGrade(self, anoGrade):
        listaGrades = []
        listaGrades = self.ctrlPrincipal.ctrlGrade.getGrade()
        for grade in listaGrades:
            if grade.getAno() == anoGrade:
                return True
        return False

    def checkGradeDisponivel(self, anoGrade):    
        for curso in self.listaCursos:
            if curso.getGrade().getAno() == anoGrade:
                return True
        return False

    def getCurso(self, nome):
        cursoRet = None
        for curso in self.listaCursos:
            if curso.getNome() == nome:
                cursoRet = curso
        return cursoRet

    def getCursos(self):
        return self.listaCursos

    def mostrarCursos(self):
        mensagem = 'Curso - Grade\n'
        for curso in self.listaCursos:
            mensagem += curso.getNome() + " " + curso.getGrade().getAno() + "\n"
        messagebox.showinfo("Todos os cursos", mensagem)

#Opereções de edição da classe

    def adcCurso(self):
        self.limiteIns = LimAdcCurso(self)

    def newCurso(self, event):
        gradeEscolhida = self.limiteIns.inputGrade.get()
        grade = self.ctrlPrincipal.ctrlGrade.getGrades(gradeEscolhida)
        nome = self.limiteIns.inputNome.get()

        if self.checkCurso(nome):       
            messagebox.showinfo("Erro","Esse curso ja esta cadastrado")
        else:          
            if len(nome) == 0 or len(gradeEscolhida) == 0:
                messagebox.showinfo("Erro","Há campos que não foram preenchidos")
            else:
                if not self.checkGrade(gradeEscolhida):
                    messagebox.showinfo("Erro","Essa grade não está valida")
                else:
                    if self.checkGradeDisponivel(gradeEscolhida):
                        messagebox.showinfo("Erro","Essa grade já tem curso relacionado")
                    else:
                        curso = Curso(nome, grade)
                        self.listaCursos.append(curso)
                        messagebox.showinfo("Sucesso","Curso cadastrado")
                        
                        self.limiteIns.inputGrade.delete(0, len(self.limiteIns.inputGrade.get()))                        
                        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
            

    def Close(self, event):
        self.limiteIns.destroy()