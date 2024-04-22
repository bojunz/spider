import scrapy
import logging
import re
logger = logging.getLogger(__name__)

class GithubSpider(scrapy.Spider):
    name = "github"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/login"]
    '''点击session文件然后点击payload'''
    '''commit: Sign in
authenticity_token: THiflemKH3vjF18UtpedPF4tLitnqAoOXZfVhnB6scGei7ElFxn1dIYABdVTsmy3aHEqvtQ069SCBsid9V3eNw==
login: qwer
password: qwer
webauthn-conditional: undefined
javascript-support: true
webauthn-support: supported
webauthn-iuvpaa-support: unsupported
return_to: https://github.com/login
allow_signup: 
client_id: 
integration: 
required_field_b090: 
timestamp: 1702530749506
timestamp_secret: 0a01d949aeba3c4efbadf25bd067ec874f8eae7f60b5544e3f1f19a67ad26250'''
    def parse(self, response):
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        required_field = re.findall('required_field_[a-zA-Z0-9]{4}',response.text)[0]
        timestamp = response.xpath("//input[@name='timestamp']/@value").extract_first()
        timestamp_secret = response.xpath("//input[@name='timestamp_secret']/@value").extract_first()
        #print(authenticity_token,timestamp,timestamp_secret,required_field)

        post_data = {
            'commit': 'Sign in',
            'authenticity_token': authenticity_token,
            'login': '921503996@qq.com',
            'password': 'zbj1999$',
            'required_field_b090':required_field,
        #'javascript - support': 'true',
        #'webauthn - support': 'supported',
        #'webauthn - iuvpaa - support': 'unsupported',
        #'return_to: https': '// github.com / login',
        'timestamp': timestamp,
        'timestamp_secret': timestamp_secret,
        }
        print(post_data)
        yield scrapy.FormRequest(
            url='https://github.com/session',
            formdata=post_data,
            callback=self.parse_login,
        )

    def parse_login(self, response):
        print("Parsing login response...")
        if "bojun" in response.text:
            logger.info("Login successful!")
            # Add your further processing logic for successful login here
        else:
            logger.warning("Login failed!")
            # Log response status, headers, and body for debugging
            logger.debug(f"Response Status: {response.status}")
            logger.debug(f"Response Headers: {response.headers}")
            logger.debug(f"Response Body: {response.text}")

