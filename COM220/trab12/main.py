import tkinter as tk
import classAlun as classAlun
import classDisc as classDisc
import classGrad as classGrad
import classHist as classHist
import classCurs as classCurs

class ControlePrincipal():

    def __init__(self, root, controle):

        self.controle = controle
        self.root = root
        self.root.geometry('600x250')
        self.menubar = tk.Menu(self.root)        
        self.alunoMenu = tk.Menu(self.menubar)
        self.discMenu = tk.Menu(self.menubar)
        self.cursoMenu = tk.Menu(self.menubar)
        self.salvamentoMenu = tk.Menu(self.menubar)

        self.menubar.add_cascade(label="Aluno", \
                    menu=self.alunoMenu)
        self.alunoMenu.add_command(label="Cadastrar", \
                    command=self.controle.inserirAlunos)
        self.alunoMenu.add_command(label="Cadastrar disciplina", \
                    command=self.controle.inserirHistorico)
        self.alunoMenu.add_command(label="Consulta", \
                    command=self.controle.exibirHistorico) 

        self.menubar.add_cascade(label="Disciplina", \
                    menu=self.discMenu)  
        self.discMenu.add_command(label="Adicionar", \
                    command=self.controle.inserirDisciplinas)
        self.discMenu.add_command(label="Exibir", \
                    command=self.controle.mostrarDisciplinas)            

        self.menubar.add_cascade(label="Curso", \
                    menu=self.cursoMenu) 
        self.cursoMenu.add_command(label="Adicionar curso", \
                    command=self.controle.inserirCurso)
        self.cursoMenu.add_command(label="Adicionar grade", \
                    command=self.controle.inserirGrade)
        self.cursoMenu.add_command(label="Exibir curso", \
                    command=self.controle.mostrarCursos)
        self.cursoMenu.add_command(label="Exibir grade", \
                    command=self.controle.mostrarGrades)  
   
        self.menubar.add_cascade(label="Salvar", \
                    menu=self.salvamentoMenu)
        self.salvamentoMenu.add_command(label="Salvar", \
                    command=self.controle.salvaDados)

        self.root.config(menu=self.menubar)
      
class ControlPrincipal():   

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Sistema de cadastro escolar")
        self.ctrlAluno = classAlun.CtrlAluno(self)
        self.ctrlHistorico = classHist.CtrlHistorico(self)
        self.ctrlCurso = classCurs.CtrlCurso(self)
        self.ctrlGrade = classGrad.CtrlGrade(self)
        self.ctrlDisciplina = classDisc.CtrlDisciplina()
        
        self.limite = ControlePrincipal(self.root, self) 
        
        self.root.mainloop()
    
#Aluno
    def mostrarAlunos(self):
        self.ctrlAluno.mostrarAlunos()    
    def inserirAlunos(self):
        self.ctrlAluno.inserirAlunos()

#Grade
    def inserirGrade(self):
        self.ctrlGrade.adcGrade()

    def mostrarGrades(self):
        self.ctrlGrade.showGrade()

#Histórico
    def inserirHistorico(self):
        self.ctrlHistorico.inserirHistorico()

    def exibirHistorico(self):
        self.ctrlHistorico.historicoAluno()

#Disciplina
    def inserirDisciplinas(self):
        self.ctrlDisciplina.adcDisciplina()

    def mostrarDisciplinas(self):
        self.ctrlDisciplina.showDisciplinas()

#Curso
    def inserirCurso(self):
        self.ctrlCurso.adcCurso()

    def mostrarCursos(self):
        self.ctrlCurso.mostrarCursos()

#Arquivo
    def salvaDados(self):
        self.ctrlHistorico.salvaHistoricos()
        self.ctrlCurso.salvaCurso()
        self.ctrlDisciplina.salvaDisciplinas()
        self.ctrlAluno.salvaAlunos()
        self.ctrlGrade.salvaGrade()

if __name__ == '__main__':
    App = ControlPrincipal()