# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    director = scrapy.Field()
    score = scrapy.Field()
    pass

class DoubanItem2(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    introduce = scrapy.Field()
    pass