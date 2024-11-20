from beverage.beverage import Beverage


class HouseBlend(Beverage):
    """
    Classe que representa o café House Blend.
    """

    def __init__(self, description: str = 'House Blend'):
        """
        Inicializa uma nova instância de House Blend.

        Args:
            description (str): A descrição da bebida (padrão é 'House Blend').
        """
        super().__init__()
        self.description = description

    def cost(self):
        """
        Calcula o custo da bebida com base no tamanho.

        Returns:
            float: O custo da bebida.
        """
        if self.get_size() == Beverage.Size.TALL:
            return 0.89
        elif self.get_size() == Beverage.Size.GRANDE:
            return 0.99
        elif self.get_size() == Beverage.Size.VENTI:
            return 1.09

    def get_description(self):
        """
        Retorna a descrição da bebida.

        Returns:
            str: A descrição da bebida.
        """
        return self.description


class DarkRoast(Beverage):
    """
    Classe que representa o café Dark Roast.
    """

    def __init__(self, description: str = 'Dark Roast'):
        """
        Inicializa uma nova instância de Dark Roast.

        Args:
            description (str): A descrição da bebida (padrão é 'Dark Roast').
        """
        super().__init__()
        self.description = description

    def cost(self):
        """
        Calcula o custo da bebida com base no tamanho.

        Returns:
            float: O custo da bebida.
        """
        if self.get_size() == Beverage.Size.TALL:
            return 0.99
        elif self.get_size() == Beverage.Size.GRANDE:
            return 1.09
        elif self.get_size() == Beverage.Size.VENTI:
            return 1.19

    def get_description(self):
        """
        Retorna a descrição da bebida.

        Returns:
            str: A descrição da bebida.
        """
        return self.description


class Decaf(Beverage):
    """
    Classe que representa o café Decaf (descafeinado).
    """

    def __init__(self, description: str = 'Decaf'):
        """
        Inicializa uma nova instância de Decaf.

        Args:
            description (str): A descrição da bebida (padrão é 'Decaf').
        """
        super().__init__()
        self.description = description

    def cost(self):
        """
        Calcula o custo da bebida com base no tamanho.

        Returns:
            float: O custo da bebida.
        """
        if self.get_size() == Beverage.Size.TALL:
            return 1.05
        elif self.get_size() == Beverage.Size.GRANDE:
            return 1.15
        elif self.get_size() == Beverage.Size.VENTI:
            return 1.25

    def get_description(self):
        """
        Retorna a descrição da bebida.

        Returns:
            str: A descrição da bebida.
        """
        return self.description


class Espresso(Beverage):
    """
    Classe que representa o café Espresso.
    """

    def __init__(self, description: str = 'Espresso'):
        """
        Inicializa uma nova instância de Espresso.

        Args:
            description (str): A descrição da bebida (padrão é 'Espresso').
        """
        super().__init__()
        self.description = description

    def cost(self):
        """
        Calcula o custo da bebida com base no tamanho.

        Returns:
            float: O custo da bebida.
        """
        if self.get_size() == Beverage.Size.TALL:
            return 1.99
        elif self.get_size() == Beverage.Size.GRANDE:
            return 2.09
        elif self.get_size() == Beverage.Size.VENTI:
            return 2.19

    def get_description(self):
        """
        Retorna a descrição da bebida.

        Returns:
            str: A descrição da bebida.
        """
        return self.description