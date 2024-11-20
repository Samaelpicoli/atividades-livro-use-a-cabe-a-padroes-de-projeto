from command import Command

class MacroCommand(Command):
    def __init__(self, commands: list):
        self.commands = commands

    def execute(self):
        """Executa todos os comandos na macro."""
        for command in self.commands:
            command.execute()

    def undo(self):
        """Desfaz todos os comandos na macro."""
        for command in self.commands:
            command.undo()