from command import Command
from objects.light import Light


class LightOffCommand(Command):
    """
    Inicializa o comando para desligar a luz.

    Args:
        light (Light): Instância da luz a ser controlada.
    """
    def __init__(self, light: Light):
        self.light = light


    def execute(self):
        """Executa o comando, desligando a luz."""
        self.light.off()

    def undo(self):
        """Desfaz o comando, ligando a luz."""
        self.light.on()