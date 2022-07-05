#Nome: Lucas Batista Pereira
#Matricula: 2020007290
#COM 220
#TRAB 7

from abc import ABC, abstractmethod
from datetime import date

class Venda(ABC):
    def __init__(self, nroNF, dtEmissao):
        self.__nroNF = nroNF
        self.__dtEmissao = dtEmissao
        self.__itens = []

    def getNroNF(self):
        return self.__nroNF

    def getDtEmissao(self):
        return self.__dtEmissao

    def getItens(self):
        return self.__itens

    def mostrarItens(self):
        for venda in self.__itens:
            print("-> Codigo do produto: {}".format(venda.getCodProd()))
            print("-> Quantidade: {}".format(venda.getQuant()))
            print("-> Preco: {}\n".format(venda.getPrecoUnit()))

    def adicionaItem(self, pCodProd, pQuant, pPrecoUnit):
        self.__itens.append(item_Venda(pCodProd, pQuant, pPrecoUnit))

    def calculaTotalVendido(self):
        soma = 0
        for venda in self.getItens():
            soma += venda.getPrecoUnit() * venda.getQuant()
        return soma
            
    @abstractmethod
    def geraNF(self):
        pass
    
    @abstractmethod
    def calculaImposto(self):
        pass

class VendaPF(Venda):
    def __init__(self, nroNF, dtEmissao, cpf, nome):
        super().__init__(nroNF, dtEmissao)
        self.__cpf = cpf
        self.__nome = nome
        self.impostoPF = 0.09
    
    def getCpf(self):
        return self.__cpf

    def getNome(self):
        return self.__nome

#abstracts
    def geraNF(self):
        print("\nNota fiscal: {}".format(super().getNroNF()))
        print("Data de emissão: {}".format(super().getDtEmissao()))
        print("Itens adquiridos:")
        super().mostrarItens()
        print("CPF do comprador: {}".format(self.getCpf()))
        print("Nome do comprador: {}".format(self.getNome()))

    def calculaImposto(self):
        return super().calculaTotalVendido() * self.impostoPF

class VendaPJ(Venda):
    def __init__(self, nroNF, dtEmissao, cpf, nome):
        super().__init__(nroNF, dtEmissao)
        self.__cpf = cpf
        self.__nome = nome
        self.impostoPJ = 0.06

    def getCpf(self):
        return self.__cpf

    def getNome(self):
        return self.__nome

#abstracts
    def geraNF(self):
        print("\nNota fiscal: {}".format(super().getNroNF()))
        print("Data de emissão: {}".format(super().getDtEmissao()))
        print("Itens adquiridos:")
        super().mostrarItens()
        print("CPF do comprador: {}".format(self.getCpf()))
        print("Nome do comprador: {}".format(self.getNome()))

    def calculaImposto(self):
        return super().calculaTotalVendido() * self.impostoPJ

class item_Venda():
    def __init__(self, codProd, quant, precoUnit):
        self.__codProd = codProd
        self.__quant = quant
        self.__precoUnit = precoUnit
    
    def getCodProd(self):
        return self.__codProd

    def getQuant(self):
        return self.__quant

    def getPrecoUnit(self):
        return self.__precoUnit

if __name__ == "__main__":
    totalFaturado = 0
    totalImposto = 0
    vendas = []
    vendapf = VendaPF(1000, date.today(), '123456789', 'Joao')
    vendapf.adicionaItem(100, 10, 10)
    vendapf.adicionaItem(100, 10, 20)
    vendapf.adicionaItem(100, 10, 30)
    vendas.append(vendapf)
    vendapj = VendaPJ(1001, date.today(), '987654321', 'Silva Ltda')
    vendapj.adicionaItem(200, 100, 10)
    vendapj.adicionaItem(201, 100, 20)
    vendas.append(vendapj)
    for venda in vendas:
        totalFaturado += venda.calculaTotalVendido()
        totalImposto += venda.calculaImposto()
    print('Total faturado: {}'.format(totalFaturado))
    print('Total pago em impostos: {}'.format(totalImposto))

    vendapf.geraNF()
    vendapj.geraNF()