import scrapy
from ..items import HouseItem

class ChangshaSpider(scrapy.Spider):
    num = 0
    name = "changsha"
    # allowed_domains = ["cs.58.com"]
    start_urls = ["https://cs.58.com/zufang/"]
    custom_settings = {
        'ITEM_PIPELINES': {"house.pipelines.HousePipeline": 300}
    }
    url = 'https://cs.58.com/zufang/pn%d/'

    def parse(self,response):
        max_page = response.xpath("//div[@class='pager']//a[position()=last()-1]//span/text()").extract_first()
        print(max_page)
        for i in range(int(max_page)):
            new_url = self.url%i
            yield scrapy.Request(
                url=new_url,
                callback=self.parse_info,
            )

    def parse_info(self, response):
        num = 0
        divs = response.xpath('//div[@class="des"]')
        for div in divs:
            item = HouseItem()
            title = div.xpath('./h2/a/text()').extract_first()
            area = div.xpath('./p[1]/text()').extract_first()
            location = div.xpath('.//p[2]/a/text()').extract_first()
            item['title'] = title.strip() if title else ""
            item['area'] = area.replace('\xa0','').strip() if area else ""
            item['location'] = location.strip() if location else ""
            item['num'] = str(self.num)
            self.num += 1
            print(item)
            yield item

