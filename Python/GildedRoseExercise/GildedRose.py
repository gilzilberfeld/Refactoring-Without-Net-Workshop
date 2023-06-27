# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                pass
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage(item)
            elif item.name == "Aged Brie":
                self.update_aged_brie(item)
            else:
                self.update_others(item)

    def update_others(self, item):
        self.decrease_quality(item)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            self.decrease_quality(item)

    def decrease_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def update_aged_brie(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            self.increase_quality_under_50(item)

    def update_backstage(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in < 11:
                self.increase_quality_under_50(item)
            if item.sell_in < 6:
                self.increase_quality_under_50(item)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = 0

    def increase_quality_under_50(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
