import scrapy
import logging
import time
from ..items import MooncakeItem


logger = logging.getLogger(__name__)
class ChinazSpider(scrapy.Spider):
    name = "chinaz"
    # allowed_domains = ["sc.chinaz.com"]
    start_urls = ["https://699pic.com/zhuanti/longniansongfujiehaoyuan.html"]
    custom_settings = {
        'ITEM_PIPELINES':{"CrawSpider01.pipelines.MooncakePipeline": 301},
    }

    def parse(self, response):
        container = response.xpath('//ul[@class="swipeboxEx clearfix"]/li')
        for div in container:
            item = MooncakeItem()
            name = div.xpath('./a/img/@title').extract_first()
            link = div.xpath('./a/img/@src').extract_first()
            link = 'https:' + str(link)
            link = link.replace('_s', '')
            print(name,link)
            item['src'] = link
            item['name'] = name
            # logger.warning(name,link)
            time.sleep(2)
            print('--------正在爬取下一个---------')
            yield item
