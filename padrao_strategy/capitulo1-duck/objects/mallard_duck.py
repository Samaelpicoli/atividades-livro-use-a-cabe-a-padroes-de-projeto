from objects.duck import Duck
from behavior.fly.fly_no_way import FlyNoWay
from behavior.fly.fly_with_wings import FlyWithWings
from behavior.quack.quack import Quack



class MallardDuck(Duck):

    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print('I m a real Mallard Duck')

