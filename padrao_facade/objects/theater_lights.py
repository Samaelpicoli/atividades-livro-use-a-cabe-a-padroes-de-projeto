class TheaterLights:

    def __init__(self, description):
        """Inicializa as luzes do teatro com uma descrição."""
        self.description = description


    def on(self):
        """Liga as luzes do teatro."""
        print(f"{self.description} on")


    def off(self):
        """Desliga as luzes do teatro."""
        print(f"{self.description} off")


    def dim(self, level):
        """Ajusta o nível de intensidade das luzes."""
        print(f"{self.description} dimming to {level}%")


    def __str__(self):
        """Retorna a descrição das luzes do teatro."""
        return self.description