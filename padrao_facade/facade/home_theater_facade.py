from objects.amplifier import Amplifier
from objects.cd_player import CdPlayer
from objects.dvd_player import DvdPlayer
from objects.popcorn_popper import PopcornPopper
from objects.projector import Projector
from objects.screen import Screen
from objects.theater_lights import TheaterLights
from objects.tuner import Tuner


class HomeTheaterFacade:
    """
    Classe que representa a fachada do sistema de home theater.

    O padrão Facade simplifica a interação com o sistema complexo
    de componentes de home theater, fornecendo uma interface
    unificada para operações comuns, como assistir a um filme,
    ouvir CDs ou rádio. Isso permite que o usuário controle
    facilmente os diferentes dispositivos sem se preocupar com 
    a lógica interna de cada um.
    """

    def __init__(
            self,
            amp: Amplifier,
            tuner: Tuner,
            dvd: DvdPlayer,
            cd: CdPlayer,
            projector: Projector,
            screen: Screen,
            lights: TheaterLights,
            popper: PopcornPopper
        ):
        """
        Inicializa a fachada do home theater com todos os
        componentes necessários.
        """
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watch_movie(self, movie):
        """Prepara o home theater para assistir a um filme."""
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_dvd(self.dvd)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        """Desliga o home theater após assistir a um filme."""
        print("Shutting movie theater down...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

    def listen_to_cd(self, cd_title):
        """Prepara o home theater para ouvir um CD."""
        print("Get ready for an audiophile experience...")
        self.lights.on()
        self.amp.on()
        self.amp.set_volume(5)
        self.amp.set_cd(self.cd)
        self.amp.set_stereo_sound()
        self.cd.on()
        self.cd.play(cd_title)

    def end_cd(self):
        """Desliga o home theater após ouvir um CD."""
        print("Shutting down CD...")
        self.amp.off()
        self.amp.set_cd(self.cd)
        self.cd.eject()
        self.cd.off()

    def listen_to_radio(self, frequency):
        """Sintoniza o rádio em uma frequência especificada."""
        print("Tuning in the airwaves...")
        self.tuner.on()
        self.tuner.set_frequency(frequency)
        self.amp.on()
        self.amp.set_volume(5)
        self.amp.set_tuner(self.tuner)

    def end_radio(self):
        """Desliga o sintonizador de rádio."""
        print("Shutting down the tuner...")
        self.tuner.off()
        self.amp.off()