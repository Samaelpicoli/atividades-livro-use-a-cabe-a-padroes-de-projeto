from state import State


class NoQuarterState(State):
    """
    Classe que representa o estado 'sem moeda' da máquina de gumballs.

    Neste estado, a máquina está aguardando a inserção de uma moeda
    antes de permitir outras ações.
    """

    def __init__(self, gumball_machine):
        """
        Inicializa o estado sem moeda com uma referência à máquina de
        gumballs.

        Args:
            gumball_machine (GumballMachine): A referência à máquina
            de gumballs.
        """
        self.gumball_machine = gumball_machine


    def insert_quarter(self):
        """Método chamado ao inserir uma moeda."""
        print('You inserted a quarter')
        self.gumball_machine.set_state(
            self.gumball_machine.get_has_quarter_state()
        )


    def eject_quarter(self):
        """
        Método chamado ao tentar ejetar a moeda, mas nenhuma foi inserida.
        """
        print('You haven"t inserted a quarter.')


    def turn_crank(self):
        """Método chamado ao girar a manivela sem ter inserido uma moeda."""
        print('You turned, but there"s no quarter.')


    def dispense(self):
        """
        Método chamado para dispensar uma gumball, mas o pagamento
        não foi feito.
        """
        print('You need to pay first.')


    def __str__(self):
        """Retorna uma representação em string do estado sem moeda."""
        return 'waiting for quarter'
    
