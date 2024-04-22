# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Myspider03Pipeline:
    count = 0
    def process_item(self, item, spider):
        print('这是pipeline的计数函数')
        if spider.name =='wy':
            self.count +=1
            print(item)
        return item

    def close_spider(self,spider):
        print(self.count)
