from condiments.condiment_decorator import CondimentDecorator
from beverage.beverage import Beverage


class Milk(CondimentDecorator):
    """
    Classe que representa o condimento de leite (Milk).

    O padrão Decorator é utilizado para adicionar dinamicamente a
    funcionalidade de condimentos a uma bebida, permitindo que
    diferentes tipos de condimentos sejam combinados sem alterar
    a estrutura das classes base.
    """

    def __init__(self, beverage: Beverage):
        """
        Inicializa uma nova instância de Milk.

        Args:
            beverage (Beverage): A bebida que está sendo decorada com leite.
        """
        super().__init__()
        self.beverage = beverage

    def cost(self):
        """
        Calcula o custo total da bebida com o condimento Milk.

        Returns:
            float: O custo total da bebida com leite.
        """
        if self.beverage.get_size() == Beverage.Size.TALL:
            return 0.10 + self.beverage.cost()
        elif self.beverage.get_size() == Beverage.Size.GRANDE:
            return 0.15 + self.beverage.cost()
        elif self.beverage.get_size() == Beverage.Size.VENTI:
            return 0.20 + self.beverage.cost()

    def get_description(self):
        """
        Retorna a descrição da bebida com o condimento Milk.

        Returns:
            str: A descrição da bebida com leite.
        """
        return self.beverage.get_description() + ', Milk'


class Whip(CondimentDecorator):
    """
    Classe que representa o condimento de chantilly (Whip).

    O padrão Decorator é utilizado para adicionar dinamicamente a
    funcionalidade de condimentos a uma bebida, permitindo que
    diferentes tipos de condimentos sejam combinados sem alterar
    a estrutura das classes base.
    """

    def __init__(self, beverage: Beverage):
        """
        Inicializa uma nova instância de Whip.

        Args:
            beverage (Beverage): A bebida que está sendo decorada com chantilly.
        """
        super().__init__()
        self.beverage = beverage

    def cost(self):
        """
        Calcula o custo total da bebida com o condimento Whip.

        Returns:
            float: O custo total da bebida com chantilly.
        """
        if self.beverage.get_size() == Beverage.Size.TALL:
            return 0.10 + self.beverage.cost()
        elif self.beverage.get_size() == Beverage.Size.GRANDE:
            return 0.15 + self.beverage.cost()
        elif self.beverage.get_size() == Beverage.Size.VENTI:
            return 0.20 + self.beverage.cost()

    def get_description(self):
        """
        Retorna a descrição da bebida com o condimento Whip.

        Returns:
            str: A descrição da bebida com chantilly.
        """
        return self.beverage.get_description() + ', Whip'


class Soy(CondimentDecorator):
    """
    Classe que representa o condimento de soja (Soy).

    O padrão Decorator é utilizado para adicionar dinamicamente a
    funcionalidade de condimentos a uma bebida, permitindo que
    diferentes tipos de condimentos sejam combinados sem alterar
    a estrutura das classes base.
    """

    def __init__(self, beverage: Beverage):
        """
        Inicializa uma nova instância de Soy.

        Args:
            beverage (Beverage): A bebida que está sendo decorada com soja.
        """
        super().__init__()
        self.beverage = beverage

    def cost(self):
        """
        Calcula o custo total da bebida com o condimento Soy.

        Returns:
            float: O custo total da bebida com soja.
        """
        if self.beverage.get_size() == Beverage.Size.TALL:
            return 0.15 + self.beverage.cost()
        elif self.beverage.get_size() == Beverage.Size.GRANDE:
            return 0.20 + self.beverage.cost()
        elif self.beverage.get_size() == Beverage.Size.VENTI:
            return 0.25 + self.beverage.cost()

    def get_description(self):
        """
        Retorna a descrição da bebida com o condimento Soy.

        Returns:
            str: A descrição da bebida com soja.
        """
        return self.beverage.get_description() + ', Soy'


class Mocha(CondimentDecorator):
    """
    Classe que representa o condimento Mocha.

    O padrão Decorator é utilizado para adicionar dinamicamente a
    funcionalidade de condimentos a uma bebida, permitindo que
    diferentes tipos de condimentos sejam combinados sem alterar
    a estrutura das classes base.
    """

    def __init__(self, beverage: Beverage):
        """
        Inicializa uma nova instância de Mocha.

        Args:
            beverage (Beverage): A bebida que está sendo decorada com Mocha.
        """
        super().__init__()
        self.beverage = beverage

    def cost(self):
        """
        Calcula o custo total da bebida com o condimento Mocha.

        Returns:
            float: O custo total da bebida com Mocha.
        """
        if self.beverage.get_size() == Beverage.Size.TALL:
            return 0.20 + self.beverage.cost()
        elif self.beverage.get_size() == Beverage.Size.GRANDE:
            return 0.25 + self.beverage.cost()
        elif self.beverage.get_size() == Beverage.Size.VENTI:
            return 0.30 + self.beverage.cost()

    def get_description(self):
        """
        Retorna a descrição da bebida com o condimento Mocha.

        Returns:
            str: A descrição da bebida com Mocha.
        """
        return self.beverage.get_description() + ', Mocha'