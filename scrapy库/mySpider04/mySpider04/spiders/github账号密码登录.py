import scrapy
import logging
import re
logger = logging.getLogger(__name__)

'''class Github2Spider(scrapy.Spider):
    name = "github2"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/login"]

    def parse(self, response):
        print(111)
        yield scrapy.FormRequest.from_response(
            response,
            formdata={
                'login': '921503996@qq.com',
                'password': 'zbj1999$',
            },
            callback = self.parse_login
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
            logger.debug(f"Response Body: {response.text}")'''

class Github2Spider(scrapy.Spider):
    name = "github2"
    # allowed_domains = ["github.com"]
    start_urls = ["http://github.com/session"]

    def parse(self, response):
        formdata = {
            'login': '921503996@qq.com',
            'password': 'zbj1999$',
        }
        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            headers={'Referer': 'https://github.com/'},
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