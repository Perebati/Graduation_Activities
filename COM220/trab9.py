#Nome: Lucas Batista Pereira
#Matricula: 2020007290
#COM 220
#TRAB 9

from abc import ABC, abstractmethod

#Execeptions
class DuplicadoCPF(Exception):
    pass

class IdadeMenorQuePermitida(Exception):
     pass

class CursoErrado(Exception):
    pass

class TitulacaoErrada(Exception):
    pass

#Classes
class Pessoa(ABC):
    def __init__(self, nome, endereco, idade , cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf
    
    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco
    
    def getIdade(self):
        return self.__idade

    def getCpf(self):
        return self.__cpf
    
    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao
    
    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print("\nNome do professor: {}".format(self.getNome()))
        print("Endereco do professor: {}".format(self.getEndereco()))
        print("Idade do professor: {}".format(self.getIdade()))
        print("CPF do professor: {}".format(self.getCpf()))
        print("Titulação do professor: {}".format(self.getTitulacao()))


class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso

    def getCurso(self):
        return self.__curso
    
    def printDescricao(self):
        print("\nNome do aluno: {}".format(self.getNome()))
        print("Endereco do aluno: {}".format(self.getEndereco()))
        print("Idade do aluno: {}".format(self.getIdade()))
        print("CPF do aluno: {}".format(self.getCpf()))
        print("Curso do aluno: {}".format(self.getCurso()))

#main
if __name__ == "__main__":
    
    #Professores
    Adalberto = Professor("Adalberto", "Itajuba", 45, 100,"doutor")     #Deve dar certo
    Beatriz = Professor("Beatriz", "Piranguinho", 21, 101, "doutor")    #Deve dar errado (Idade)
    Carlos = Professor("Carlos", "Delfim", 41, 102, "nao doutor")       #Deve dar errado (Titulação)
    Diego = Professor("Diego", "Ribeirão", 45, 103, "doutor")           #Deve dar certo 
    Eledir = Professor("Eledir", "Uberaba", 60, 103, "doutor")          #Deve dar errado (Mesmo CPF)

    #Alunos
    Alex = Aluno("Alex", "Jundiai", 21, 200, "CCO")                     #Deve dar certo
    Bruna = Aluno("Bruna", "Itauna", 17, 201, "CCO")                    #Deve dar errado (Idade menor)
    Cris = Aluno("Cris", "Campinas", 20, 202, "ECO")                    #Deve dar errado (Curso)
    Dino = Aluno("Dino", "Niteroi", 21, 203, "SIN")                     #Deve dar certo
    Eduardo = Aluno("Eduardo", "Cabo frio", 21, 203, "CCO")             #Deve dar errado (Mesmo CPF)

    #Lista de todas as pessoas
    listaPessoas = [
        Adalberto, Beatriz, Carlos, Diego, Eledir,
        Alex, Bruna, Cris, Dino, Eduardo
    ]

    #Lista das pessoas que se encaixam no cadastro
    cadastro = []
    
    for pessoa in listaPessoas:
        try:
            #Verificação dos exceptions do aluno
            if type(pessoa) == Aluno:
                if pessoa.getIdade() < 18:
                    raise IdadeMenorQuePermitida()
                elif pessoa.getCurso() != "CCO" and pessoa.getCurso() != "SIN":
                    raise CursoErrado()
               
            #Verificação dos exceptions do professor
            elif type(pessoa) == Professor:
                if pessoa.getIdade() < 30:
                    raise IdadeMenorQuePermitida()
                elif pessoa.getTitulacao() != "doutor":
                    raise TitulacaoErrada()

            #Verifica o CPF do cadastro com a da lista
            for check in cadastro:
                if check.getCpf() == pessoa.getCpf():
                    raise DuplicadoCPF()

        #Execução dos exeptions, caso haja
        except DuplicadoCPF:
            print("O CPF '%i' já está cadastrado!" \
                %  pessoa.getCpf())
        except IdadeMenorQuePermitida:
            print("A idade de '%s' é menor do que a permitida!" \
                % pessoa.getNome())
        except CursoErrado:
            print("O curso de '%s' não é permitido no cadastro de alunos!"\
                % pessoa.getNome())
        except TitulacaoErrada:
            print("A titulação de '%s' não é permitida para o cadastro de professores!" \
                % pessoa.getNome())
        
        #Caso não haja execptions
        else: 
            cadastro.append(pessoa)

    #Printa apenas os cadastrados
    for pessoa in cadastro:
        pessoa.printDescricao()