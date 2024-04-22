from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
url = 'https://movie.douban.com/top250'
browser.get(url)
browser.set_window_size(1800,800)
while True:
    next_page = browser.find_elements(By.XPATH,'//span[@class="next"]/a')
    if next_page:
        next_page[0].click()
    else:
        break
# browser.implicitly_wait(10)

time.sleep(5)
