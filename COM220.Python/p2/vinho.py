import tkinter as tk
from tkinter import Variable, ttk
from tkinter import messagebox
from typing import Text

class TipoErrado(Exception):
    pass

class VariedadeErrada(Exception):
    pass

class OrigemErrada(Exception):
    pass

class Vinho:
    def __init__(self, codigo, nome, tipo, variedade, origem, preco):
        self.__codigo = codigo
        self.__nome = nome
        self.__tipo = tipo
        self.__variedade = variedade
        self.__origem = origem
        self.__preco = preco

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getTipo(self):
        return self.__tipo

    def getVariedade(self):
        return self.__variedade
    
    def getOrigem(self):
        return self.__origem
    
    def getPreco(self):
        return self.__preco
    
class LimCadastroVinho(tk.Toplevel):
    def __init__(self, control):
        tk.Toplevel.__init__(self)

        self.title("Cadastro de Vinho")
        self.control = control

        self.frameCodigo = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameTipo = tk.Frame(self)
        self.frameVariedade = tk.Frame(self)
        self.frameOrigem = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameTipo.pack()
        self.frameVariedade.pack()
        self.frameOrigem.pack()
        self.framePreco.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text = "Código: ")
        self.labelCodigo.pack(side = "left")
        self.inputCodigo = tk.Entry(self.frameCodigo, width = 20)
        self.inputCodigo.pack(side = "left")

        self.labelNome = tk.Label(self.frameNome, text = "Nome: ")
        self.labelNome.pack(side = "left")
        self.inputNome = tk.Entry(self.frameNome, width = 20)
        self.inputNome.pack(side = "left")

        self.labelTipo = tk.Label(self.frameTipo, text = "Tipo: ")
        self.labelTipo.pack(side = "left")
        self.inputTipo = tk.Entry(self.frameTipo, width = 20)
        self.inputTipo.pack(side = "left")

        self.labelVariedade = tk.Label(self.frameVariedade, text = "Variedade: ")
        self.labelVariedade.pack(side = "left")
        self.inputVariedade = tk.Entry(self.frameVariedade, width = 20)
        self.inputVariedade.pack(side = "left")

        self.labelOrigem = tk.Label(self.frameOrigem, text = "Origem: ")
        self.labelOrigem.pack(side = "left")
        self.inputOrigem = tk.Entry(self.frameOrigem, width = 20)
        self.inputOrigem.pack(side = "left")

        self.labelPreco = tk.Label(self.framePreco, text = "Preço: ")
        self.labelPreco.pack(side = "left")
        self.inputPreco = tk.Entry(self.framePreco, width = 20)
        self.inputPreco.pack(side = "left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="Adicionar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", control.adcVinho)

        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", control.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", control.fechar)

class LimConsultaVinhos(tk.Toplevel):
    def __init__(self, control):
        tk.Toplevel.__init__(self)
        self.title("Consulta de Vinho")
        self.control = control
    
        self.frameCombo = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCombo.pack()
        self.frameButton.pack()

        self.escolhaCombo1 = tk.StringVar()
        self.combobox1 = ttk.Combobox(self.frameCombo, width = 15 , textvariable = self.escolhaCombo1)
        self.combobox1.pack(side="left")
        self.combobox1['values'] = self.control.listaTipos()

        self.escolhaCombo2 = tk.StringVar()
        self.combobox2 = ttk.Combobox(self.frameCombo, width = 15 , textvariable = self.escolhaCombo2)
        self.combobox2.pack(side="left")
        self.combobox2['values'] = self.control.listaVariedade()

        self.buttonSubmit = tk.Button(self.frameButton ,text="Pesquisar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", control.pesquisarVinhos)


class CtrlVinho():
    def __init__(self, controlePrincipal):
        self.listaVinhos = []
        self.verifTipo = ["Branco", "Tinto", "Rose", "Espumante"]
        self.verifVariedade = ["Cabernet Sauvignon", "Carmenere", "Merlot", "Malbec", "Sauvignon Blanc", "Pinot Grigio"]
        self.verifOrigem = ["Brasil", "Argentina", "Chile", "Itália", "França", "Portugal", "África do Sul"]

    def inserirVinhos(self):
        self.limiteIns = LimCadastroVinho(self) 

    def verificaDados(self, tipo, variedade, origem):
        try:
            if tipo not in self.verifTipo:
                raise TipoErrado()
            elif variedade not in self.verifVariedade:
                raise VariedadeErrada()
            elif origem not in self.verifOrigem:
                raise OrigemErrada()
        
        except TipoErrado:
            messagebox.showinfo("Entrada Errada","O tipo desse vinho não existe no registro")
            return False
        except VariedadeErrada:
            messagebox.showinfo("Entrada Errada","A variedade desse vinho não existe no registro")
            return False
        except OrigemErrada:
            messagebox.showinfo("Entrada Errada","A origem desse vinho não existe no registro")
            return False
        
        else:
            return True

    def clearHandler(self,event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))                    
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputTipo.delete(0, len(self.limiteIns.inputTipo.get()))
        self.limiteIns.inputVariedade.delete(0, len(self.limiteIns.inputVariedade.get()))
        self.limiteIns.inputOrigem.delete(0, len(self.limiteIns.inputOrigem.get()))
        self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))

    def adcVinho(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        tipo = self.limiteIns.inputTipo.get()
        varidade = self.limiteIns.inputVariedade.get()
        origem = self.limiteIns.inputOrigem.get()
        preco = self.limiteIns.inputPreco.get()

        if self.verificaDados(tipo, varidade, origem) == False:
            self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))                    
            self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
            self.limiteIns.inputTipo.delete(0, len(self.limiteIns.inputTipo.get()))
            self.limiteIns.inputVariedade.delete(0, len(self.limiteIns.inputVariedade.get()))
            self.limiteIns.inputOrigem.delete(0, len(self.limiteIns.inputOrigem.get()))
            self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))
            return

        vinho = Vinho(codigo, nome, tipo, varidade, origem, preco)
        self.listaVinhos.append(vinho)

        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))                    
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputTipo.delete(0, len(self.limiteIns.inputTipo.get()))
        self.limiteIns.inputVariedade.delete(0, len(self.limiteIns.inputVariedade.get()))
        self.limiteIns.inputOrigem.delete(0, len(self.limiteIns.inputOrigem.get()))
        self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))

        messagebox.showinfo("Sucesso","Vinho cadastrado com sucesso")
        return

    def listaTipos(self):
        vetorTipos = ["---"]
        for tipos in self.listaVinhos:
            if tipos.getTipo() not in vetorTipos:
                vetorTipos.append(tipos.getTipo())
        return vetorTipos

    def listaVariedade(self):
        vetorVariedade = ["---"]
        for vari in self.listaVinhos:
            if vari.getVariedade() not in vetorVariedade:
                vetorVariedade.append(vari.getVariedade())
        return vetorVariedade

    def consultaVinhos(self):
        self.limiteIns = LimConsultaVinhos(self) 

    def pesquisarVinhos(self, event):
        mensagem = "Codigo | Nome | Tipo | Variedade | Origem | Preco |"
        tipo = self.limiteIns.escolhaCombo1.get()
        variedade = self.limiteIns.escolhaCombo2.get()

    
        if(tipo == "---" and variedade == "---"):
            messagebox.showinfo("Erro","Deve haver um parametro de busca")
            return
        elif(tipo != "---" and variedade != "---"):
            messagebox.showinfo("Erro","Deve haver apenas um parametro de busca")
            return
        elif(tipo != "---" and variedade == "---"):
            self.limiteIns.escolhaCombo2.set("---")
            for tip in self.listaVinhos:
                if tip.getTipo() == tipo:
                    mensagem += "\n" + str(tip.getCodigo()) + " - " + tip.getNome() + " - " + tip.getTipo() + " - " \
                        + tip.getVariedade() + " - " + tip.getOrigem() + " - " + str(tip.getPreco())
            
            messagebox.showinfo("Lista de vinhos", mensagem)    
            return
        elif(tipo == "---" and variedade != "---"):
            self.limiteIns.escolhaCombo1.set("---")
            for var in self.listaVinhos:
                if var.getVariedade() == variedade:
                    mensagem += "\n" + str(var.getCodigo()) + " - " + var.getNome() + " - " + var.getTipo() + " - " \
                        + var.getVariedade() + " - " + var.getOrigem() + " - " + str(var.getPreco())

            messagebox.showinfo("Lista de vinhos", mensagem)
            return

    def fechar(self, event):
        self.limiteIns.destroy()