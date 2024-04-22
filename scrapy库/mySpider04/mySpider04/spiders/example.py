import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

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
                '密码字段':'密码'
            },
            callback = self.prase_login

        )
    #第二种方法
    def parse(self, response):
        user = 'usraccount'
        password = 'password'
        post_data = {
             '用户名字段': user,
             '密码字段': password
        }
        yield scrapy.FormRequest(url='post请求网址',formdata=post_data,callback=self.prase_login

        )

    def prase_login(self):
        pass