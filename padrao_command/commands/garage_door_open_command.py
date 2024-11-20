from command import Command
from objects.garage_door import GarageDoor


class GarageDoorOpenCommand(Command):


    def __init__(self, garage_door: GarageDoor):
        """
        Inicializa o comando para abrir a porta da garagem.

        Args:
            garage_door (GarageDoor): Instância da porta da
            garagem a ser controlada.
        """
        self.garage_door = garage_door


    def execute(self):
        """Executa o comando para abrir a porta da garagem."""
        self.garage_door.up()