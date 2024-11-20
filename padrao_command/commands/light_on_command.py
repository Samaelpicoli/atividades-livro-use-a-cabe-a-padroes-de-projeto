from command import Command
from objects.light import Light


class LightOnCommand(Command):

    def __init__(self, light: Light):
        """
        Inicializa o comando para desligar a luz.

        Args:
            light (Light): Instância da luz a ser controlada.
        """
        self.light = light


    def execute(self):
        """Executa o comando, ligando a luz."""
        self.light.on()

    def undo(self):
        """Desfaz o comando, desligando a luz."""
        self.light.off()



