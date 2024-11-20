class Screen:

    def __init__(self, description):
        """Inicializa a tela com uma descrição."""
        self.description = description


    def up(self):
        """Levanta a tela."""
        print(f"{self.description} going up")


    def down(self):
        """Desce a tela."""
        print(f"{self.description} going down")


    def __str__(self):
        """Retorna a descrição da tela."""
        return self.description