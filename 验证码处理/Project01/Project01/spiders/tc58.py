import scrapy,re,base64
from fontTools.ttLib import TTFont

class Tc58Spider(scrapy.Spider):
    name = "tc58"
    # allowed_domains = ["58.com"]
    start_urls = ["https://bj.58.com/pinpaigongyu/?PGTID=0d200001-0000-1a67-b333-9a4955744969&ClickID=2"]

    def font(self,text):
        base_str = re.findall("\{font-family:'fangchan-secret';src:url\('data:application\/font-ttf;charset=utf-8;base64(.*?)'\) format\('truetype'\)\}",text)
        base_str = re.findall("\{font-family:'fangchan-secret';src:url\('data:application\/font-ttf;charset=utf-8;base64,(.*?)'\) format\('truetype'\)\}",
            text)[0]
        data = base64.decodebytes(base_str.encode())
        with open('font.woff', 'wb') as f:
            f.write(data)

        font = TTFont('font.woff')
        font_map = font.getBestCmap()
        print(font_map)
        return font_map

    def font_change(self,text,font_dict):
        new_money = ''
        for m in text:
            b=m
            b = b.encode('unicode_escape')
            try:
                b = re.findall(r"u(.*?)'",str(b))[0]
                b = int(b,16)
                value = font_dict.get(b,None)
                if value:
                    new_money += str(int(value[-2:])-1)
                else:
                    new_money += m
            except IndexError:
                new_money += m
        return new_money

    def parse(self, response):
        house_li = response.xpath('//ul[@class="list"]//li')
        font_dict = self.font(response.text)
        for house in house_li:
            title = house.xpath('.//h2/text()').extract_first()
            room = house.xpath('.//p[1]/text()').extract_first()
            info = house.xpath('.//p[3]/text()').extract()
            price = house.xpath('./a/div[3]//text()').extract()
            title = ''.join([i.strip() for i in title])
            room = ''.join([i.strip() for i in room])
            info = ''.join([i.strip() for i in info])
            price = ''.join([i.strip() for i in price])

            new_title = self.font_change(title,font_dict)
            new_room = self.font_change(room,font_dict)
            new_info = self.font_change(info,font_dict)
            new_price = self.font_change(price,font_dict)
            print(new_title,new_room,new_info,new_price)


