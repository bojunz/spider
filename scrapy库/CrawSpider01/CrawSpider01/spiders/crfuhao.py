import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FuhaoSpider(CrawlSpider):
    name = "crfuhao"
    allowed_domains = ["www.phb123.com"]
    start_urls = ["https://www.phb123.com/renwu/fuhao/shishi.html"]

    rules = (Rule(LinkExtractor(allow=r"shishi_\d"),
                  callback="parse_item",
                  follow=True),)

    def parse_item(self, response):
        trs = response.xpath('//table[@class="rank-table"/tbody/tr')
        trs = trs[1:]
        for tr in trs:
            rank =tr.xpath('./td[1]/text()').extract_first()
            name =tr.xpath('./td[2]/p/text()').extract_first()
            wealth =tr.xpath('./td[3]/text()').extract_first()
            area = tr.xpath('./td[5]/a/text()').extract_first()
            print(name,rank,area,wealth,)
