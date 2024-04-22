import scrapy
import logging
from selenium import webdriver
class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    # allowed_domains = ["wangyi.com"]
    # start_urls = ["https://news.163.com/domestic/"]
    start_urls = ["https://news.163.com/"]

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=r"C:\Users\bzz00\Desktop\chromedriver.exe")

    model_urls = []
    def parse(self, response):
        print(response.request)
        lis = response.xpath('//html/body/div/div[3]/div[2]/div[2]/div/ul/li')
        lis = lis[1:3] + lis[4:6]
        for i in lis:
            new_url = i.xpath('./a/@href').extract_first()
            self.model_urls.append(new_url)
            print(new_url,'wangyi')
            # logger.warning(url)
            yield scrapy.Request(
                url=  new_url,
                callback=self.parse_model
            )
    def parse_model(self,response):
        div_list = response.xpath('//div[@class="ndi_main"]/div')
        for div in div_list:
            title = div.xpath(".//h3/a/text()").extract_first()
            detail_url = div.xpath(".//h3/a/@href").extract_first()
            print('wangyi test',title ,detail_url)