from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()

browser.set_window_size(800,800)

browser.get('https://www.baidu.com')

#第一个参数是方式，第二个是属性的值
#send_keys中输入需要的值
'''可以通过ID，NAME，CLASS_NAME'''
browser.find_element(By.ID,'kw').send_keys('大聪明')
time.sleep(2)
#点击
browser.find_element(By.ID,'su').click()
'''XPATH
browser.find_element(By.XPATH,'//*[@id="kw"]')'''

time.sleep(10)
browser.quit()