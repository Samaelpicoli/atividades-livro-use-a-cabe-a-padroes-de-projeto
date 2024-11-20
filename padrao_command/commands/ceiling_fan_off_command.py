from command import Command
from objects.ceiling_fan import CeilingFan


class CeilingFanOffCommand(Command):


    def __init__(self, ceiling_fan: CeilingFan):
        """
        Inicializa o comando para desligar o ventilador de teto.

        Args:
            ceiling_fan (CeilingFan): Instância do ventilador de teto
            a ser controlado.
        """
        self.ceiling_fan = ceiling_fan


    def execute(self):
        """Executa o comando para desligar o ventilador de teto."""
        self.ceiling_fan.off()