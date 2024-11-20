from pizza_store import PizzaStore
from pizzas_ny import NyStyleCheesePizza

class NyPizzaStore(PizzaStore):

    def create_pizza(self, sabor: str):
        if sabor == 'cheese':
            return NyStyleCheesePizza()
        '''
        elif sabor == 'pepperoni':
            return NyStylePepperoniPizza()
        elif sabor == 'clam':
            return NyStyleClamPizza()
        elif sabor == 'veggie':
            return NyStyleVeggiePizza()
        else:
            return None
        '''


