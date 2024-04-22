from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path=r"C:\Users\bzz00\Desktop\chromedriver.exe")
browser.get('https://news.163.com/domestic/')

# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

#获取页面内容
i=1
while True:
    content = browser.page_source
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    tree = etree.HTML(content)
    text = tree.xpath('/html/body/div/div[3]/div[3]/div[1]/div[1]/div/div[3]/text()')
    # text = tree.xpath('/html/body/div/div[3]/div[3]/div[1]/div[1]/div/div[2]')[0]
    print(text,i)
    if text:
        print(text)
        break
    else:
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(5)
        load = tree.xpath('/html/body/div/div[3]/div[3]/div[1]/div[1]/div/a')
        print(load)
        if load:
            browser.find_element(By.CSS_SELECTOR,'.load_more_btn').click()
            time.sleep(2)
        print('111')
        i+=1
        print('not yet')
time.sleep(5)
