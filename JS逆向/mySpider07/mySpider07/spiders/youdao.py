import scrapy
from time import time
import random
from hashlib import md5
import logging


logger = logging.getLogger(__name__)
class YoudaoSpider(scrapy.Spider):
    name = "youdao"
    # allowed_domains = ["fanyi.youdao.com"]
    # start_urls = ["https://fanyi.youdao.com/index.html"]
    start_urls = ["https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"]
    # start_urls = ["https://dict.youdao.com/webtranslate"]
    cookie = 'OUTFOX_SEARCH_USER_ID=-1678191860@10.130.108.42; OUTFOX_SEARCH_USER_ID_NCOO=494302586.9246066'
    cookie_dict = {}
    for i in cookie.split('; '):
        cookie_dict[i.split('=')[0]] = i.split('=')[1]
    def start_requests(self):
        word = 'spider'
        lts = str(int(time()*1000))
        salt = lts+str(random.randint(0,9))
        sign = 'fanyideskweb' + word + salt + 'Ygy_4c=r#e#4EX^NUGUc5'
        md = md5()
        md.update(sign.encode())  # 设置编码格式
        sign =  md.hexdigest()  # 获取加密的数据

        post_data ={
            'i': word,
        'from': 'auto',
        'to':'',
        'dictResult': 'true',
        'keyid': 'webfanyi',
        'sign': sign,
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': 'client, mysticTime, product',
        'mysticTime': '1703487465046',
        'keyfrom':'fanyi.web',
        'mid': '1',
        'screen': '1',
        'model': '1',
        'network': 'wifi',
        'abtest': '0',
        'yduuid': 'abcdefg',
        }
        print('aaa')
        yield scrapy.FormRequest(
            self.start_urls[0],
            formdata=post_data,
            callback=self.parse,
            cookies=self.cookie_dict,
            headers={
                'Accept':'application / json, text / plain, * / *',
                'Host':'dict.youdao.com',
                'Origin':'https://fanyi.youdao.com',
                'Referer':'https://fanyi.youdao.com/',
            }
        )
    def parse(self, response):
        logger.warning('success')
        logger.warning(response,response.status,response.text,response.headers)
