from beverage.beverage import Beverage

class CondimentDecorator(Beverage):
    """
    Classe/Interface abstrata que representa um decorador de condimento.

    O padrão Decorator permite adicionar funcionalidade a objetos de
    forma dinâmica, sem alterar a estrutura das classes originais.
    Neste caso, a classe CondimentDecorator é usada para estender
    a funcionalidade de bebidas, permitindo que condimentos sejam
    adicionados de forma flexível e reutilizável.
    """

    def get_description(self):
        """
        Retorna a descrição do condimento.

        Returns:
            str: A descrição do condimento.
        """
        pass