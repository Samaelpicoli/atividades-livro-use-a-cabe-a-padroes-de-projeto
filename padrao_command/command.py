class Command:


    def execute(self):
        """
        Executa o comando.

        Este método deve ser implementado por subclasses
        para definir a ação a ser realizada.
        """
        pass


    def undo(self):
        """
        Desfaz a última ação realizada pelo comando.

        Este método deve ser implementado por subclasses
        para definir a ação de desfaçagem.
        """
        pass