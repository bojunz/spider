import scrapy
import re

class GameSpider(scrapy.Spider):
    name = "game"
    allowed_domains = ["4399.com"]
    start_urls = ["https://my.4399.com"]

    def start_requests(self):

        #方法一，直接加cookie
        # cookie = "_4399tongji_vid=169739461347719; _4399tongji_st=1697394613; Hm_lvt_5c9e5e1fa99c3821422bf61e662d4ea5=1697394614; \
        # Hm_lvt_e5a07b5994f78634294b9c347a5be7d2=1697394614; _4399stats_vid=16973946144773093; USESSIONID=fe4f5701-c360-\
        # 42da-99e4-56dd86bcb491; phlogact=l223524; ck_accname=zbj1596357; Puser=zbj1596357; Qnick=; Uauth=4399|1|2023\
        # 1016|my.|1697394884495|5924973b16b35c006863f34430dfa21a; Pauth=213557530|zbj1596357|t3ce7n53269648abe474\
        # 5964aa0eb565|1697394884|10002|ce6888f66acb17a984087e2a6095271e|0; Xauth=b7d4a33c933013a4375ca2e5555\
        # 0b110; ptusertype=my.4399_login; Pnickset=1; zone_guide_date=1697472000; zone_guide_time=1; ol=1; _gprp_c=""; Pmtime=5d1c\
        # 08e4335c400f94ad%7C1697394968; Hm_lpvt_5c9e5e1fa99c3821422bf61e662d4ea5=1697394978; Hm_lpvt_e5a07b5994f78634294b9c\
        # 347a5be7d2=1697394978"
        # cookie_dict = {}
        # for i in cookie1.split(';'):
        #     cookie_dict[i.split('=')[0]] = i.split(('='))[1]
        # yield scrapy.Request(url=self.start_urls[0],callback=self.parse,cookies=\
        #                      cookie_dict)

        #方法二，加入headers, headers 方法记得要把setting中 COOKIES_ENABLED = False
        # cookie1 = '_4399tongji_vid=169739461347719; _4399tongji_st=1697394613; Hm_lvt_5c9e5e1fa99c3821422bf61e662d4ea5=1697394614; Hm_lvt_e5a07b5994f78634294b9c347a5be7d2=1697394614; _4399stats_vid=16973946144773093; USESSIONID=fe4f5701-c360-42da-99e4-56dd86bcb491; phlogact=l223524; ck_accname=zbj1596357; Puser=zbj1596357; Qnick=; Uauth=4399|1|20231016|my.|1697394884495|5924973b16b35c006863f34430dfa21a; Pauth=213557530|zbj1596357|t3ce7n53269648abe4745964aa0eb565|1697394884|10002|ce6888f66acb17a984087e2a6095271e|0; Xauth=b7d4a33c933013a4375ca2e55550b110; ptusertype=my.4399_login; Pnickset=1; zone_guide_date=1697472000; zone_guide_time=1; ol=1; _gprp_c=""; Pmtime=5d1c08e4335c400f94ad%7C1697394968; Hm_lpvt_5c9e5e1fa99c3821422bf61e662d4ea5=1697394978; Hm_lpvt_e5a07b5994f78634294b9c347a5be7d2=1697394978'
        # header = {
        #     'cookie' :cookie1
        # }
        # yield scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=header)

        #方法3

        pass

    def parse(self, response):
        print(response.request.url)
        print(response)
        # print(response.text)
        print(re.findall('zbj1596357',response.text,re.S))

