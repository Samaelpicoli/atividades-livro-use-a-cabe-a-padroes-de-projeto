from abc import ABC, abstractmethod


class Turkey(ABC):
    """
    Classe abstrata que representa um peru.

    Os subclasses devem implementar os métodos `gobble` e `fly` para definir
    o comportamento específico do peru.
    """

    def __init__(self):
        """Inicializa um objeto Turkey."""
        pass


    @abstractmethod
    def gobble(self):
        """
        Emite o som característico do peru.

        Este método deve ser implementado pelas subclasses para fornecer
        a lógica específica do som que o peru faz.
        """
        pass


    @abstractmethod
    def fly(self):
        """Permite que o peru voe.

        Este método deve ser implementado pelas subclasses para definir
        como o peru se comporta ao voar.
        """
        pass