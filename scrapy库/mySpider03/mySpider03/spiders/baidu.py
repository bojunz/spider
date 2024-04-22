import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://baidu.com"]

    def parse(self, response):
        #查看返回状态
        print(response)
        #查看请求头
        print(response.request.headers)
        #查看返回IP
        print(response.request.meta['proxy'])
