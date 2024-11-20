from ny_pizza_store import NyPizzaStore
from chicago_pizza_store import ChicagoPizzaStore

ny_store = NyPizzaStore()
chicago_store = ChicagoPizzaStore()

pizza = ny_store.order_pizza('cheese')

pizza = chicago_store.order_pizza('cheese')