from arma import ArcoEFlecha, Espada, Faca, Machado
from personagem import Personagem

class Rainha(Personagem):
    def __init__(self):
        super().__init__(ArcoEFlecha())

    def lutar(self):
        print('Rainha vai lutar...')
        self.usar_arma()


class Rei(Personagem):
    def __init__(self):
        super().__init__(Machado())

    def lutar(self):
        print('Rei vai lutar...')
        self.usar_arma()


class Troll(Personagem):
    def __init__(self):
        super().__init__(Espada())

    def lutar(self):
        print('Troll vai lutar...')
        self.usar_arma()


class Cavaleiro(Personagem):
    def __init__(self):
        super().__init__(Faca())

    def lutar(self):
        print('Cavaleiro vai lutar...')
        self.usar_arma()



if __name__ == '__main__':

    rainha = Rainha()
    rainha.lutar()

    rei = Rei()
    rei.lutar()

    troll = Troll()
    troll.lutar()

    cavaleiro = Cavaleiro()
    cavaleiro.lutar()
