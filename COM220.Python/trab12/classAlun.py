import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Aluno:
    def __init__(self, matricula_aluno, nome, curso):
        self.__matricula_aluno = matricula_aluno
        self.__nome = nome
        self.__curso = curso

    def getmatricula_aluno(self):
        return self.__matricula_aluno
    
    def getNome(self):
        return self.__nome
    
    def getCurso(self):
        return self.__curso

class LimInsereAlunos(tk.Toplevel):
    def __init__(self, control):
        tk.Toplevel.__init__(self)
        self.title("Aluno")
        self.control = control

        self.frameMatricula = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameNomeAluno = tk.Frame(self)
        
        self.frameMatricula.pack()
        self.frameNomeAluno.pack()
        self.frameCurso.pack()
        self.frameBotao.pack()
      
        self.labelMatricula = tk.Label(self.frameMatricula,text="Matrícula: ")
        self.labelMatricula.pack(side="left")
        self.inputMatricula = tk.Entry(self.frameMatricula, width=20)
        self.inputMatricula.pack(side="left")

        self.labelNome = tk.Label(self.frameNomeAluno,text="Nome: ")
        self.labelNome.pack(side="left")  
        self.inputNome = tk.Entry(self.frameNomeAluno, width=20)
        self.inputNome.pack(side="left") 

        self.labelCurso = tk.Label(self.frameCurso,text="Curso: ")
        self.labelCurso.pack(side="left")
        self.inputCurso = tk.Entry(self.frameCurso, width=20)
        self.inputCurso.pack(side="left") 

        self.buttonSubmit = tk.Button(self.frameBotao ,text="Adicionar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", control.criaAluno)

        self.buttonFecha = tk.Button(self.frameBotao ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", control.fechar)

class CtrlAluno():     
    def __init__(self, controlPrincipal):
        if not os.path.isfile("classAlun.pickle"):
            self.listaALunos = []
        else:
            with open("classAlun.pickle", "rb") as f:
                self.listaALunos = pickle.load(f)
        
        self.ctrlPrincipal = controlPrincipal

    def salvaAlunos(self):
        if len(self.listaALunos) != 0:
            with open("classAlun.pickle", "wb") as f:
                pickle.dump(self.listaALunos, f)

    def getAlunos(self):
        return self.listaALunos

    def inserirAlunos(self):
        self.limiteIns = LimInsereAlunos(self) 

    def verificaAluno(self, matricula_aluno):
        for aluno in self.listaALunos:
            if aluno.getmatricula_aluno() == matricula_aluno:
                return True
        return False

    def getAluno(self, matricula_aluno):
        aluno = None
        for a in self.listaALunos:
            if a.getmatricula_aluno() == matricula_aluno:
                aluno = a
        return aluno

    def verifCurso(self, nome_curso):
        listaCursos = []
        listaCursos = self.ctrlPrincipal.ctrlCurso.getCursos()
        for curso in listaCursos:
            if curso.getNome() == nome_curso:
                return True
        return False

    def mostrarAlunos(self):
        mensagem = 'Matrícula | Nome | Curso\n'
        for est in self.listaALunos:
            mensagem += '\n' + est.getmatricula_aluno() + ' - ' + est.getNome() + ' - ' + est.getCurso().getNome()
        messagebox.showinfo("Lista de Alunos", mensagem)

    def criaAluno(self, event):
        curso_selecionado = self.limiteIns.inputCurso.get()
        curso = self.ctrlPrincipal.ctrlCurso.getCurso(curso_selecionado)
        matricula_aluno = self.limiteIns.inputMatricula.get()
        nome = self.limiteIns.inputNome.get()
        aluno = Aluno(matricula_aluno, nome, curso)

        if self.verificaAluno(matricula_aluno):
            messagebox.showinfo("Erro", "Aluno já cadastrado")
        else:
            if len(matricula_aluno) == 0 or len(nome) == 0 or len(curso_selecionado) == 0:
                messagebox.showinfo("Erro", "Há campos não preenchidos")
            else:
                if not self.verifCurso(curso_selecionado):
                    messagebox.showinfo("Erro", "Cruso nao existe")
                else:
                    self.listaALunos.append(aluno)
                    messagebox.showinfo("Sucesso", "Aluno cadastrado")
                    self.limiteIns.inputMatricula.delete(0, len(self.limiteIns.inputMatricula.get()))
                    self.limiteIns.inputCurso.delete(0, len(self.limiteIns.inputCurso.get()))                    
                    self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
    def fechar(self, event):
        self.limiteIns.destroy()
    