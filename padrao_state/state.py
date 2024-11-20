from abc import ABC, abstractmethod


class State(ABC):
    """Interface que representa os estados da máquina de gumballs.

    O padrão State permite que um objeto altere seu comportamento
    quando seu estado interno muda. Neste caso, a máquina de gumballs muda
    seu comportamento com base em seu estado atual (vazia, com moeda, etc.),
    encapsulando a lógica específica de cada estado em suas respectivas classes.
    """

    @abstractmethod
    def insert_quarter(self):
        """Insere uma moeda na máquina."""
        pass


    @abstractmethod
    def eject_quarter(self):
        """Ejeta a moeda da máquina."""
        pass


    @abstractmethod
    def turn_crank(self):
        """Gira a manivela da máquina."""
        pass


    @abstractmethod
    def dispense(self):
        """Dispensa uma gumball da máquina."""
        pass