import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Crawspider01Item
import time

class CrdoubanSpider(CrawlSpider):
    name = "crdouban"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250?start=0&filter="]

    rules = (Rule(LinkExtractor(allow=r"top250\?start=\d+&filter="),
                  callback="parse_item",
                  follow=True),)

    def parse_item(self, response):
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        div = response.xpath('//div[@class="info"]')
        for n,i in enumerate(div):
            print(f'这是第{n}部电影')
            item = Crawspider01Item()
            # item = {}
            title = i.xpath('./div[1]/a/span[1]/text()').extract_first()
            introduce = i.xpath('./div[2]/p[1]/text()').extract()
            introduce = ''.join([j.strip() for j in [i.replace('\\xa0', '') for i in introduce]])
            introduce = introduce.replace('\xa0','---')
            item['title'] = title
            item['introduce'] = introduce
            # print(title,introduce)
            print(item)
            print('休息两秒')
            time.sleep(2)
