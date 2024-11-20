from abc import ABC, abstractmethod


class MenuComponent(ABC):
    
    
    @abstractmethod
    def get_name(self):
        pass


    @abstractmethod
    def get_description(self):
        pass
    

    @abstractmethod
    def get_price(self):
        pass
    

    @abstractmethod
    def is_vegetarian(self):
        pass
    

    @abstractmethod
    def print_item(self):
        pass