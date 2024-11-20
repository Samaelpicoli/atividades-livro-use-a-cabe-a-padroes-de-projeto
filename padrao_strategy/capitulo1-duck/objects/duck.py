from abc import ABC, abstractmethod

from behavior.fly.fly_behavior import FlyBehavior
from behavior.quack.quack_behavior import QuackBehavior


class Duck(ABC):

    
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self._fly_behavior = fly_behavior
        self._quack_behavior = quack_behavior

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self._fly_behavior.fly()

    def perform_quack(self):
        self._quack_behavior.quack()
        
    @property
    def fly_behavior(self):
        return self._fly_behavior
    
    @fly_behavior.setter
    def fly_behavior(self, new_fly_behavior: FlyBehavior):
        self._fly_behavior = new_fly_behavior
    
    @property
    def quack_behavior(self):
        return self._quack_behavior
    
    @quack_behavior.setter
    def quack_behavior(self, new_quack_behavior: QuackBehavior):
        self._quack_behavior = new_quack_behavior
