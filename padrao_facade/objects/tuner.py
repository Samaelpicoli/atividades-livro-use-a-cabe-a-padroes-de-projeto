class Tuner:

    def __init__(self, description, amplifier):
        """Inicializa o sintonizador com uma descrição e um amplificador."""
        self.description = description
        self.amplifier = amplifier
        self.frequency = 0.0


    def on(self):
        """Liga o sintonizador."""
        print(f"{self.description} on")


    def off(self):
        """Desliga o sintonizador."""
        print(f"{self.description} off")


    def set_frequency(self, frequency):
        """Define a frequência do sintonizador."""
        print(f"{self.description} setting frequency to {frequency}")
        self.frequency = frequency


    def set_am(self):
        """Define o modo AM."""
        print(f"{self.description} setting AM mode")


    def set_fm(self):
        """Define o modo FM."""
        print(f"{self.description} setting FM mode")


    def __str__(self):
        """Retorna a descrição do sintonizador."""
        return self.description