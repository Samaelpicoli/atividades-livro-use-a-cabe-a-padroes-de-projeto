class Stereo:

    def __init__(self, location: str):
        """
        Inicializa o estéreo na localização especificada.

        Args:
            location (str): Localização do estéreo (ex: "Sala de Estar").
        """
        self.location = location


    def on(self):
        """Liga o som estéreo."""
        print(f'{self.location} stereo is on')


    def off(self):
        """Desliga o som estéreo."""
        print(f'{self.location} stereo is off')


    def set_cd(self):
        """Define o estéreo para entrada de CD."""
        print(f'{self.location} stereo is set for CD input')


    def remove_cd(self):
        """Remove o CD do estéreo."""
        print(f'{self.location} stereo removed the CD')


    def set_dvd(self):
        """Define o estéreo para entrada de DVD."""
        print(f'{self.location} stereo is set for DVD input')


    def remove_dvd(self):
        """Remove o DVD do estéreo."""
        print(f'{self.location} stereo removed the DVD')


    def set_radio(self):
        """Define o estéreo para rádio."""
        print(f'{self.location} stereo is set for Radio')


    def disable_radio(self):
        """Desativa a função de rádio do estéreo."""
        print(f'{self.location} stereo disabled Radio')


    def set_volume(self, volume: int):
        """
        Define o volume do estéreo.

        Args:
            volume (str): Nível de volume a ser definido
            (deve estar entre 1 e 11).
        """
        if 1 <= volume <= 11:
            print(f'{self.location} Stereo volume set to {volume}')
        else:
            print(f'{self.location} Stereo volume must be between 1 and 11')


