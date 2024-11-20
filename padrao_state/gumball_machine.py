from has_quarter_state import HasQuarterState
from no_quarter_state import NoQuarterState
from sold_out import SoldOutState
from sold_state import SoldState
from state import State
from winner_state import WinnerState


class GumballMachine:
    """
    Classe que representa uma máquina de gumballs.

    A máquina pode estar em diferentes estados
    (esgotada, sem moeda, com moeda, vendendo)
    e muda seu comportamento com base no estado atual.
    """

    def __init__(self, number_gumballs: int):
        """
        Inicializa a máquina de gumballs com um número
        especificado de gumballs.

        Args:
            number_gumballs (int): O número inicial de gumballs na máquina.
        """
        self.sold_out_state = SoldOutState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.winner_state = WinnerState(self)
        self.count = number_gumballs
        if number_gumballs > 0:
            self.state = self.no_quarter_state
        else:
            self.state = self.sold_out_state


    def insert_quarter(self):
        """Método chamado ao inserir uma moeda na máquina."""
        self.state.insert_quarter()


    def eject_quarter(self):
        """Método chamado ao ejetar a moeda da máquina."""
        self.state.eject_quarter()


    def turn_crank(self):
        """Método chamado ao girar a manivela da máquina."""
        self.state.turn_crank()
        self.state.dispense()


    def set_state(self, state: State):
        """
        Altera o estado atual da máquina.

        Args:
            state (State): O novo estado a ser definido.
        """
        self.state = state


    def release_ball(self):
        """Dispensa uma gumball da máquina, se disponível."""
        print("A gumball comes rolling out the slot...")
        if self.count > 0:
            self.count -= 1


    def get_count(self) -> int:
        """Retorna o número atual de gumballs na máquina."""
        return self.count


    def refill(self, count: int):
        """
        Reabastece a máquina com um número especificado de gumballs.

        Args:
            count (int): O número de gumballs a serem adicionados.
        """
        self.count = count
        self.state = self.no_quarter_state


    def get_state(self) -> State:
        """Retorna o estado atual da máquina."""
        return self.state


    def get_sold_out_state(self) -> SoldOutState:
        """Retorna o estado de esgotado da máquina."""
        return self.sold_out_state


    def get_no_quarter_state(self) -> NoQuarterState:
        """Retorna o estado sem moeda da máquina."""
        return self.no_quarter_state


    def get_has_quarter_state(self) -> HasQuarterState:
        """Retorna o estado com moeda da máquina."""
        return self.has_quarter_state


    def get_sold_state(self) -> SoldState:
        """Retorna o estado de venda da máquina."""
        return self.sold_state
    
    def get_winner_state(self) -> WinnerState:
        """Retorna o estado de vencedor de 2 gomas"""
        return self.winner_state


    def __str__(self) -> str:
        """Retorna uma representação em string da máquina de gumballs."""
        result = []
        result.append("\nMighty Gumball, Inc.")
        result.append("Python-enabled Standing Gumball Model #2004")
        result.append(
            f"Inventory: {self.count} gumball{'s' if self.count != 1 else ''}"
        )
        result.append(f"Machine is {self.state}")
        return "\n".join(result)