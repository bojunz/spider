import scrapy
from ..items import DoubanItem
import logging

logger = logging.getLogger(__name__)
class DoubanSpider(scrapy.Spider):
    name = "douban"  #爬虫标识符
    # allowed_domains = ["www.douban.com"]  #搜索的域名范围
    start_urls = ["https://movie.douban.com/top250"] #爬取的url列表，从这里开始抓取数据
    # start_urls = ["https://www.baidu.com"] #爬取的url列表，从这里开始抓取数据


    def parse(self, response):
        #最大页数
        max_page = response.xpath('//div[@class="paginator"]/a[9]/text()').extract_fist()
        logger.warning(max_page)


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

            # print(title)
            # logging.warning(title)
            logger.warning(title)

            item['title'] = title
            item['director'] = director
            item['score'] = s
            # yield item

        # next_url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        next_url = response.xpath('//div[@class="paginator"]/span[3]/a/@href').extract_first()

        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url
            logger.warning(next_url)
            yield scrapy.Request(
                #新的请求地址，重复下载过程
                url= next_url,
                #把当前response函数交给指定解析器处理
                callback= self.parse,

            )
