from command import Command
from objects.stereo import Stereo


class StereoOffCommand(Command):

    def __init__(self, stereo: Stereo):
        """
        Inicializa o comando para desligar o estéreo.

        Args:
            stereo (Stereo): Instância do estéreo a ser controlado.
        """
        self.stereo = stereo


    def execute(self):
        """Executa o comando para desligar o estéreo."""
        self.stereo.off()