from iterator import Iterator
from menu_item import MenuItem
from pancake_house_iterator import PancakeHouseMenuIterator


class PancakeHouseMenu:


    def __init__(self):
        self.menu_items = []
        self.add_item("K&B's Pancake Breakfast", 
                      "Pancakes with scrambled eggs, and toast", 
                      True, 
                      2.99)
        self.add_item("Regular Pancake Breakfast", 
                      "Pancakes with fried eggs, sausage", 
                      False, 
                      2.99)
        self.add_item("Blueberry Pancakes", 
                      "Pancakes made with fresh blueberries, and blueberry syrup", 
                      True, 
                      3.49)
        self.add_item("Waffles", 
                      "Waffles, with your choice of blueberries or strawberries", 
                      True, 
                      3.59)
        


    def add_item(self, name, description, vegetarian, price):
        menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items.append(menu_item)



    def create_iterator(self) -> Iterator:
        return iter(self.menu_items)