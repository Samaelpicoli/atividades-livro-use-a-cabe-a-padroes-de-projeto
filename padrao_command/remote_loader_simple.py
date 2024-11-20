from commands.ceiling_fan_off_command import CeilingFanOffCommand
from commands.ceiling_fan_low_command import CeilingFanLowCommand
from commands.garage_door_close_command import GarageDoorCloseCommand
from commands.garage_door_open_command import GarageDoorOpenCommand
from commands.light_off_command import LightOffCommand
from commands.light_on_command import LightOnCommand
from commands.stereo_off_command import StereoOffCommand
from commands.stereo_on_command import StereoOnCommand
from commands.stereo_on_with_cd_command import StereoOnWithCDCommand
from objects.ceiling_fan import CeilingFan
from objects.garage_door import GarageDoor
from objects.light import Light
from objects.stereo import Stereo
from remote_control import RemoteControl



remote_control = RemoteControl()

light_living_room = Light('Living Room')
light_kitchen = Light('Kitchen')
ceiling_fan = CeilingFan('Livinh Room')
garage_door = GarageDoor()
stereo = Stereo('Living Room')


light_on_living_room = LightOnCommand(light_living_room)
light_off_living_room = LightOffCommand(light_living_room)
light_on_kitchen = LightOnCommand(light_kitchen)
light_off_kitchen = LightOffCommand(light_kitchen)

ceiling_fan_on = CeilingFanLowCommand(ceiling_fan)
ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

garage_door_up = GarageDoorOpenCommand(garage_door)
garage_door_down = GarageDoorCloseCommand(garage_door)

stereo_on_with_cd = StereoOnWithCDCommand(stereo)
stereo_off = StereoOffCommand(stereo)

remote_control.set_command(0, light_on_living_room, light_off_living_room)
remote_control.set_command(1, light_on_kitchen, light_off_kitchen)
remote_control.set_command(2, ceiling_fan_on, ceiling_fan_off)
remote_control.set_command(3, garage_door_up, garage_door_down)
remote_control.set_command(4, stereo_on_with_cd, stereo_off)

print(remote_control)
remote_control.on_button_was_pushed(0)
remote_control.off_button_was_pushed(0)
remote_control.on_button_was_pushed(1)
remote_control.off_button_was_pushed(1)
remote_control.on_button_was_pushed(2)
remote_control.off_button_was_pushed(2)
remote_control.on_button_was_pushed(3)
remote_control.off_button_was_pushed(3)
remote_control.on_button_was_pushed(4)
remote_control.off_button_was_pushed(4)

