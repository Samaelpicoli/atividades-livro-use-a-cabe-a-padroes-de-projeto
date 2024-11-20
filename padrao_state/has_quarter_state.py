from random import randint
from state import State


class HasQuarterState(State):
    """
    Classe que representa o estado 'com moeda' da máquina de gumballs.

    Neste estado, a máquina recebeu uma moeda e está esperando que
    o usuário gire a manivela.
    """

    def __init__(self, gumball_machine):
        """
        Inicializa o estado com moeda com uma referência à máquina de
        gumballs.

        Args:
            gumball_machine (GumballMachine): A referência à máquina
            de gumballs.
        """
        self.random_winner = randint(1, 10)
        self.gumball_machine = gumball_machine


    def insert_quarter(self):
        """
        Método chamado ao tentar inserir outra moeda
        enquanto já existe uma moeda inserida.
        """
        print('You can\'t insert another quarter.')


    def eject_quarter(self):
        """Método chamado ao ejetar a moeda que foi inserida."""
        print('Quarter returned')
        self.gumball_machine.set_state(
            self.gumball_machine.get_no_quarter_state()
        )


    def turn_crank(self):
        """Método chamado ao girar a manivela após inserir uma moeda."""
        print('You turned...')
        if self.random_winner == 10 and self.gumball_machine.get_count() > 2:
            self.gumball_machine.set_state(
                self.gumball_machine.get_winner_state()
            )
        else:
            self.gumball_machine.set_state(
                self.gumball_machine.get_sold_state()
            )


    def dispense(self):
        """
        Método chamado para dispensar uma gumball, mas não
        dispensa nada até que a manivela seja girada.
        """
        print('No gumball dispensed.')


    def __str__(self):
        """Retorna uma representação em string do estado com moeda."""
        return 'waiting for turn of crank'