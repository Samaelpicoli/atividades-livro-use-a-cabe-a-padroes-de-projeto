from command import Command
from objects.stereo import Stereo


class StereoOnWithCDCommand(Command):

    def __init__(self, stereo: Stereo):
        """
        Inicializa o comando para ligar o estéreo e configurar o CD.

        Args:
            stereo (Stereo): Instância do estéreo a ser controlado.
        """
        self.stereo = stereo


    def execute(self):
        """
        Executa o comando para ligar o estéreo, configurar o CD e
        ajustar o volume.
        """
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)