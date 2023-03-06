# -*- coding: utf-8 -*-
from Solution.EX5.ItemFactory import get_item_by_name


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item(item)

    def update_item(self, item):
        item = get_item_by_name(item)
        item.update()
