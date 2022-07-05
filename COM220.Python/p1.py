#Nome: Lucas Batista Pereira
#Matricula: 2020007290
#COM 220
#P1

from datetime import date

class Conta():
    def __init__(self, nroConta, nome, limite, senha):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__limite = limite
        self.__senha = senha
        self.__transacoes = []
        self.__saldoReal = 0

    def getNroConta(self):
        return self.__nroConta
    
    def getNome(self):
        return self.__nome

    def getLimite(self):
        return self.__limite

    def getSenha(self):
        return self.__senha

    def getTransacoes(self):
        return self.__transacoes

    def getSaldoReal(self):
        return self.__saldoReal

    def adicionaDeposito(self, valor, data, nomeDepositante):
        self.__transacoes.append(Deposito(valor, data, nomeDepositante))        #Registra a operação
        self.__saldoReal += valor

    def creditoTransf(self, valor, data, senha, tipoTransf):
        self.__transacoes.append(Tranferencia(valor, data, senha, tipoTransf))  #Registra a operação
        self.__saldoReal += valor

    def adicionaSaque(self, valor, data, senha):
        if senha == self.getSenha():                                            #Checa senha
            if (self.calculaSaldo() - valor) > (- 1 * self.getLimite()):        #checa se é possivel realizar a operação
                self.__transacoes.append(Saque(valor, data, senha))             #Registra a operação
                self.__saldoReal -= valor                                       #faz a subtração do saldo real
                print("Saque de {} realizado!".format(valor))   
                return True
            else: return False
        else: return False

    def adicionaTransf(self, valor, data, senha, contaFavorecido):
        if senha == self.getSenha():
            if (self.calculaSaldo() - valor) > (- 1 * self.getLimite()):        #checa se é possivel realizar a operação
                self.__transacoes.append(Tranferencia(valor, data, senha, "D")) #Registra a operação
                self.__saldoReal -= valor                                       #Acrescenta ao saldo real
                contaFavorecido.creditoTransf(valor, data, senha, "C")          #Realiza a tranferencia para o favorecido
                print("Trasferencia de {} para {} realizado com sucesso!".format(valor, contaFavorecido.getNome()))
                return True
            else: return False
        else: return False
        
    def calculaSaldo(self):
        return self.__saldoReal + self.__limite 

    def mostraHistorico(self):                                                  #Função para mostrar Historico
        i = 0
        print("------------------------------------")
        print("\nHistorico de {}:".format(self.getNome()))
        for transacao in self.getTransacoes():
            i += 1
            print("\nOperacao: {}".format(i))
            transacao.mostraHistorico()

class Transacao():
    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data

    def getValor(self):
        return self.__valor

    def getData(self):
        return self.__data

class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self.__senha = senha
    
    def getSenha(self):
        return self.__senha

    def mostraHistorico(self):
        print("Valor do saque: {}".format(super().getValor()))
        print("Data do saque: {}".format(super().getData()))
        print("Senha do saque: {}\n".format(self.getSenha()))

class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self.__nomeDepositante = nomeDepositante

    def getNomeDepositante(self):
        return self.__nomeDepositante

    def mostraHistorico(self):
        print("Valor do deposito: {}".format(super().getValor()))
        print("Data do deposito: {}".format(super().getData()))
        print("Nome do depositante: {}\n".format(self.getNomeDepositante()))

class Tranferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self.__senha = senha
        self.__tipoTransf = tipoTransf

    def getSenha(self):
        return self.__senha
    
    def getTipoTransf(self):
        return self.__tipoTransf

    def mostraHistorico(self):
        print("Valor da tranferencia: {}".format(super().getValor()))
        print("Data da tranferencia: {}".format(super().getData()))
        print("Senha da tranferencia: {}".format(self.getSenha()))
        print("Tipo da tranferencia: {}\n".format(self.getTipoTransf()))


if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')
    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False: # deve falhar
        print('Não foi possível realizar o saque no valor de 1000')

    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False: # deve falhar
        print('Não foi possível realizar a transf no valor de 5000')
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor de 800')
    
    print('\n------------------------------------')
    print('Saldo de c1: {}'.format(c1.calculaSaldo())) # deve imprimir 4800
    print('Saldo de c2: {}'.format(c2.calculaSaldo())) # deve imprimir 1700

    c1.mostraHistorico()
    c2.mostraHistorico()