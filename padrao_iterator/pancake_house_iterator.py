from iterator import Iterator
from menu_item import MenuItem


class PancakeHouseMenuIterator(Iterator):


    def __init__(self, items):
        self.items = items
        self.position = 0


    def has_next(self) -> bool:
        return self.position < len(self.items)


    def next(self) -> MenuItem:
        if self.has_next():
            menu_item = self.items[self.position]
            self.position += 1
            return menu_item
        else:
            raise StopIteration("No more items in the iterator.")