from abc import ABC, abstractmethod

from arma import Arma


class Personagem(ABC):
    def __init__(self, arma: Arma):
        self._arma = arma

    def usar_arma(self):
        self._arma.usar_arma()

    @property
    def comportamento_arma(self):
        return self._arma
    
    @comportamento_arma.setter
    def comportamento_arma(self, nova_arma: Arma):
        self._arma = nova_arma

    @abstractmethod
    def lutar(self):
        ...