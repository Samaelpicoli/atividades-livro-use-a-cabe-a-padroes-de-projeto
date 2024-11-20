class DvdPlayer:

    def __init__(self, description, amplifier):
        """Inicializa o reprodutor de DVD com uma descrição e um amplificador."""
        self.description = description
        self.amplifier = amplifier
        self.current_track = 0
        self.movie = None


    def on(self):
        """Liga o reprodutor de DVD."""
        print(f"{self.description} on")


    def off(self):
        """Desliga o reprodutor de DVD."""
        print(f"{self.description} off")


    def eject(self):
        """Ejetar o DVD atual."""
        self.movie = None
        print(f"{self.description} eject")


    def play(self, movie):
        """Reproduz o filme especificado."""
        self.movie = movie
        self.current_track = 0
        print(f"{self.description} playing \"{movie}\"")


    def play_track(self, track):
        """Reproduz a faixa especificada do DVD."""
        if self.movie is None:
            print(f"{self.description} can't play track {track}, no DVD inserted")
        else:
            self.current_track = track
            print(f"{self.description} playing track {self.current_track} of \"{self.movie}\"")


    def stop(self):
        """Para a reprodução atual."""
        self.current_track = 0
        print(f"{self.description} stopped \"{self.movie}\"")


    def pause(self):
        """Pausa a reprodução atual."""
        print(f"{self.description} paused \"{self.movie}\"")


    def set_two_channel_audio(self):
        """Define o áudio em dois canais."""
        print(f"{self.description} set two channel audio")


    def set_surround_audio(self):
        """Define o áudio surround."""
        print(f"{self.description} set surround audio")


    def __str__(self):
        """Retorna a descrição do reprodutor de DVD."""
        return self.description