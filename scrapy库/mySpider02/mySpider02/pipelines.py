# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Myspider02Pipeline:
    def process_item(self, item, spider):
        print('这是初始管道')
        return item

class DoubanPipeline:
    fp = None

    def open_spider(self,spider):
        if spider.name=='douban':
            print('爬虫开始运行')
            self.fp = open('./douban.txt','a',encoding='utf8')


    def process_item(self, item, spider):
        if spider.name == 'douban':
            print('这是第一个管道')
            self.fp.write(f"{item['title']}:{item['director']:{item['score']}}\n")
            return item

    def close_spider(self,spider):
        if spider.name == 'douban':
            print('爬虫结束运行')
            self.fp.close()

class DoubanNewPipeline:
    fp = None
    def open_spider(self,spider):
            print('爬虫开始运行')
            self.fp = open('./douban.txt','a',encoding='utf8')


    def process_item(self, item, spider):
            self.fp.write(f"{item['title']}:{item['introduce']}\n")
            return item

    def close_spider(self,spider):
            print('爬虫结束运行')
            self.fp.close()