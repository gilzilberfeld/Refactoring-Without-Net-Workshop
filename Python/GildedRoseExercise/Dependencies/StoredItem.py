from abc import abstractmethod, ABC


class StoredItem(ABC):

    def __init__(self, item):
        self.item = item
        self.message = ""

    @abstractmethod
    def update(self):
        pass
