from commands.no_command import NoCommand


class RemoteControl:

    def __init__(self):
        """
        Inicializa o controle remoto com comandos vazios para ligar e
        desligar.

        Cria listas para comandos de ligar e desligar, cada uma com
        7 slots,
        inicializadas com comandos nulos (NoCommand).
        """
        self.on_commands = [NoCommand() for _ in range(7)]
        self.off_commands = [NoCommand() for _ in range(7)]


    def set_command(self, slot: int, on_command, off_command):
        """
        Define os comandos de ligar e desligar para um slot específico.

        Args:
            slot (int): O índice do slot onde os comandos serão definidos.
            on_command: O comando a ser executado quando o botão de ligar
            é pressionado.
            off_command: O comando a ser executado quando o botão de desligar
            é pressionado.
        """
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command


    def on_button_was_pushed(self, slot: int):
        """
        Executa o comando de ligar associado ao slot especificado.

        Args:
            slot (int): O índice do slot cujo comando de ligar
            será executado.
        """
        self.on_commands[slot].execute()


    def off_button_was_pushed(self, slot: int):
        """
        Executa o comando de desligar associado ao slot especificado.

        Args:
            slot (int): O índice do slot cujo comando de desligar será
            executado.
        """
        self.off_commands[slot].execute()


    def __str__(self) -> str:
        """
        Retorna uma representação em string do controle remoto,
        incluindo os comandos configurados.
        """
        string_buffer = "\n----- Remote Control -----\n"
        for i in range(len(self.on_commands)):
            on_command_name = self.on_commands[i].__class__.__name__
            off_command_name = self.off_commands[i].__class__.__name__
            string_buffer += f"[slot {i}] {on_command_name}   {off_command_name}\n"
        return string_buffer