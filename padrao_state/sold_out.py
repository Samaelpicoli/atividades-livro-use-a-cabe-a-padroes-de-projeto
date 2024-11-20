from state import State


class SoldOutState(State):
    """
    Classe que representa o estado 'esgotado' da máquina de gumballs.

    Neste estado, a máquina não tem gumballs para dispensar, 
    e os métodos refletem essa condição.
    """

    def __init__(self, gumball_machine):
        """
        Inicializa o estado esgotado com uma referência à máquina de gumballs.

        Args:
            gumball_machine (GumballMachine): A referência à máquina de
            gumballs.
        """
        self.gumball_machine = gumball_machine


    def insert_quarter(self):
        """
        Método chamado ao tentar inserir uma moeda
        enquanto a máquina está esgotada.
        """
        print('You can"t insert a quarter, the machine is sold out.')


    def eject_quarter(self):
        """
        Método chamado ao tentar ejetar a moeda enquanto
        a máquina está esgotada.
        """
        print('You can"t eject, you haven"t inserted a quarter yet.')


    def turn_crank(self):
        """
        Método chamado ao girar a manivela enquanto a máquina está esgotada.
        """
        print('You turned, but there are no gumballs.')


    def dispense(self):
        """
        Método chamado para dispensar uma gumball,
        mas não há gumballs disponíveis.
        """
        print('No gumball dispensed.')


    def __str__(self):
        """Retorna uma representação em string do estado esgotado."""
        return 'sold out'