from objects.duck import Duck
from behavior.fly.fly_no_way import FlyNoWay
from behavior.fly.fly_rocket_powered import FlyRocketPowered
from behavior.quack.quack import Quack


class ModelDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Quack())
 
    def display(self):
        print('sou um modelo pato')

