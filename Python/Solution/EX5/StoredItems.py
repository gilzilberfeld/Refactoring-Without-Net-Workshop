from abc import abstractmethod, ABC


class StoredItem(ABC):

    def __init__(self, item):
        self.item = item
        self.message = ""

    @abstractmethod
    def update(self):
        pass

    def decrease_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def increase_quality(self):
        self.item.quality = self.item.quality + 1

    def decrease_quality(self):
        self.item.quality = self.item.quality - 1


class DexterityOrElixir(StoredItem):
    def update(self):
        if self.item.quality > 0:
            self.decrease_quality()
        self.decrease_sell_in()
        if self.item.quality > 0:
            if self.item.sell_in < 0:
                self.decrease_quality()


class Backstage(StoredItem):
    def update(self):
        if self.item.quality < 50:
            self.increase_quality()
            if self.item.quality < 50:
                if self.item.sell_in < 11:
                    self.increase_quality()
                if self.item.sell_in < 6:
                    self.increase_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.item.quality = 0


class AgedBrie(StoredItem):
    def update(self):
        if self.item.quality < 50:
            self.increase_quality()
        self.decrease_sell_in()
        if self.item.quality < 50:
            if self.item.sell_in < 0:
                self.increase_quality()

class Sulfuras(StoredItem):
    def update(self):
        pass

class Conjured(StoredItem):
    def update(self):
        if self.item.quality > 0:
            self.decrease_quality()
            self.decrease_quality()
        self.decrease_sell_in()