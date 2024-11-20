from abc import ABC, abstractmethod
from enum import Enum


class Beverage(ABC):
    """
    Classe/Interface abstrata que representa uma bebida.
    """

    def __init__(self):
        """
        Inicializa uma nova bebida com tamanho padrão TALL e descrição
        desconhecida.
        """
        self.size = Beverage.Size.TALL
        self.description = 'Unknown Beverage'


    class Size(Enum):
        """
        Enumeração que define os tamanhos disponíveis para a bebida.
        """
        TALL = "TALL"
        GRANDE = "GRANDE"
        VENTI = "VENTI"


    @abstractmethod
    def cost(self):
        """
        Método abstrato que deve ser implementado pelas subclasses para
        calcular o custo da bebida.

        Returns:
            float: O custo da bebida.
        """
        pass


    def get_description(self):
        """
        Retorna a descrição da bebida.

        Returns:
            str: A descrição da bebida.
        """
        return self.description


    def set_size(self, size: Size):
        """
        Define o tamanho da bebida.

        Args:
            size (Size): O tamanho a ser definido para a bebida.
        """
        self.size = size


    def get_size(self):
        """
        Retorna o tamanho atual da bebida.

        Returns:
            Size: O tamanho da bebida.
        """
        return self.size