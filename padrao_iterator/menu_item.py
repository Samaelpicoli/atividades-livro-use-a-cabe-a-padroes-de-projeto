from menu_component import MenuComponent


class MenuItem(MenuComponent):


    def __init__(self, name: str, description: str, vegetarian: str, price: str):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price


    def get_name(self) -> str:
        return self.name


    def get_description(self) -> str:
        return self.description


    def get_price(self) -> int|float:
        return self.price


    def is_vegetarian(self) -> bool:
        return self.vegetarian


    def print_item(self):
        print(f"    {self.get_name()}", end="")
        if self.is_vegetarian():
            print(" (v)", end="")
        print(f", {self.get_price()}")
        print(f"    -- {self.get_description()}")