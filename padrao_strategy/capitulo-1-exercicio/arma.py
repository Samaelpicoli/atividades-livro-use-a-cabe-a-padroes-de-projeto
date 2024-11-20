from abc import ABC, abstractmethod

class Arma(ABC):
    @abstractmethod
    def usar_arma(self):
        ...

class Machado(Arma):
    def usar_arma(self):
        print('Usar machado')
    
class Espada(Arma):
    def usar_arma(self):
        print('Usar espada')

class ArcoEFlecha(Arma):
    def usar_arma(self):
        print('Usar arco e flecha')

class Faca(Arma):
    def usar_arma(self):
        print('Usar faca')