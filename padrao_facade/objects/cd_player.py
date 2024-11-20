class CdPlayer:

    def __init__(self, description, amplifier):
        """Inicializa o reprodutor de CD com uma descrição e um amplificador."""
        self.description = description
        self.amplifier = amplifier
        self.current_track = 0
        self.title = None


    def on(self):
        """Liga o reprodutor de CD."""
        print(f"{self.description} on")


    def off(self):
        """Desliga o reprodutor de CD."""
        print(f"{self.description} off")


    def eject(self):
        """Ejetar o CD atual."""
        self.title = None
        print(f"{self.description} eject")


    def play(self, title):
        """Reproduz o CD com o título especificado."""
        self.title = title
        self.current_track = 0
        print(f"{self.description} playing \"{title}\"")


    def play_track(self, track):
        """Reproduz a faixa especificada do CD."""
        if self.title is None:
            print(f"{self.description} can't play track {self.current_track}, no CD inserted")
        else:
            self.current_track = track
            print(f"{self.description} playing track {self.current_track}")


    def stop(self):
        """Para a reprodução atual."""
        self.current_track = 0
        print(f"{self.description} stopped")


    def pause(self):
        """Pausa a reprodução atual."""
        print(f"{self.description} paused \"{self.title}\"")


    def __str__(self):
        """Retorna a descrição do reprodutor de CD."""
        return self.description