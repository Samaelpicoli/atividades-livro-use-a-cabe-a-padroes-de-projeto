from abstracts.duck import Duck


class MallardDuck(Duck):

    """Representa um pato Mallard, que é um tipo concreto de Duck."""

    def __init__(self):
        """Inicializa um objeto MallardDuck."""
        super().__init__()


    def quack(self):
        """Emite o som característico de um pato Mallard."""
        print('Quack')


    def fly(self):
        """Simula o voo de um pato Mallard."""
        print('I\'m flying')