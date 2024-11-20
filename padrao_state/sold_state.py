from state import State


class SoldState(State):
    """
    Classe que representa o estado de 'vendendo' da máquina de gumballs.

    Neste estado, a máquina já está processando a venda de uma gumball. 
    O comportamento dos métodos é adaptado para refletir esta condição.
    """

    def __init__(self, gumball_machine):
        """
        Inicializa o estado de venda com uma referência à máquina de gumballs.

        Args:
            gumball_machine (GumballMachine): A referência à máquina
            de gumballs.
        """
        self.gumball_machine = gumball_machine


    def insert_quarter(self):
        """
        Método chamado ao tentar inserir uma moeda enquanto
        uma gumball está sendo dispensada.
        """
        print("Please wait, we're already giving you a gumball.")


    def eject_quarter(self):
        """
        Método chamado ao tentar ejetar a moeda enquanto uma
        gumball está sendo dispensada.
        """
        print("Sorry, you have already turned the crank.")


    def turn_crank(self):
        """
        Método chamado ao girar a manivela novamente enquanto
        uma gumball está sendo dispensada.
        """
        print("Turning twice doesn't get you another gumball.")


    def dispense(self):
        """
        Dispensa a gumball e atualiza o estado da máquina, se necessário.
        """
        self.gumball_machine.release_ball() 
        if self.gumball_machine.get_count() > 0:
            self.gumball_machine.set_state(
                self.gumball_machine.get_no_quarter_state()
            )
        else:
            print("Oops, out of gumballs!")
            self.gumball_machine.set_state(
                self.gumball_machine.get_sold_out_state()
            )


    def __str__(self):
        """Retorna uma representação em string do estado de venda."""
        return "dispensing a gumball"