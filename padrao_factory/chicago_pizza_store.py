from pizza_store import PizzaStore
from pizzas_chicago import ChicagoStyleCheesePizza

class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, sabor: str):
        if sabor == 'cheese':
            return ChicagoStyleCheesePizza()
        '''
        elif sabor == 'pepperoni':
            return ChicagoStylePepperoniPizza()
        elif sabor == 'clam':
            return ChicagoStyleClamPizza()
        elif sabor == 'veggie':
            return ChicagoStyleVeggiePizza()
        else:
            return None
        '''