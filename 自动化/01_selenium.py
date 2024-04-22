from selenium import webdriver

browser = webdriver.Chrome()

browser.set_window_size(800,800)

browser.get('https://www.baidu.com')
browser.get('https://www.douban.com')

browser.back()
browser.forward()
