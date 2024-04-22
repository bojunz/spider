import scrapy
from ..items import DoubanItem2
from ..items import DetailItem3
import logging

logger = logging.getLogger(__name__)
class Douban2Spider(scrapy.Spider):
    name = "douban_new"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250"]
    custom_settings = {
        'ITEM_PIPELINES':{"mySpider02.pipelines.DoubanNewPipeline": 300}
    }
    url = 'https://movie.douban.com/top250?start=%d&filter='

    def parse(self, response):
        #最大页数
        max_page = response.xpath('//div[@class="paginator"]/a[9]/text()').extract_first()
        print('这是最大页数',max_page)

        for page in range(0,int(max_page)*25,25):
            new_url = self.url%page
            yield scrapy.Request(
                url = new_url,
                callback= self.parse_douban,
                meta={'index':page}
            )
    def parse_douban(self,response):
        print(response.meta['index'],'当前页数')
        items = []
        div  = response.xpath('//div[@class="info"]')
        for i in div:
            item = DoubanItem2()
            # item = {}
            title = i.xpath('./div[1]/a/span[1]/text()').extract_first()
            introduce = i.xpath('./div[2]/p[1]/text()').extract()
            introduce = ''.join([j.strip() for j in [i.replace('\\xa0','') for i in introduce]])
            # logger.warning(title)
            item['title'] = title
            item['introduce'] = introduce
            # print(title,introduce)
            items.append(item)

            detail = i.xpath('./div[1]/a/@href').extract_first() #获取详情页url
            yield scrapy.Request(
                url=detail,
                callback=self.parse_detail,
                meta={"movie_detail":item}
            )

    def parse_detail(self,response):
        info = response.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]//text()').extract_first()
        # info = [i.strip() for i in info]
        moive_info = response.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div/span[1]//text()').extract_first()
        moive_info = ''.join([j.strip() for j in [i.replace('\\u3000', '') for i in moive_info]])
        detail = DetailItem3()
        detail['info'] = info
        detail['moive_info'] = moive_info

        item = response.meta['movie_detail']
        item['detail'] = detail
        print(item)
        # logger.warning(item)
        # exit(-1)

        # yield item

        # next_page = response.xpath('//div[@class="paginator"]/span[3]/a/@href').extract_first()
        # logger.warning(next_page)
        # if next_page:
        #     next_page = 'https://movie.douban.com/top250'+next_page
        #     #调度器
        #     yield scrapy.Request(
        #         #新的url请求地址
        #         url=next_page,
        #         #执行当前的结果交给谁处理
        #         callback=self.parse,
        #
        #     )

