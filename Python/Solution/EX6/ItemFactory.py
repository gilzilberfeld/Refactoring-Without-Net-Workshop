from Solution.EX6.StoredItems import *


def get_item_by_name(item):
    match item.name:
        case "Aged Brie":
            return AgedBrie(item)
        case "Backstage passes to a TAFKAL80ETC concert":
            return Backstage(item)
        case "+5 Dexterity Vest" | "Elixir of the Mongoose":
            return DexterityOrElixir(item)
        case "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item)
        case "Conjured":
            return Conjured(item)
