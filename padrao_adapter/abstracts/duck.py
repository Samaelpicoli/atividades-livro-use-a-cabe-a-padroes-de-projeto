from abc import ABC, abstractmethod


class Duck(ABC):
    """
    Classe abstrata que representa um pato.

    Os subclasses devem implementar os métodos `quack` e `fly` para definir
    o comportamento específico do pato.
    """

    def __init__(self):
        """Inicializa um objeto Duck."""
        pass


    @abstractmethod
    def quack(self):
        """
        Emite o som característico do pato.

        Este método deve ser implementado pelas subclasses para fornecer
        a lógica específica do som que o pato faz.
        """
        pass


    @abstractmethod
    def fly(self):
        """
        Permite que o pato voe.

        Este método deve ser implementado pelas subclasses para definir
        como o pato se comporta ao voar.
        """
        pass