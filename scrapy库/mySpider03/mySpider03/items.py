# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider03Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WYItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    content = scrapy.Field()
    pass
