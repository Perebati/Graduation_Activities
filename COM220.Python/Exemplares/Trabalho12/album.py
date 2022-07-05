#Lucas Batista Pereira
#2020007290

#ok

import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Album:
    def __init__(self, titulo, ano, artista):
        self.__titulo = titulo
        self.__ano = ano
        self.__artista = artista
        self.__musicas = []
    
    def getTitulo(self):
        return self.__titulo

    def getAno(self):
        return self.__ano

    def getArttista(self):
        return self.__artista
    
    def getMusicas(self):
        return self.__musicas
    
    def addMusica(self, musica):
        self.__musicas.append(musica)

class InsereAlbum(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        
        self.geometry("300x100")
        self.title("Adicionar Álbum")
        self.controle = controle

        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)
        self.frame3 = tk.Frame(self)
        self.frame4 = tk.Frame(self)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

        self.labelTitulo = tk.Label(self.frame1, text = "Titulo : ")
        self.labelTitulo.pack(side = "left")
        self.inputTitulo = tk.Entry(self.frame1, width = 20)
        self.inputTitulo.pack(side = "left")

        self.labelAno = tk.Label(self.frame2, text = "Ano: ")
        self.labelAno.pack(side = "left")
        self.inputAno = tk.Entry(self.frame2, width = 20)
        self.inputAno.pack(side = "left")

        self.labelArtista = tk.Label(self.frame3, text = "Artista: ")
        self.labelArtista.pack(side = "left")
        self.inputArtista = tk.Entry(self.frame3, width = 20)
        self.inputArtista.pack(side = "left")

        self.button1 = tk.Button(self.frame4, text = "Cadastrar")
        self.button1.pack(side = "left")
        self.button1.bind("<Button>", controle.handlerCadatroAlbum)

        self.button2 = tk.Button(self.frame4, text = "Concluido")
        self.button2.pack(side = "left")
        self.button2.bind("<Button>", controle.concluidoInsereHandler)
    

class ConsultaAlbum(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("250x50")
        self.title("Consultar Álbum")
        self.controle = controle

        self.frame3 = tk.Frame(self)
        self.frame4 = tk.Frame(self)
        self.frame3.pack()
        self.frame4.pack()

        self.labelTitulo = tk.Label(self.frame3, text = "Titulo do Álbum: ")
        self.inputTitulo = tk.Entry(self.frame3, width = 20)
        self.labelTitulo.pack(side = "left")
        self.inputTitulo.pack(side = "left")

        self.button1 = tk.Button(self.frame4, text = "Consultar")
        self.button1.pack()
        self.button1.bind("<Button>", controle.HandlerConsultaAlbum)

class ControleAlbum:
    
    def __init__(self, controlePrincipal):
        if not os.path.isfile("album.pickle"):
            self.listaAlbuns = []
        else:
            with open("album.pickle", "rb") as f:
                self.listaAlbuns = pickle.load(f)
        
        self.controlePrincipal = controlePrincipal
        self.controleArtista = controlePrincipal.controleArtista
        self.controleMusica = controlePrincipal.controleMusica
    
    def getAlbums(self):
        return self.listaAlbuns

    def cadastraAlbum(self):
        self.LimiteCadastraAlbum = InsereAlbum(self)
    
    def consultaAlbum(self):
        self.limBuscaAlb = ConsultaAlbum(self)

    def handlerCadatroAlbum(self, event):
        titulo = self.LimiteCadastraAlbum.inputTitulo.get()
        ano = self.LimiteCadastraAlbum.inputAno.get()
        nomeArtista = self.LimiteCadastraAlbum.inputArtista.get()

        for art in self.controleArtista.getArtistas():
            if nomeArtista == art.getNome():
                album = Album(titulo, ano, art)
                self.listaAlbuns.append(album)
                art.addAlbum(album)
                messagebox.showinfo("Sucesso","Álbum cadastrado com sucesso")

                self.clearTitulo(event)
                self.clearAno(event)
                self.clearArtista(event)
                return

        messagebox.showinfo("Erro","Não foi possivel cadastrar o álbum")
    
    def HandlerConsultaAlbum(self, event):
        titulo = self.limBuscaAlb.inputTitulo.get()
        mensagem = ""
        flag = False

        for album in self.getAlbums():
            if titulo == album.getTitulo():
                flag = True
                mensagem += titulo + "\n"
                for musicas in album.getMusicas():
                    mensagem += musicas.getNroFaixa() + " - " + musicas.getTitulo() + "\n"
                messagebox.showinfo(mensagem, flag)
                self.clearTituloConsulta(event)
                return
        messagebox.showinfo("Erro", flag)
        self.clearTituloConsulta(event)
    
    def close(self, event):
        self.limBuscaAlb.destroy()

    def clearTitulo(self, event):
        self.LimiteCadastraAlbum.inputTitulo.delete(0, len(self.LimiteCadastraAlbum.inputTitulo.get()))
    
    def clearAno(self, event):
        self.LimiteCadastraAlbum.inputAno.delete(0, len(self.LimiteCadastraAlbum.inputAno.get()))
    
    def clearArtista(self, event):
        self.LimiteCadastraAlbum.inputArtista.delete(0, len(self.LimiteCadastraAlbum.inputArtista.get()))
    
    def clearTituloConsulta(self, event):
        self.limBuscaAlb.inputTitulo.delete(0, len(self.limBuscaAlb.inputTitulo.get()))

    def salvaAlbum(self):
        if len(self.listaAlbuns) != 0:
            with open("album.pickle", "wb") as f:
                pickle.dump(self.listaAlbuns, f)
    
    def concluidoInsereHandler(self, event):
        self.LimiteCadastraAlbum.destroy()
