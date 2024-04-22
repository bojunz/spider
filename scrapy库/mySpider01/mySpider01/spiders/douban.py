import scrapy
from ..items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = "douban"  #爬虫标识符
    allowed_domains = ["www.douban.com"]  #搜索的域名范围
    start_urls = ["https://movie.douban.com/top250"] #爬取的url列表，从这里开始抓取数据
    # start_urls = ["https://www.baidu.com"] #爬取的url列表，从这里开始抓取数据


    def parse(self, response):
        items = []
        div = response.xpath("//li//div[@class='hd']")
        director = response.xpath("//li//div[@class='bd']")
        score = response.xpath("//li//div[@class='star']/span[2]/text()").extract()
        for i,j,s in zip(div,director,score):
            item = DoubanItem()
            title = i.xpath(".//span[@class='title']/text()").extract()
            director = j.xpath("./p/text()").extract()
            # print(director,'-------------1---------------')
            director = ''.join([j.strip() for j in [i.replace('\\a0','') for i in director]])
            # print(director,'-------------2---------------')
            item['title'] = title
            item['director'] = director
            item['score'] = s
            items.append(item)
        return items
