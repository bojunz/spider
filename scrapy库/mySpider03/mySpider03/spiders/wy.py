import scrapy
from selenium import webdriver
from ..items import WYItem
import logging

logger = logging.getLogger(__name__)
class WySpider(scrapy.Spider):
    name = "wy"
    # allowed_domains = ["wangyi.com"]
    start_urls = ["https://news.163.com/"]
    custom_settings = {
        'ITEM_PIPELINES': {"mySpider03.pipelines.Myspider03Pipeline": 300}
    }

    model_urls = []

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=r"C:\Users\bzz00\Desktop\chromedriver.exe")


    def parse(self, response):
        print('这是spider的parse函数')
        print(response.request)
        lis = response.xpath('//div[@class="ns_area list"]/ul/li')
        lis = lis[1:3] + lis[4:6]
        for i in lis:
            new_url = i.xpath('./a/@href').extract_first()
            self.model_urls.append(new_url)
            print(new_url, 'wangyi')
            yield scrapy.Request(
                url=new_url,
                callback=self.parse_model
            )
    def parse_model(self,response):
        print('这是spider的parse_model函数')
        div_list = response.xpath('//div[@class="ndi_main"]/div')
        for div in div_list:
            title = div.xpath(".//h3/a/text()").extract_first()
            detail_url = div.xpath(".//h3/a/@href").extract_first()
            item = WYItem()
            item['title'] = title
            print('wangyi test', title, detail_url)
            if detail_url: #None是广告，不是广告才发送详情页信息
                yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})

    def parse_detail(self,response):
        print('这是spider的parse_detail函数')
        content = response.xpath('//div[@class="post_body"]//text()').extract()
        content = ''.join(content)
        content = content.replace('\n','')
        item = response.meta['item']
        item['content'] = content
        print(content)
        yield item

