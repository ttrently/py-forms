#

from typing import Any


class Model:
    
    def __init__(self)->None:
        self._items = []

    def count(self) -> int:
        ''' Returns row count. '''
        return len(self.items())
    
    def item(self, index: int) -> Any:
        ''' Returns item at `index`. '''
        try:
            return self._items[index]
        except IndexError:
            return None

    def items(self) -> list:
        return self._items
