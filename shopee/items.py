# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ShopeeItem(scrapy.Item):
    url = scrapy.Field()
    shop_name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    discount_rate = scrapy.Field()
    describe = scrapy.Field()
    n_solded = scrapy.Field()
    rating = scrapy.Field()
    n_items = scrapy.Field()
    type = scrapy.Field()
