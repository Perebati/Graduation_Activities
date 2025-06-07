import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Musica:
    def __init__(self, titulo, nroFaixa, artista, album):
        self.titulo = titulo
        self.nroFaixa = nroFaixa
        self.artista = artista
        self.album = album
    
    def getTitulo(self):
        return self.titulo
    
    def getNroFaixa(self):
        return self.nroFaixa
    
    def getArtista(self):
        return self.artista
    
    def getAlbum(self):
        return self.album
    
class LimiteInsereMusica(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("250x125")
        self.title("Inserir Musica")
        self.controle = controle

        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)
        self.frame3 = tk.Frame(self)
        self.frame4 = tk.Frame(self)
        self.frame5 = tk.Frame(self)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        self.labelInsereTitulo = tk.Label(self.frame1, text = "Título da Música: ")
        self.labelInsereTitulo.pack(side = "left")
        self.entraTitulo = tk.Entry(self.frame1, width = 20)
        self.entraTitulo.pack(side = "left")

        self.labelInsereFaixa = tk.Label(self.frame2, text = "Faixa da Música: ")
        self.labelInsereFaixa.pack(side = "left")
        self.entraFaixa = tk.Entry(self.frame2, width = 20)
        self.entraFaixa.pack(side = "left")

        self.labelInsereArtista = tk.Label(self.frame3, text = "Artista da Música: ")
        self.labelInsereArtista.pack(side = "left")
        self.entraArtista = tk.Entry(self.frame3, width = 20)
        self.entraArtista.pack(side = "left")

        self.labelInsereAlbum = tk.Label(self.frame4, text = "Album da Música: ")
        self.labelInsereAlbum.pack(side = "left")
        self.entraAlbum = tk.Entry(self.frame4, width = 20)
        self.entraAlbum.pack(side = "left")

        self.botaoCadastrar = tk.Button(self.frame5, text = "Cadastrar")
        self.botaoCadastrar.pack(side = "left")
        self.botaoCadastrar.bind("<Button>", controle.cadastrarMusicaHandler)

        self.botaoConcluido = tk.Button(self.frame5, text = "Sair")
        self.botaoConcluido.pack(side = "left")
        self.botaoConcluido.bind("<Button>", controle.concluidoInsereHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaMusica(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("250x50")
        self.title("Consultar Música")
        self.controle = controle

        self.frameMusica = tk.Frame(self)
        self.frame5 = tk.Frame(self)
        self.frameMusica.pack()
        self.frame5.pack()

        self.labelTitulo = tk.Label(self.frameMusica, text = "Título da Música: ")
        self.entraTitulo = tk.Entry(self.frameMusica, width = 20)
        self.labelTitulo.pack(side = "left")
        self.entraTitulo.pack(side = "left")

        self.botaoConsultar = tk.Button(self.frame5, text = "Consultar")
        self.botaoConsultar.pack()
        self.botaoConsultar.bind("<Button>", controle.consultarMusicaHandler)

class LimiteMostraMusica:
    def __init__(self, mensagem, tipo):
        if tipo:
            messagebox.showinfo("Música encontrada", mensagem)
        else:
            messagebox.showinfo("Aviso", mensagem)

class ControleMusica:
    def __init__(self, controlePrincipal):
        if not os.path.isfile("musica.pickle"):
            self.listaMusicas = []
        else:
            with open("musica.pickle", "rb") as f:
                self.listaMusicas = pickle.load(f)
        
        self.controlePrincipal = controlePrincipal
        self.controleArtista = controlePrincipal.controleArtista

        
    def getMusicas(self):
        return self.listaMusicas

    def cadastraMusica(self):
        self.LimiteCadastraMusica = LimiteInsereMusica(self)
    
    def consultaMusica(self):
        self.LimiteBuscaMusica = LimiteConsultaMusica(self)

    def cadastrarMusicaHandler(self, event):
        titulo = self.LimiteCadastraMusica.entraTitulo.get()
        faixa = self.LimiteCadastraMusica.entraFaixa.get()
        nomeArtista = self.LimiteCadastraMusica.entraArtista.get()
        nomeAlbum = self.LimiteCadastraMusica.entraAlbum.get()
        
        tipoArt = False
        artista = 1
        album = 1
        for art in self.controleArtista.getArtistas():
            if nomeArtista == art.getNome():
                artista = art
                tipoArt = True
        
        if not tipoArt:
            self.LimiteCadastraMusica.mostraJanela("Aviso", "Artista não encontrado")
            return
        
        tipoAlb = False
        for alb in artista.getAlbuns():
            if nomeAlbum == alb.getTitulo():
                album = alb
                tipoAlb = True
        
        if not tipoAlb:
            self.LimiteCadastraMusica.mostraJanela("Aviso", "Álbum não encontrado")
            return
        
        musica = Musica(titulo, faixa, artista, album)
        self.listaMusicas.append(musica)
        artista.addMusica(musica)
        album.addMusica(musica)
        self.LimiteCadastraMusica.mostraJanela("Sucesso", "Música cadastrada com sucesso")
        self.limpaTituloInsere(event)
        self.limpaFaixaInsere(event)
       
    def consultarMusicaHandler(self, event):
        musica = self.LimiteBuscaMusica.entraTitulo.get()
        mensagem = ""
        tipo = False

        for musc in self.getMusicas():
            if musica == musc.getTitulo():
                tipo = True
                mensagem += "Música: " + musc.getTitulo() + "\n"
                mensagem += "Faixa: " + musc.getNroFaixa() + "\n"
                mensagem += "Artista: " + musc.getArtista().getNome() + "\n"
                mensagem += "Álbum: " + musc.getAlbum().getTitulo()
                LimiteMostraMusica(mensagem, True)
                self.limpaTituloConsulta(event)
                return
        LimiteMostraMusica("Musica não encontrada", tipo)
        self.limpaTituloConsulta(event)
    
    def limpaTituloInsere(self, event):
        self.LimiteCadastraMusica.entraTitulo.delete(0, len(self.LimiteCadastraMusica.entraTitulo.get()))

    def limpaFaixaInsere(self, event):
        self.LimiteCadastraMusica.entraFaixa.delete(0, len(self.LimiteCadastraMusica.entraFaixa.get()))
    
    def limpaTituloConsulta(self, event):
        self.LimiteBuscaMusica.entraTitulo.delete(0, len(self.LimiteBuscaMusica.entraTitulo.get()))

    def salvaMusica(self):
        if len(self.listaMusicas) != 0:
            with open("musica.pickle", "wb") as f:
                pickle.dump(self.listaMusicas, f)
    
    def concluidoInsereHandler(self, event):
        self.LimiteCadastraMusica.destroy()
    
    def concluidoConsultaHandler(self, event):
        self.LimiteBuscaMusica.destroy()

        

        


        



            

            

        
        
