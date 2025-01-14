from commands.ceiling_fan_high_command import CeilingFanHighCommand
from commands.ceiling_fan_medium_command import CeilingFanMediumCommand
from commands.ceiling_fan_off_command import CeilingFanOffCommand
from commands.light_off_command import LightOffCommand
from commands.light_on_command import LightOnCommand
from objects.ceiling_fan import CeilingFan
from objects.light import Light
from remote_control_with_undo import RemoteControlWithUndo



remote_control = RemoteControlWithUndo()
living_room_light = Light('Living Room')


living_room_light_on = LightOnCommand(living_room_light)
living_room_light_off = LightOffCommand(living_room_light)

remote_control.set_command(0, living_room_light_on, living_room_light_off)
remote_control.on_button_was_pushed(0)
remote_control.off_button_was_pushed(0)
print(remote_control)
remote_control.undo_button_was_pushed()
remote_control.off_button_was_pushed(0)
remote_control.on_button_was_pushed(0)
print(remote_control)
remote_control.undo_button_was_pushed()


ceiling_fan = CeilingFan('Living Room')


ceiling_fan_medium = CeilingFanMediumCommand(ceiling_fan)
ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)
ceiling_fan_off_mode = CeilingFanOffCommand(ceiling_fan)

remote_control.set_command(0, ceiling_fan_medium, ceiling_fan_off_mode)
remote_control.set_command(1, ceiling_fan_high, ceiling_fan_off_mode)

remote_control.on_button_was_pushed(0)
remote_control.off_button_was_pushed(0)
print(remote_control)
remote_control.undo_button_was_pushed()
remote_control.on_button_was_pushed(1)
print(remote_control)
remote_control.undo_button_was_pushed()



