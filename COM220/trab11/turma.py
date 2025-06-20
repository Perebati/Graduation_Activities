import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import estudante as est 
import disciplina as disc

class Turma:

    def __init__(self, codigo, disciplina, estudantes):
        self.__codigo = codigo
        self.__disciplina = disciplina
        self.__estudantes = estudantes

    def getCodigo(self):
        return self.__codigo
    
    def getDisciplina(self):
        return self.__disciplina

    def getEstudantes(self):
        return self.__estudantes


class LimiteInsereTurma(tk.Toplevel):
    def __init__(self, controle, listaCodDiscip, listaNroMatric):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Turma")
        self.controle = controle

        self.frameCodTurma = tk.Frame(self)
        self.frameDiscip = tk.Frame(self)
        self.frameEstudante = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodTurma.pack()
        self.frameDiscip.pack()
        self.frameEstudante.pack()
        self.frameButton.pack()        

        self.labelCodTurma = tk.Label(self.frameCodTurma,text="Informe o código da turma: ")
        self.labelCodTurma.pack(side="left")
        self.inputCodTurma = tk.Entry(self.frameCodTurma, width=20)
        self.inputCodTurma.pack(side="left")

        self.labelDiscip = tk.Label(self.frameDiscip,text="Escolha a disciplina: ")
        self.labelDiscip.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameDiscip, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCodDiscip
          
        self.labelEst = tk.Label(self.frameEstudante,text="Escolha o estudante: ")
        self.labelEst.pack(side="left") 
        self.listbox = tk.Listbox(self.frameEstudante)
        self.listbox.pack(side="left")
        for nro in listaNroMatric:
            self.listbox.insert(tk.END, nro)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Aluno")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereAluno)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Turma")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaTurma)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraTurmas():
    def __init__(self, str):
        messagebox.showinfo('Lista de turmas', str)

class ConsultaTurmas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consulta de turmas")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameButton.pack()

        self.labelCodDisc = tk.Label(self.frameNro,text="Cód da disciplina:")
        self.labelCodDisc.pack(side="left")

        self.inputCodDisc = tk.Entry(self.frameNro, width=20)
        self.inputCodDisc.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.checkTurma)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)


class CtrlTurma():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaTurmas = []

    def insereTurmas(self):        
        self.listaAlunosTurma = []
        listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        listaNroMatric = self.ctrlPrincipal.ctrlEstudante.getListaNroMatric()
        self.limiteIns = LimiteInsereTurma(self, listaCodDisc, listaNroMatric)

    def criaTurma(self, event):
        codTurma = self.limiteIns.inputCodTurma.get()
        discSel = self.limiteIns.escolhaCombo.get()
        disc = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(discSel)
        turma = Turma(codTurma, disc, self.listaAlunosTurma)
        self.listaTurmas.append(turma)
        self.limiteIns.mostraJanela('Sucesso', 'Turma criada com sucesso')
        self.limiteIns.destroy()

    def insereAluno(self, event):
        alunoSel = self.limiteIns.listbox.get(tk.ACTIVE)
        aluno = self.ctrlPrincipal.ctrlEstudante.getEstudante(alunoSel)
        self.listaAlunosTurma.append(aluno)
        self.limiteIns.mostraJanela('Sucesso', 'Aluno matriculado')
        self.limiteIns.listbox.delete(tk.ACTIVE)
        
    def mostraTurmas(self):
        str = ''
        for turma in self.listaTurmas:
            str += 'Código: ' + turma.getCodigo() + '\n'
            str += 'Disciplina: ' + turma.getDisciplina().getCodigo() + '\n'
            str += 'Estudantes:\n'
            for estud in turma.getEstudantes():
                str += estud.getNroMatric() + ' - ' + estud.getNome() + '\n'
            str += '------\n'

        self.limiteLista = LimiteMostraTurmas(str)

    def consultaTurmas(self):
        self.limiteIns = ConsultaTurmas(self)

    def checkTurma(self, event):
        codDisc = self.limiteIns.inputCodDisc.get()
        listaTurmas = ''
        flag = False
        for disc in self.listaTurmas:
            if disc.getDisciplina().getCodigo() == codDisc:
                listaTurmas += 'Código da turma: ' + disc.getCodigo() + '\n'
                flag = True
            
        if(flag == True):
            messagebox.showinfo("Turmas encontradas", listaTurmas)
            return
        else:
            messagebox.showinfo("Falha na busca!", "Não há turmas com essa disciplina!") 
            return
    
    def clearHandler(self, event):
        self.limiteIns.inputCodDisc.delete(0, len(self.limiteIns.inputCodDisc.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
     