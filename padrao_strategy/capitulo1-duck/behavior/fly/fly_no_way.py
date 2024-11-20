from behavior.fly.fly_behavior import FlyBehavior


class FlyNoWay(FlyBehavior):
    def fly(self):
        print('não posso voar')