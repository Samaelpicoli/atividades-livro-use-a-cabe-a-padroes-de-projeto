class CeilingFan:
    
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0


    def __init__(self, location: str):
        """
        Inicializa um ventilador de teto.

        Args:
            location (str): Localização do ventilador (ex: "Sala de Estar").
        """
        self.location = location
        self.speed = self.OFF


    def high(self):
        """Liga o ventilador de teto na velocidade alta."""
        self.speed = self.HIGH
        print(f"{self.location} ceiling fan is on high")


    def medium(self):
        """Liga o ventilador de teto na velocidade média."""
        self.speed = self.MEDIUM
        print(f"{self.location} ceiling fan is on medium")


    def low(self):
        """Liga o ventilador de teto na velocidade baixa."""
        self.speed = self.LOW
        print(f"{self.location} ceiling fan is on low")


    def off(self):
        """Desliga o ventilador de teto."""
        self.speed = self.OFF
        print(f"{self.location} ceiling fan is off")


    def get_speed(self) -> int:
        """
        Retorna a velocidade atual do ventilador de teto.

        Returns:
            int: Velocidade atual do ventilador.
        """
        return self.speed

