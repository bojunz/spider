from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome()

browser.set_window_size(800,800)

browser.get('https://qzone.qq.com')

# 切换到iframe
browser.switch_to.frame('login_frame')
browser.find_element(By.ID,'switcher_plogin').click()
# time.sleep(5)
browser.find_element(By.ID,'u').send_keys(123456)
browser.find_element(By.ID,'p').send_keys(123456)
browser.find_element(By.ID,'login_button').click()
time.sleep(50)