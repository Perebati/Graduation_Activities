#Nome: Lucas Batista Pereira
#Matricula: 2020007290
#COM 220
#TRAB 8

def mdc(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def mesmaFracao(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())    


class Fracao:
    def __init__(self, num, den):
        self.__num = num        
        self.__den = den     

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

    def getNum(self):
        return self.__num

    def getDen(self):
        return self.__den       

    def simplifica(self):
        divComum = mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum   

    def __add__(self,outraFrac):
        novoNum = self.__num * outraFrac.getDen() + self.__den * outraFrac.getNum()
        novoDen = self.__den * outraFrac.getDen()
        divComum = mdc(novoNum, novoDen)
        pInt = novoNum//novoDen
        if(pInt >= 1):
            return FracaoMista(pInt, (novoNum - (pInt * novoDen)), novoDen)
        else: return Fracao(novoNum//divComum, novoDen//divComum)     

class FracaoMista:
    def __init__(self, pInt, num, den):
        self.__pInt = pInt
        self.__num = num
        self.__den = den

    def __str__(self):
        if self.__num == 0:
            return str(self.__pInt)
        else:
            return str(self.__pInt) + " " + str(self.__num) + "/" + str(self.__den)
    
    def getPInt(self):
        return self.__pInt

    def getNum(self):
        return (self.__den * self.__pInt) + self.__num

    def getDen(self):
        return self.__den

    def __add__(self, outraFrac):
        novoNum = self.getNum() * outraFrac.getDen() + self.__den * outraFrac.getNum()
        novoDen = self.__den * outraFrac.getDen()
        divComum = mdc(novoNum, novoDen)
        pInt2 = novoNum//novoDen
        if(pInt2 >= 1):
            return FracaoMista(pInt2, (novoNum - (pInt2 * novoDen)), novoDen)
        else: return Fracao(novoNum//divComum, novoDen//divComum)     

if __name__ == "__main__":
    frac1 = Fracao(7, 6) 
    frac2 = Fracao(13, 7)
    frac3 = frac1 + frac2
    print(frac3)
    print()
    frac1 = Fracao (1, 3)
    frac2 = Fracao(2, 3)
    frac3 = frac1 + frac2
    print(frac3)
    print()
    frac1 = FracaoMista(3, 1, 2)
    frac2 = FracaoMista(4, 2, 3)
    frac3 = frac1 + frac2
    print(frac3)
    print()
    frac1 = FracaoMista(0, 1, 4)
    frac2 = FracaoMista(0, 2, 3)
    frac3 = frac1 + frac2 #Caso a soma das funções mistas for menor que 1, o programa imprime uma fração comum
    print(frac3)

