import unittest

from approvaltests.approvals import verify
from GildedRose.GildedRose import *
from GildedRose.Uncouchables.Item import *

items = [
    Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
    Item(name="Aged Brie", sell_in=2, quality=0),
    Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
]

def print_items():
    item_log = "name, sellIn, quality\n"
    for item in items:
        item_log += ("%s\n" % item)
    item_log += "\n"

    return item_log


class GildedRoseApprovals(unittest.TestCase):
    def test_items_before_and_after_quality_update(self):
        log = "Before Update\n"
        log += print_items()
        GildedRose(items).update_quality()
        log += "After Update\n"
        log += print_items()
        verify(log)


if __name__ == '__main__':
    unittest.main()
