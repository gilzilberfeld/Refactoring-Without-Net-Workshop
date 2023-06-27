import unittest

from approvaltests.approvals import verify

from Solution.EX6.GildedRose import GildedRose
from Solution.EX6.Item import Item
from Solution.EX6.NotificationService import NotificationService

items = [
    Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
    Item(name="Aged Brie", sell_in=2, quality=0),
    Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
    Item(name="Conjured demon holding vessel", sell_in=10, quality=85)
]


def print_items():
    item_log = "name, sellIn, quality\n"
    for item in items:
        item_log += ("%s\n" % item)
    item_log += "\n"

    return item_log


class MockNotifier(NotificationService):

    def __init__(self):
        self.log = ""

    def notify_town_crier(self, message):
        self.log += message
        self.log += "\n"



class GildedRoseApprovals(unittest.TestCase):

    def test_update_quality_30_days(self):
        log = ""
        shop = GildedRose(items, MockNotifier())

        for day in range(1, 30):
            log += "Day " + str(day) + "\n"
            log += print_items()
            shop.update_quality()
            log += "\n"

        verify(log)

    def test_notification_updates_30_days(self):
        notifier = MockNotifier()
        shop = GildedRose(items, notifier)

        for day in range(1, 30):
            shop.update_quality()

        verify(notifier.log)

if __name__ == '__main__':
    unittest.main()
