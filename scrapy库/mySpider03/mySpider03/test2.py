from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By
import re
browser = webdriver.Chrome(executable_path=r"C:\Users\bzz00\Desktop\chromedriver.exe")
browser.get('https://news.163.com/domestic/')

# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

#获取页面内容
bottom = []

while not bottom:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    page_text = browser.page_source
    bottom = re.findall(r':-\)已经到最后啦~',page_text)
    print(bottom)
    time.sleep(1)

    if not bottom:
        try:
            browser.find_element(By.CSS_SELECTOR,'.load_more_btn').click()
        except:
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(5)
