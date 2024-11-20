from state import State

class WinnerState(State):
    """Classe que representa o estado 'vencedor' da máquina de gumballs.

    Neste estado, o usuário recebe duas gumballs ao girar a manivela. 
    O estado é ativado em situações especiais, como um prêmio.
    """

    def __init__(self, gumball_machine):
        """I
        nicializa o estado vencedor com uma referência à máquina de gumballs.

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
        print('Please wait, were already giving you a gumball.')


    def eject_quarter(self):
        """
        Método chamado ao tentar ejetar a moeda após girar a manivela.
        """
        print('Sorry, you have already turned the crank.')


    def turn_crank(self):
        """
        Método chamado ao girar a manivela novamente enquanto
        uma gumball está sendo dispensada."""
        print('Turning twice doesn"t get you another gumball.')


    def dispense(self):
        """
        Dispensa duas gumballs para o usuário, refletindo o
        estado de 'vencedor'.
        """
        print('You are a Winner! You get two gumballs for your quarter.')
        if self.gumball_machine.get_count() == 0:
            self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())
        else:
            # Dispensa a primeira gumball
            self.gumball_machine.release_ball()
            if self.gumball_machine.get_count() > 0:
                # Dispensa a segunda gumball
                self.gumball_machine.release_ball()
                if self.gumball_machine.get_count() == 0:
                    self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())
                else:
                    self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
            else:
                print('Oops, out of gumballs.')
                self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())