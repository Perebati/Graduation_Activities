import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
import os

class Playlist:

    def __init__(self, nome, listaMusicas):
        self.nome = nome
        self.listaMusicas = listaMusicas

    def getNome(self):
        return self.nome
    
    def getMusicas(self):
        return self.listaMusicas

class InserePlaylist(tk.Toplevel):
    def __init__(self, controle, listaArtistas):
        tk.Toplevel.__init__(self)
        self.geometry("350x250")
        
        self.title("Inserir Playlist")
        self.controle = controle
        self.listaArtistas = listaArtistas
        self.ultimoArtista = ""
    
        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)
        self.frame3 = tk.Frame(self)
        self.frame4 = tk.Frame(self)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()        

        self.labelNome = tk.Label(self.frame1,text="Nome da Playlist: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frame1, width=20)
        self.inputNome.pack(side="left")

        self.labelArtista = tk.Label(self.frame2, text="Artista: ")
        self.labelArtista.pack(side="left")
        self.inputArtista = tk.StringVar()
        self.combobox = ttk.Combobox(
            self.frame2, textvariable=self.inputArtista, state="readonly",
            values=self.listaArtistas)
        self.combobox.pack(side="left")
          
        self.labelMusicas = tk.Label(self.frame3,text="Músicas: ")
        self.labelMusicas.pack(side="left") 
        self.listaBox = tk.Listbox(self.frame3, width = 30)
        self.listaBox.pack(side="left")

        self.buttonCadMusic = tk.Button(self.frame4 ,text="Inserir música")           
        self.buttonCadMusic.pack(side="left")
        self.buttonCadMusic.bind("<Button>", controle.insereMusicaHandler)

        self.buttCad = tk.Button(self.frame4 ,text="Criar Playlist")           
        self.buttCad.pack(side="left")
        self.buttCad.bind("<Button>", controle.cadastrarPlaylistHandler) 

        self.buttConc = tk.Button(self.frame4, text = "Concluido")
        self.buttConc.pack(side = "left")
        self.buttConc.bind("<Button>", controle.concluidoCadastraPlaylist)  

class ConsultaPlaylist(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("250x50")
        self.title("Consultar Playlist")
        self.controle = controle

        self.frame3 = tk.Frame(self)
        self.frame4 = tk.Frame(self)
        self.frame3.pack()
        self.frame4.pack()

        self.labelTitulo = tk.Label(self.frame3, text = "Nome da Playlist: ")
        self.inputTitulo = tk.Entry(self.frame3, width = 20)
        self.labelTitulo.pack(side = "left")
        self.inputTitulo.pack(side = "left")

        self.buttConsultar = tk.Button(self.frame4, text = "Consultar")
        self.buttConsultar.pack()
        self.buttConsultar.bind("<Button>", controle.ConsultaPlaylistHandler)  

class ControlePlaylist:       
    def __init__(self, controlePrincipal):
        if not os.path.isfile("Playlist.pickle"):
            self.listaPlaylist = []
        else:
            with open("Playlist.pickle", "rb") as f:
                self.listaPlaylist = pickle.load(f)

        self.controlePrincipal = controlePrincipal
        self.controleArtista = controlePrincipal.controleArtista
        self.controleMusica = controlePrincipal.controleMusica
    
    def ConsultaPlaylist(self):
        self.limBuscplaylist = ConsultaPlaylist(self)

    def cadastraPlaylist(self):
        self.listaMuscEscolhida = []     
        self.listaArtistas = []
        for arti in self.controleArtista.getArtistas():
            self.listaArtistas.append(arti.getNome())
        self.limCadplaylist = InserePlaylist(self, self.listaArtistas)
    
    def cadastrarPlaylistHandler(self, event):
        nomePlaylist = self.limCadplaylist.inputNome.get()
        musicas = self.listaMuscEscolhida
        playlist = Playlist(nomePlaylist, musicas)
        self.listaPlaylist.append(Playlist)
        messagebox.showinfo("Sucesso","Playlist criada com sucesso")
        self.limCadplaylist.destroy()
    
    def insereMusicaHandler(self, event):
        musicaNome = self.limCadplaylist.listaBox.get(tk.ACTIVE)
        for musc in self.controleMusica.getMusicas():
            if musicaNome == musc.getTitulo():
                self.listaMuscEscolhida.append(musc)
                self.limCadplaylist.listaBox.delete(tk.ACTIVE)
            messagebox.showinfo("Sucesso", "Musica adicionada a playlist")
    
    def ConsultaPlaylistHandler(self, event):
        playlist = self.limBuscplaylist.inputTitulo.get()
        mensagem = ""
        for plst in self.listaPlaylist:
            if playlist == plst.getNome():
                mensagem += plst.getNome() + "\n"
                for mus in plst.getMusicas():
                    mensagem += mus.getNroFaixa() + " " + mus.getTitulo() + "\n"
                messagebox.showinfo("Sucesso",mensagem)
                return
        messagebox.showinfo("Erro","Playlist não encontrada")

    def concluidoCadastraPlaylist(self, event):
        self.limCadplaylist.destroy()
    
    def salvaPlaylist(self):
        if len(self.listaPlaylist) != 0:
            with open("Playlist.pickle", "wb") as f:
                pickle.dump(self.listaPlaylist, f)

    def atualizaListBox(self):
        listaMusicas = self.controleMusica.getMusicas()
        artistaSel = self.limCadplaylist.inputArtista.get()
        if  self.limCadplaylist.ultimoArtista != artistaSel:
            vetorMusicas = []
            self.limCadplaylist.listaBox.delete(0, tk.END)
            for mus in listaMusicas:
                if artistaSel == mus.getArtista().getNome(): 
                    if mus not in self.listaMuscEscolhida:
                        vetorMusicas.append(mus.getTitulo())
            for music in vetorMusicas:
                self.limCadplaylist.listaBox.insert(tk.END, music)  
            self.limCadplaylist.ultimoArtista = artistaSel

        self.controlePrincipal.root.after(100, self.atualizaListBox)
