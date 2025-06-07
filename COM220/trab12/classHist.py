#ok

import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Historico:
    def __init__(self, aluno, nota, disciplina):
        self.__aluno = aluno
        self.__nota = nota
        self.__disciplina = disciplina

    def getAluno(self):
        return self.__aluno

    def getNota(self):
        return self.__nota
    
    def getDisciplina(self):
        return self.__disciplina

class InserirDisciplinaHist(tk.Toplevel):
    def __init__(self, control):
        tk.Toplevel.__init__(self)
        self.title("Histórico")
        self.control = control

        self.frameAlu = tk.Frame(self)
        self.frameDisc = tk.Frame(self)
        self.frameNota = tk.Frame(self)
        self.frameButtom = tk.Frame(self)
        self.frameNota.pack()
        self.frameAlu.pack()
        self.frameDisc.pack()
        self.frameButtom.pack()

        self.labelAlu = tk.Label(self.frameAlu,text="Matrícula aluno: ")
        self.labelAlu.pack(side="left")
        self.inputAluno = tk.Entry(self.frameAlu, width=20)
        self.inputAluno.pack(side="left")

        self.labelDisciplina = tk.Label(self.frameDisc,text="Disciplina: ")
        self.labelDisciplina.pack(side="left")
        self.inputDisciplina = tk.Entry(self.frameDisc, width=20)
        self.inputDisciplina.pack(side="left") 

        self.labelNota = tk.Label(self.frameNota,text="Nota: ")
        self.labelNota.pack(side="left")  
        self.inputNota = tk.Entry(self.frameNota, width=20)
        self.inputNota.pack(side="left")             
      
        self.botaoCriar = tk.Button(self.frameButtom ,text="Inserir")      
        self.botaoCriar.pack(side="left")
        self.botaoCriar.bind("<Button>", control.newHist)

        self.botaoClose = tk.Button(self.frameButtom ,text="Concluído")      
        self.botaoClose.pack(side="left")
        self.botaoClose.bind("<Button>", control.Close)

    def exibeJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ExibirHist(tk.Toplevel):
    def __init__(self, control):
        
        tk.Toplevel.__init__(self)
        self.title("Histórico do Aluno")
        self.control = control

        self.frameAlu = tk.Frame(self)
        self.frameButtom = tk.Frame(self)

        self.frameAlu.pack()
        self.frameButtom.pack()

        self.labelAlu = tk.Label(self.frameAlu,text="Matrícula: ")
        self.labelAlu.pack(side="left")
        self.inputAluno = tk.Entry(self.frameAlu, width=20)
        self.inputAluno.pack(side="left")      
      
        self.botaoCriar = tk.Button(self.frameButtom ,text="Emitir histórico")      
        self.botaoCriar.pack(side="left")
        self.botaoCriar.bind("<Button>", control.showHistorico)
   
class CtrlHistorico():
    def __init__(self, controlPrincipal):

#Bloco de código relacionado a arquivos
        if not os.path.isfile("classHist.pickle"):
            self.listaHist = []
        else:
            with open("classHist.pickle", "rb") as f:
                self.listaHist = pickle.load(f)
        self.ctrlPrincipal = controlPrincipal

    def salvaHistoricos(self):
        if len(self.listaHist) != 0:
            with open("classHist.pickle", "wb") as f:
                pickle.dump(self.listaHist, f)

#Opereções básicas sobre a classe

    def getHistorico(self, matricAluno):
        historico = None
        for hist in self.listaHist:
            if hist.getAluno().getmatricula_aluno == matricAluno:
                historico = hist
        return historico

    def verificaCampoAluno(self, numMatric):
        listaAlunos = []
        listaAlunos = self.ctrlPrincipal.ctrlAluno.getAlunos()

        for aluno in listaAlunos:
            if aluno.getmatricula_aluno() == numMatric:
                return True
        return False

    def verificaCampoDisciplina(self, codDisc):
        listaDisciplinas = []
        listaDisciplinas = self.ctrlPrincipal.ctrlDisciplina.getDisciplinas()

        for disciplina in listaDisciplinas:
            if disciplina.getCodigo() == codDisc:
                return True
        return False
    
    def verificaHistorico(self, numMatric):
        for historico in self.listaHist:
            if historico.getAluno() == numMatric:
                return True
        return False

    def historicoAluno(self):
        self.limiteMos = ExibirHist(self) 

    def showHistorico(self, event):
        matricula = self.limiteMos.inputAluno.get()
        if not self.verificaCampoAluno(matricula):
            messagebox.showinfo("Erro", "Aluno não cadastrado")
        else:
            hrsObri = 0
            hrsElet = 0
            mensagem = 'Matrícula | Nota | Disciplina | Resultado\n'

            for historico in self.listaHist:
                obrigatoria = False
                cargaHrDisc = 0
                if historico.getAluno().getmatricula_aluno() == matricula:
                    
                    for disciplina in historico.getAluno().getCurso().getGrade().getDisciplinas():
                        if historico.getDisciplina().getCodigo() == disciplina.getCodigo():
                            obrigatoria = True
                            cargaHrDisc = float(disciplina.getCargaHoraria())
                    
                    if obrigatoria:
                        hrsObri += cargaHrDisc
                    else:
                        hrsElet += float(historico.getDisciplina().getCargaHoraria())
                    if float(historico.getNota()) >= 6.0:
                        mensagem += historico.getAluno().getmatricula_aluno() + ' - ' \
                            + historico.getNota() + ' - ' + historico.getDisciplina().getCodigo() + ' -> Aprovado' + '\n'
                    else:
                        mensagem += historico.getAluno().getmatricula_aluno() + ' - ' \
                            + historico.getNota() + ' - ' + historico.getDisciplina().getCodigo() + ' -> Reprovado' + '\n'
            
            mensagem += '\nTotal obrigatória (horas): ' + str(hrsObri) + '\n'
            mensagem += 'Total eletiva (horas): ' + str(hrsElet) + '\n'
            messagebox.showinfo("Aluno", mensagem)
    
#Opereções de edição da classe

    def newHist(self, event):
        alunoEsc = self.limiteIns.inputAluno.get()
        aluno = self.ctrlPrincipal.ctrlAluno.getAluno(alunoEsc)
        nota = self.limiteIns.inputNota.get()
        discEsc = self.limiteIns.inputDisciplina.get()
        disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(discEsc)
        validado = True

        if self.verificaHistorico(alunoEsc):
            messagebox.showinfo("Aluno", "O aluno já possui historico")
        else:
            if not self.verificaCampoAluno(alunoEsc):
                messagebox.showinfo("Erro", "Matricula invalida")
                validado = False
            if not self.verificaCampoDisciplina(discEsc):
                messagebox.showinfo("Erro", "Codigo de disciplina invalido")
                validado = False
            if len(alunoEsc) == 0 or len(discEsc) == 0 or len(nota) == 0:
                messagebox.showinfo("Erro", "Há campos não preenchidos")
                validado = False
            if validado:
                historico = Historico(aluno, nota, disciplina)
                self.listaHist.append(historico)
                messagebox.showinfo("Sucesso", "Aluno cadastrado")
        
        self.limiteIns.inputAluno.delete(0, len(self.limiteIns.inputAluno.get()))
        self.limiteIns.inputDisciplina.delete(0, len(self.limiteIns.inputDisciplina.get()))        
        self.limiteIns.inputNota.delete(0, len(self.limiteIns.inputNota.get()))
     
    def inserirHistorico(self):
        self.limiteIns = InserirDisciplinaHist(self) 

    def Close(self, event):
        self.limiteIns.destroy()