# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazontutorialItem(scrapy.Item):
    name = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()

