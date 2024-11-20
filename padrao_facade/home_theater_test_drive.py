from facade.home_theater_facade import HomeTheaterFacade

from objects.amplifier import Amplifier
from objects.cd_player import CdPlayer
from objects.dvd_player import DvdPlayer
from objects.popcorn_popper import PopcornPopper
from objects.projector import Projector
from objects.screen import Screen
from objects.theater_lights import TheaterLights
from objects.tuner import Tuner



def main():
    amp = Amplifier("Top-O-Line Amplifier")
    tuner = Tuner("Top-O-Line AM/FM Tuner", amp)
    dvd = DvdPlayer("Top-O-Line DVD Player", amp)
    cd = CdPlayer("Top-O-Line CD Player", amp)
    projector = Projector("Top-O-Line Projector", dvd)
    lights = TheaterLights("Theater Ceiling Lights")
    screen = Screen("Theater Screen")
    popper = PopcornPopper("Popcorn Popper")

    home_theater = HomeTheaterFacade(amp, tuner, dvd, cd, projector, screen, lights, popper)

    home_theater.watch_movie("Raiders of the Lost Ark")
    home_theater.end_movie()

if __name__ == "__main__":
    main()