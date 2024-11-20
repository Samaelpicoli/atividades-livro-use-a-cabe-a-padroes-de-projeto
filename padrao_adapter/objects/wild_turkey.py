from abstracts.turkey import Turkey


class WildTurkey(Turkey):

    """Representa um peru selvagem, que é um tipo concreto de Turkey."""

    def __init__(self):
        """Inicializa um objeto WildTurkey."""
        super().__init__()


    def gobble(self):
        """Emite o som característico de um peru selvagem."""
        print('Gobble gobble')


    def fly(self):
        """
        Simula o voo de um peru selvagem, que é limitado a curtas distâncias.
        """
        print('I\'m flying a short distance')