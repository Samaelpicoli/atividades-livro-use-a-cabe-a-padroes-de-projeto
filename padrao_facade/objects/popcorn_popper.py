class PopcornPopper:

    def __init__(self, description):
        """Inicializa a máquina de pipoca com uma descrição."""
        self.description = description


    def on(self):
        """Liga a máquina de pipoca."""
        print(f"{self.description} on")


    def off(self):
        """Desliga a máquina de pipoca."""
        print(f"{self.description} off")


    def pop(self):
        """Começa a estourar pipocas."""
        print(f"{self.description} popping popcorn!")


    def __str__(self):
        """Retorna a descrição da máquina de pipoca."""
        return self.description