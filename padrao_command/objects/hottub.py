class Hottub:


    def __init__(self):
        """
        Inicializa o hottub com temperatura inicial de 0 graus.
        """
        self.temperature = 0


    def on(self):
        """Liga o hottub."""
        self.on = True
        print("Hottub is on")


    def off(self):
        """Desliga o hottub."""
        self.on = False
        print("Hottub is off")


    def bubbles_on(self):
        """Ativa as bolhas do hottub."""
        if self.on:
            print("Hottub is bubbling!")
        else:
            print("Hottub is off, cannot bubble.")


    def bubbles_off(self):
        """Desativa as bolhas do hottub."""
        if self.on:
            print("Hottub is not bubbling")
        else:
            print("Hottub is off, cannot stop bubbling.")


    def jets_on(self):
        """Liga os jatos do hottub."""
        if self.on:
            print("Hottub jets are on")
        else:
            print("Hottub is off, cannot turn on the jets.")


    def jets_off(self):
        """Desliga os jatos do hottub."""
        if self.on:
            print("Hottub jets are off")
        else:
            print("Hottub is off, cannot turn off the jets.")


    def set_temperature(self, temperature: int):
        """Define a temperatura do hottub."""
        self.temperature = temperature
        print(f"Hottub temperature set to {temperature} degrees")


    def heat(self):
        """Aquece o hottub a 105 graus."""
        self.temperature = 105
        print("Hottub is heating to a steaming 105 degrees")


    def cool(self):
        """Esfria o hottub a 98 graus."""
        self.temperature = 98
        print("Hottub is cooling to 98 degrees")

