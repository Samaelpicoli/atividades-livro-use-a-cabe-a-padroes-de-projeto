from behavior.quack.quack_behavior import QuackBehavior


class MuteQuack(QuackBehavior):
    def quack(self):
        print('Shiiii...')