# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import logging
import scrapy


logger = logging.getLogger(__name__)


class Crawspider01Pipeline:
    def process_item(self, item, spider):
        return item

class MooncakePipeline(ImagesPipeline):
    #根据图片地址进行图片数据请求
    def get_media_requests(self, item, info):
        print(1)
        logger.warning(item['src'])
        return scrapy.Request(item['src'])

    #指定图片名字以及路径
    def file_path(self, request, response=None, info=None, *, item=None):
        print(2)
        image_name = request.url.split('/')[-1]
        return image_name

    #返回数据给下一个即将执行的管道
    def item_completed(self, results, item, info):
        # 图片下载路径、url和校验和等信息
        print(results)
        return item