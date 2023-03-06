from abc import abstractmethod, ABC


class StoredItem(ABC):

    def __init__(self, item):
        self.quality = item.quality
        self.sell_in = item.sell_in
        self.message = ""

    @abstractmethod
    def update(self):
        pass
