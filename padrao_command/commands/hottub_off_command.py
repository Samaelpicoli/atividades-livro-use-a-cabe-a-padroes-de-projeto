from command import Command
from objects.hottub import Hottub


class HottubOffCommand(Command):


    def __init__(self, hottub: Hottub):
        """
        Inicializa o comando para desligar o hottub.

        Args:
            hottub (Hottub): Instância do hottub a ser controlado.
        """
        self.hottub = hottub


    def execute(self):
        """Executa o comando para esfriar e desligar o hottub."""
        self.hottub.cool()
        self.hottub.off()


    def undo(self):
        """Desfaz o comando, ligando o hottub e aquecendo-o."""
        self.hottub.heat()
        self.hottub.on()
