# -*- coding: utf-8 -*-

class GildedRose2(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item(item)

    def update_item(self, item):
        if item.name == "Aged Brie":
            if item.quality < 50:
                self.increase_quality(item)
            self.decrease_sellin(item)
            if item.quality < 50:
                if item.sell_in < 0:
                    self.increase_quality(item)
            return
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.quality < 50:
                self.increase_quality(item)
                if item.quality < 50:
                    if item.sell_in < 11:
                        self.increase_quality(item)
                    if item.sell_in < 6:
                        self.increase_quality(item)
            self.decrease_sellin(item)
            if item.sell_in < 0:
                item.quality = 0
            return
        if item.name == "+5 Dexterity Vest" or item.name == "Elixir of the Mongoose":
            if item.quality > 0:
                self.decrease_quality(item)
            self.decrease_sellin(item)
            if item.quality > 0:
                if item.sell_in < 0:
                    self.decrease_quality(item)

    def update_backstage_passes_again(self, item):
        if item.sell_in < 0:
            item.quality = 0

    def update_aged_brie_again(self, item):
        if item.quality < 50:
            if item.sell_in < 0:
                self.increase_quality(item)

    def update_backstage_passes(self, item):
        if item.quality < 50:
            self.increase_quality(item)
            if item.quality < 50:
                if item.sell_in < 11:
                    self.increase_quality(item)
                if item.sell_in < 6:
                    self.increase_quality(item)

    def decrease_sellin(self, item):
        item.sell_in = item.sell_in - 1

    def increase_quality(self, item):
        item.quality = item.quality + 1

    def decrease_quality(self, item):
        item.quality = item.quality - 1
