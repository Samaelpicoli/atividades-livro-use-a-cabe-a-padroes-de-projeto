class Projector:

    def __init__(self, description, dvd_player):
        """Inicializa o projetor com uma descrição e um reprodutor de DVD."""
        self.description = description
        self.dvd_player = dvd_player


    def on(self):
        """Liga o projetor."""
        print(f"{self.description} on")


    def off(self):
        """Desliga o projetor."""
        print(f"{self.description} off")


    def wide_screen_mode(self):
        """Define o modo widescreen (proporção 16x9)."""
        print(f"{self.description} in widescreen mode (16x9 aspect ratio)")


    def tv_mode(self):
        """Define o modo TV (proporção 4x3)."""
        print(f"{self.description} in tv mode (4x3 aspect ratio)")


    def __str__(self):
        """Retorna a descrição do projetor."""
        return self.description