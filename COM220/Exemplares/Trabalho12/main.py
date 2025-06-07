import tkinter as tk
import artista 
import album 
import musica
import playlist

class MenuPrincipal:
	def __init__(self, root, controle):
		
		self.root = root
		self.controle = controle
		self.root.geometry("450x250")
		self.root.title("Trab13")

		self.menu = tk.Menu(self.root)
		self.menuArtista = tk.Menu(self.menu)
		self.menuMusica = tk.Menu(self.menu)
		self.menuAlbum = tk.Menu(self.menu)
		self.menuPlaylist = tk.Menu(self.menu)
		self.menuSair = tk.Menu(self.menu)

		self.menu.add_cascade(label = "Artista", menu = self.menuArtista) 
		self.menuArtista.add_command(label = "Cadastrar", command = self.controle.insereArtista)
		self.menuArtista.add_command(label = "Consultar", command = self.controle.consultaArtista)
		
		self.menu.add_cascade(label = "Música", menu = self.menuMusica) 
		self.menuMusica.add_command(label = 'Cadastrar', command = self.controle.insereMusica)
		self.menuMusica.add_command(label = 'Consultar', command = self.controle.consultaMusica)
		
		self.menu.add_cascade(label = "Álbum", menu = self.menuAlbum)
		self.menuAlbum.add_command(label = "Cadastrar", command = self.controle.insereAlbum)
		self.menuAlbum.add_command(label = "Consultar", command = self.controle.consultaAlbum)

		self.menu.add_cascade(label = "Playlist", menu = self.menuPlaylist)
		self.menuPlaylist.add_command(label = "Cadastrar", command = self.controle.inserePlaylist)
		self.menuPlaylist.add_command(label = "Consultar", command = self.controle.consultaPlaylist)

		self.menu.add_cascade(label = "Sair", menu = self.menuSair)
		self.menuSair.add_command(label = "Salvar", command = self.controle.salvaDados)
		self.menuSair.add_command(label = "Não Salvar", command = lambda: self.root.destroy())

		self.root.config(menu=self.menu)

class ControlePrincipal:
	def __init__(self):
		self.root = tk.Tk()
		self.limite = MenuPrincipal(self.root, self)
		self.controleArtista = artista.ControleArtista()
		self.controleMusica = musica.ControleMusica(self)
		self.controleAlbum = album.ControleAlbum(self)
		self.controlePlaylist = playlist.ControlePlaylist(self)
		
		self.root.mainloop()

	def insereArtista(self):
		self.controleArtista.cadastraArtista()
	
	def consultaArtista(self):
		self.controleArtista.consultaArtista()
	
	def insereMusica(self):
		self.controleMusica.cadastraMusica()
	
	def consultaMusica(self):
		self.controleMusica.consultaMusica()

	def insereAlbum(self):
		self.controleAlbum.cadastraAlbum()

	def consultaAlbum(self):
		self.controleAlbum.consultaAlbum()
	
	def inserePlaylist(self):
		self.controlePlaylist.cadastraPlaylist()
		self.controlePlaylist.atualizaListBox()

	def consultaPlaylist(self):
		self.controlePlaylist.ConsultaPlaylist()

	def salvaDados(self):
		self.controleArtista.salvaArtista()
		self.controleAlbum.salvaAlbum()
		self.controleMusica.salvaMusica()
		self.controlePlaylist.salvaPlaylist()
		self.root.destroy()
	

if __name__ == '__main__':
	App = ControlePrincipal()