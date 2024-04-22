import scrapy
import re

class Example3Spider(scrapy.Spider):
    name = "game3"
    allowed_domains = ["4399.com"]
    start_urls = ["https://my.4399.com"]

    #改写start_request方法
    '''使用headers方法cookie要=Flase'''
    def start_requests(self):
        headers = {
        'cookie' : "_4399tongji_vid=169739461347719; _4399stats_vid=16973946144773093; Puser=zbj1596357; Qnick=; _gprp_c=""; home4399=yes; Hm_lvt_334aca66d28b3b338a76075366b2b9e8=1702527927; Hm_lpvt_334aca66d28b3b338a76075366b2b9e8=1702527927; UM_distinctid=18c669282b5542-05cb9a100daf37-26031051-144000-18c669282b6f37; USESSIONID=13a0fd3a-2451-4f7a-b141-2403963b1b8d; Qauth=9453de84-73df-4d3f-bd2e-dcd55d545e4d_1702527954324_aa0272d4; phlogact=l216026; Uauth=4399|1|20231214|www_home.|1702528046568|e493fd44b29df085a4b475c609574b43; Pauth=213557530|zbj1596357|t3ce7n532636eb0426acf2ba17fe02aa|1702528046|10002|c471c30cd3a411c9d61667c5a8eea249|0; ck_accname=zbj1596357; Xauth=df179d6230006f411a0c5c33adf991e6; ptusertype=www_home.4399_login; Sauth=213557530%7Czbj1596357%7C1702528046%7C1703392059%7Ccd30d52cd725f3224080%7C%7Czbj1596357%7C9fec6d5350af8ecc66ac04de2404f7f6; Pnickset=1; zone_guide_date=1702569600; zone_guide_time=2; Pnick=deleted; _4399tongji_st=1702528069; ol=1; Hm_lvt_e5a07b5994f78634294b9c347a5be7d2=1702528070; Hm_lvt_5c9e5e1fa99c3821422bf61e662d4ea5=1702528070; Pmtime=efe4def435e4a18001c7%7C1702528320; Hm_lpvt_5c9e5e1fa99c3821422bf61e662d4ea5=1702528318; Hm_lpvt_e5a07b5994f78634294b9c347a5be7d2=1702528318"

        }
        yield scrapy.Request(url=self.start_urls[0],callback=self.parse,headers=headers)
    def parse(self, response):
        #查找出来的参数
        print(response.request.url)
        print(response)
        print(re.findall('zbj1596357', response.text, re.S))
