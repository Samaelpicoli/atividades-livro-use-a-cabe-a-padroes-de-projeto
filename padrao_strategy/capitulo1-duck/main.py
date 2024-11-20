from objects.mallard_duck import MallardDuck
from behavior.fly.fly_no_way import FlyNoWay

if __name__ == '__main__':
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()
    mallard.fly_behavior = FlyNoWay()
    mallard.perform_fly()
    mallard.display()