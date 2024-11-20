from command import Command
from objects.tv import Tv


class TvOnCommand(Command):

    def __init__(self, tv: Tv):
        """
        Inicializa o comando para ligar a TV.

        Args:
            tv (Tv): Instância da TV a ser controlada.
        """
        self.tv = tv


    def execute(self):
        """Executa o comando para ligar a TV."""
        self.tv.on()


    def undo(self):
        """Desfaz o comando, desligando a TV."""
        self.tv.off()