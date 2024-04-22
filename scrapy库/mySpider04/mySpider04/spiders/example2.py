import scrapy


class Example2Spider(scrapy.Spider):
    name = "example2"
    allowed_domains = ["eaample2.com"]
    start_urls = ["https://eaample2.com"]

    '''第一种方法'''
    def start_requests(self):
        cookie = ""
        cookie_dict = {}
        for i in cookie.split(';'):
            cookie_dict[i.split('=')[0]] = i.split(('='))[1]
        yield scrapy.Request(url=self.start_urls[0],callback=self.parse,cookies=\
                             cookie_dict)

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={
                '用户名字段':'用户名',
                '密码字段':'密码',},
            callback = self.prase_login)

    '''第二种方法'''

    def start_requests(self):
        headers = {
            'Cookie':'cookie_info'
        }
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=headers)

    def parse(self, response):
        pass


