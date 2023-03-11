from abc import abstractmethod, ABC


class StoredItem(ABC):

    def __init__(self, item):
        self.item = item
        self.message = ""
        self.name = ""

    @abstractmethod
    def update(self):
        pass

    def decrease_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def increase_quality(self):
        self.item.quality = self.item.quality + 1

    def decrease_quality(self):
        self.item.quality = self.item.quality - 1

    def update_message(self):
        self.message = "{0} Updated - Quality: {1}, SellIn: {2}".format(self.name, self.item.quality, self.item.sell_in)


class DexterityOrElixir(StoredItem):
    def __init__(self, item):
        super().__init__(item)
        self.name = "Elixir"

    def update(self):
        if self.item.quality > 0:
            self.decrease_quality()
        self.decrease_sell_in()
        if self.item.quality > 0:
            if self.item.sell_in < 0:
                self.decrease_quality()
        self.update_message()


class Backstage(StoredItem):
    def __init__(self, item):
        super().__init__(item)
        self.name = "Backstage Passes"

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
        self.update_message()


class AgedBrie(StoredItem):
    def __init__(self, item):
        super().__init__(item)
        self.name = "Aged Brie"

    def update(self):
        if self.item.quality < 50:
            self.increase_quality()
        self.decrease_sell_in()
        if self.item.quality < 50:
            if self.item.sell_in < 0:
                self.increase_quality()
        self.update_message()


class Sulfuras(StoredItem):
    def __init__(self, item):
        super().__init__(item)
        self.name = "Sulfuras"

    def update(self):
        self.update_message()


class Conjured(StoredItem):
    def __init__(self, item):
        super().__init__(item)
        self.name = "Conjured"

    def update(self):
        if self.item.quality > 0:
            self.decrease_quality()
            self.decrease_quality()
        self.decrease_sell_in()
        self.update_message()
