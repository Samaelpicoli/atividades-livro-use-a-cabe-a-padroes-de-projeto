from commands.hottub_off_command import HottubOffCommand
from commands.hottub_on_command import HottubOnCommand
from commands.light_off_command import LightOffCommand
from commands.light_on_command import LightOnCommand
from commands.macro_command import MacroCommand
from commands.stereo_off_command import StereoOffCommand
from commands.stereo_on_command import StereoOnCommand
from commands.tv_off_command import TvOffCommand
from commands.tv_on_command import TvOnCommand
from objects.hottub import Hottub
from objects.light import Light
from objects.stereo import Stereo
from objects.tv import Tv
from remote_control_with_undo import RemoteControlWithUndo


hottub = Hottub()
light = Light('Living Room')
stereo = Stereo('Living Room')
tv = Tv('Living Room')

hottub_on = HottubOnCommand(hottub)
light_on = LightOnCommand(light)
stereo_on = StereoOnCommand(stereo)
tv_on = TvOnCommand(tv)

hottub_off = HottubOffCommand(hottub)
light_off = LightOffCommand(light)
stereo_off = StereoOffCommand(stereo)
tv_off = TvOffCommand(tv)

# Criação de macros para ligar e desligar
party_on = [light_on, stereo_on, tv_on, hottub_on]
party_off = [light_off, stereo_off, tv_off, hottub_off]

party_on_macro = MacroCommand(party_on)
party_off_macro = MacroCommand(party_off)

remote_control = RemoteControlWithUndo()

remote_control.set_command(0, party_on_macro, party_off_macro)  

print(remote_control)
print('Pushing Macro On')
remote_control.on_button_was_pushed(0)
print('Pushing Macro Off')
remote_control.off_button_was_pushed(0)  