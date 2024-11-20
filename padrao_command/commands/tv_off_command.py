from command import Command
from objects.tv import Tv


class TvOffCommand(Command):

    def __init__(self, tv: Tv):
        """
        Inicializa o comando para desligar a TV.

        Args:
            tv (Tv): Instância da TV a ser controlada.
        """
        self.tv = tv


    def execute(self):
        """Executa o comando para desligar a TV."""
        self.tv.off()


    def undo(self):
        """Desfaz o comando, ligando a TV."""
        self.tv.on()