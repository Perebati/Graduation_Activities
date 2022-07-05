#Nome: Lucas Batista Pereira
#matricula: 2020007290
#COM220
#Trab5

from abc import ABC, abstractmethod

class FormaGeo(ABC):
    def __init__(self, id):
        self.__id = id
    
    def getId(self):
        return self.__id

    def Area(self):
        return 0

    def Volume(self):
        return 0

    @abstractmethod
    def getDescricao(self):
        pass

class Ponto(FormaGeo):
    def __init__(self, id, x, y):
        super().__init__(id)
        self.__x = x
        self.__y = y
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getDescricao(self):
        print("Identificador: {}".format(self.getId()))
        print("Ponto: [{}, {}]".format(self.__x, self.__y))
        print("Area: {} ".format(super().Area()))
        print("Volume: {} ".format(super().Volume()))

class Circulo(Ponto):
    def __init__(self, id, x, y, raio):
        super().__init__(id, x, y)
        self.__raio = raio

    def getRaio(self):
        return self.__raio
    
    def getArea(self):
        area = 3.141592653589931 * (self.__raio**2)
        return area

    def getDescricao(self):
    
        print('Identificador: {}'.format(self.getId()))
        print("Circulo: Centro: [{}, {}] Raio: {}".format(self.getX(), self.getY(), self.getRaio()))
        print("Area: {}".format(self.getArea()))
        print('Volume: {}'.format(super().Volume()))

class Cilindro(Circulo):
    def __init__(self, id, x, y, raio, altura):
        super().__init__(id, x, y, raio)
        self.__altura = altura

    def getAltura(self):
        return self.__altura

    def getVolume(self):
        return super().getArea() * self.__altura

    def getArea(self):
        AreaBase = 2*super().getArea()
        AreaLateral = (2 * 3.141592653589931 * self.getRaio()) * self.getAltura()
        return (AreaBase + AreaLateral)

    def getDescricao(self):
        print('Identificador: {}'.format(self.getId()))
        print("Circulo: Centro: [{}, {}] Raio: {} Altura: {}".format(self.getX(), self.getY(), self.getRaio(), self.getAltura()))
        print("Area: {}".format(self.getArea()))
        print('Volume: {}'.format(self.getVolume()))

if __name__ == "__main__":
    ponto1 = Ponto(1, 2, 3)
    ponto1.getDescricao()
    print()
    circulo1 = Circulo(2, 22, 8, 3.5)
    circulo1.getDescricao()
    print()
    cilindro1 = Cilindro(3, 10, 10, 3.3, 10)
    cilindro1.getDescricao()
   