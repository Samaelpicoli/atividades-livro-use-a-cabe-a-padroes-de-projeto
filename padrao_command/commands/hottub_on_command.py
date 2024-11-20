from command import Command
from objects.hottub import Hottub


class HottubOnCommand(Command):


    def __init__(self, hottub: Hottub):
        """
        Inicializa o comando para ligar o hottub.

        Args:
            hottub (Hottub): Instância do hottub a ser controlado.
        """
        self.hottub = hottub


    def execute(self):
        """
        Executa o comando para ligar o hottub, aquecê-lo e ativar as bolhas.
        """
        self.hottub.on()
        self.hottub.heat()
        self.hottub.bubbles_on()


    def undo(self):
        """
        Desfaz o comando, desligando as bolhas, resfriando 
        e desligando o hottub.
        """
        self.hottub.bubbles_off()
        self.hottub.cool()
        self.hottub.off()