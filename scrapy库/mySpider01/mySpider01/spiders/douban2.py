import scrapy
from ..items import DoubanItem2

class Douban2Spider(scrapy.Spider):
    name = "douban2"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        items = []
        div  = response.xpath('//div[@class="info"]')
        for i in div:
            item = DoubanItem2()
            # item = {}
            title = i.xpath('./div[1]/a/span[1]/text()').extract_first()
            introduce = i.xpath('./div[2]/p[1]/text()').extract()
            introduce = ''.join([j.strip() for j in [i.replace('\\xa0','') for i in introduce]])
            item['title'] = title
            item['introduce'] = introduce
            # print(title,introduce)
            items.append(item)
        return items
