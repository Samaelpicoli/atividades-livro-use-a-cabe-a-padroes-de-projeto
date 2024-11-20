class Tv:

    def __init__(self, location: str):
        """
        Inicializa a TV na localização especificada.

        Args:
            location (str): Localização da TV (ex: "Sala de Estar").
        """
        self.location = location


    def on(self):
        """Liga a TV"""
        print(f'{self.location} Tv is On')


    def off(self):
        """Desliga a TV"""
        print(f'{self.location} Tv is Off')


    def set_input_channel(self, channel: int):
        """Define o canal de entrada para a TV.

        Args:
            channel (int): Canal a ser definido (ex: 1, 2, 3, ...).
        """
        print(f'Channel {channel} is set for VCR')