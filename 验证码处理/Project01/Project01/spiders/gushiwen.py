import scrapy
import os
from io import BytesIO
from PIL import Image
import pytesser3
import re


class GushiwenSpider(scrapy.Spider):
    name = "gushiwen"
    # allowed_domains = ["gushiwen.com"]
    start_urls = ["https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"]
    n = 0
    def parse(self, response):
        #获取验证码url
        code_url = response.xpath('//img[@id="imgCode"]/@src').extract_first()
        print(code_url)
        domain = r'https://so.gushiwen.cn'
        full_url = domain + code_url
        # full_url = os.path.normpath(os.path.join(domain,'',code_url))
        print(full_url)
        yield scrapy.Request(
            url = full_url,
            callback=self.parse_code,
            meta={'page':response},
            dont_filter=True
        )

    def parse_code(self,response):
        #在内存中去读取二进制图片数据
        img_data = BytesIO(response.body)
        img = Image.open(img_data)
        img2  = img.convert('L') #灰度图
        # img.show()

        avg = 150
        width, height = img2.size  # 获取图片大小
        pixel = img2.load()  # 获取当前像素值

        for x in range(width):
            for y in range(height):
                if pixel[x, y] < avg:
                    pixel[x, y] = 0
                else:
                    pixel[x, y] = 255

        ##降噪
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                count = 0  # 统计周边白色像素的个数
                if pixel[x, y - 1] > 245:  # 上
                    count += 1
                if pixel[x, y + 1] > 245:  # 下
                    count += 1
                if pixel[x - 1, y] > 245:  # 左
                    count += 1
                if pixel[x + 1, y] > 245:  # 右
                    count += 1
                if pixel[x - 1, y - 1] > 245:  # 左上
                    count += 1
                if pixel[x - 1, y + 1] > 245:  # 左下
                    count += 1
                if pixel[x + 1, y + 1] > 245:  # 右下
                    count += 1
                if pixel[x + 1, y - 1] > 245:  # 右上
                    count += 1

                if count > 5:
                    pixel[x, y] = 255

        img2.show()
        code = pytesser3.image_to_string(img2)
        code = code.split('\n')[0]
        print(f'第1次尝试')
        print(111,code)
        page = response.meta['page']

        yield scrapy.FormRequest.from_response(
            page,
            formname="aspnetForm",
            formdata={
                'email':'921503996@qq.com',
                'pwd':'maqu123',
                'code':code,
            },
            callback = self.parse_login,
        )

    def parse_login(self,response):
        print(response.url,response.status)
        res = re.findall('我的收藏',response.text)
        if res:
            print('访问成功',res)
        else:
            self.n +=1
            print(f'第{self.n}次重试')
            yield scrapy.Request(
                url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx',
                callback=self.parse,
                dont_filter=True
            )