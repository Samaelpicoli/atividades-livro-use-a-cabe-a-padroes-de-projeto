class Amplifier:

    def __init__(
            self,
            description,
            tuner = None,
            dvd = None,
            cd = None
        ):
        """Inicializa o amplificador com uma descrição."""
        self.description = description
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd


    def on(self):
        """Liga o amplificador."""
        print(f"{self.description} on")


    def off(self):
        """Desliga o amplificador."""
        print(f"{self.description} off")


    def set_stereo_sound(self):
        """Define o modo estéreo."""
        print(f"{self.description} stereo mode on")


    def set_surround_sound(self):
        """Define o modo surround (5 alto-falantes, 1 subwoofer)."""
        print(f"{self.description} surround sound on (5 speakers, 1 subwoofer)")


    def set_volume(self, level):
        """Define o volume para o nível especificado."""
        print(f"{self.description} setting volume to {level}")


    def set_tuner(self, tuner):
        """Define o sintonizador do amplificador."""
        print(f"{self.description} setting tuner to {tuner}")
        self.tuner = tuner


    def set_dvd(self, dvd):
        """Define o reprodutor de DVD do amplificador."""
        print(f"{self.description} setting DVD player to {dvd}")
        self.dvd = dvd


    def set_cd(self, cd):
        """Define o reprodutor de CD do amplificador."""
        print(f"{self.description} setting CD player to {cd}")
        self.cd = cd


    def __str__(self):
        """Retorna a descrição do amplificador."""
        return self.description