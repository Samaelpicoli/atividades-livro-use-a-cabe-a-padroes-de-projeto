class Light:

    def __init__(self, location: str):
        """
        Inicializa a luz na localização especificada.

        Args:
            location (str): Localização da luz (ex: "Sala de Estar").
        """
        self.location = location


    def on(self):
        """Liga a luz."""
        print(f'{self.location} light is On')


    def off(self):
        """Desliga a luz."""
        print(f'{self.location} light is Off')