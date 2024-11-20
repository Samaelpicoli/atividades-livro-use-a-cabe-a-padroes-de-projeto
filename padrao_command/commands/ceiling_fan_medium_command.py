from command import Command
from objects.ceiling_fan import CeilingFan


class CeilingFanMediumCommand(Command):


    def __init__(self, ceiling_fan: CeilingFan):
        """
        Inicializa o comando para ligar o ventilador de teto na velocidade
        média.

        Args:
            ceiling_fan (CeilingFan): Instância do ventilador de teto
            a ser controlado.
        """
        self.ceiling_fan = ceiling_fan
        self.prev_speed = None


    def execute(self):
        """Executa o comando de ligar o ventilador na velocidade média."""
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.medium()


    def undo(self):
        """Desfaz o comando, retornando à velocidade anterior."""
        if self.prev_speed == self.ceiling_fan.high():
            self.ceiling_fan.high()
        elif self.prev_speed == self.ceiling_fan.medium():
            self.ceiling_fan.medium()
        elif self.prev_speed == self.ceiling_fan.low():
            self.ceiling_fan.low()
        elif self.prev_speed == self.ceiling_fan.off:
            self.ceiling_fan.off()