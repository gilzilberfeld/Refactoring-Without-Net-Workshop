# -*- coding: utf-8 -*-
from Solution.EX3.StoredItems import *


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item(item)

    def update_item(self, item):
        match item.name:
            case "Aged Brie":
                AgedBrie(item).update()
            case "Backstage passes to a TAFKAL80ETC concert":
                Backstage(item).update()
            case "+5 Dexterity Vest" | "Elixir of the Mongoose":
                DexterityOrElixir(item).update()
