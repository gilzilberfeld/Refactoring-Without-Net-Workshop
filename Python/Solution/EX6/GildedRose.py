# -*- coding: utf-8 -*-
from Solution.EX6.ItemFactory import get_item_by_name


class GildedRose(object):

    def __init__(self, items, notifier):
        self.items = items
        self.notifier = notifier

    def update_quality(self):
        for item in self.items:
            self.update_item(item)

    def update_item(self, item):
        item = get_item_by_name(item)
        item.update()
        self.notifier.notify_town_crier(item.message)
