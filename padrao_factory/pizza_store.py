from abc import ABC, abstractmethod


class PizzaStore(ABC):
    """
    Classe abstrata que representa uma loja de pizzas.
    """

    @abstractmethod
    def create_pizza(self, item: str):
        """
        Método abstrato para criar uma pizza com base no tipo especificado.

        Args:
            item (str): O tipo de pizza a ser criada.

        Returns:
            Pizza: A pizza criada.
        """
        pass

    def order_pizza(self, tipo: str):
        """
        Método para processar o pedido de uma pizza.

        Args:
            tipo (str): O tipo de pizza a ser pedido.

        Returns:
            Pizza: A pizza preparada.
        """
        pizza = self.create_pizza(tipo)
        print(f"--- Fazendo uma {pizza.get_name()} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza